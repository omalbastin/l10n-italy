# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Apulia Software s.r.l. (http://www.apuliasoftware.it)
#    @author Francesco Apruzzese <f.apruzzese@apuliasoftware.it>
#
#    License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
#
##############################################################################


from openerp import _, api, exceptions, fields, models


class StockPickingCarriageCondition(models.Model):

    _name = "stock.picking.carriage_condition"
    _description = "Carriage Condition"

    name = fields.Char(string='Carriage Condition',
                       required=True, translate=True)
    note = fields.Text(string='Note', translate=True)


class StockPickingGoodsDescription(models.Model):

    _name = 'stock.picking.goods_description'
    _description = "Description of Goods"

    name = fields.Char(string='Description of Goods',
                       required=True, translate=True)
    note = fields.Text(string='Note', translate=True)


class StockPickingTransportationReason(models.Model):

    _name = 'stock.picking.transportation_reason'
    _description = 'Reason for Transportation'

    name = fields.Char(string='Reason For Transportation',
                       required=True, translate=True)
    note = fields.Text(string='Note', translate=True)
    to_be_invoiced = fields.Boolean(string='To be Invoiced')


class StockPickingTransportationMethod(models.Model):

    _name = 'stock.picking.transportation_method'
    _description = 'Method of Transportation'

    name = fields.Char(string='Method of Transportation',
                       required=True, translate=True)
    note = fields.Text(string='Note', translate=True)


class StockDdtType(models.Model):

    _name = 'stock.ddt.type'
    _description = 'Stock DdT Type'
    _inherit = ['mail.thread']

    name = fields.Char(required=True)
    sequence_id = fields.Many2one('ir.sequence', required=True)
    note = fields.Text(string='Note')
    default_carriage_condition_id = fields.Many2one(
        'stock.picking.carriage_condition',
        string='Default Carriage Condition')
    default_goods_description_id = fields.Many2one(
        'stock.picking.goods_description',
        string='Default Description of Goods')
    default_transportation_reason_id = fields.Many2one(
        'stock.picking.transportation_reason',
        string='Default Reason for Transportation')
    default_transportation_method_id = fields.Many2one(
        'stock.picking.transportation_method',
        string='Default Method of Transportation')
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id, )


class StockPickingPackagePreparation(models.Model):

    _inherit = 'stock.picking.package.preparation'
    _rec_name = 'display_name'
    _order = 'date desc'

    @api.multi
    @api.depends('transportation_reason_id.to_be_invoiced')
    def _compute_to_be_invoiced(self):
        for ddt in self:
            ddt.to_be_invoiced = ddt.transportation_reason_id and \
                ddt.transportation_reason_id.to_be_invoiced or False

    def _default_ddt_type(self):
        return self.env['stock.ddt.type'].search([], limit=1)

    ddt_type_id = fields.Many2one(
        'stock.ddt.type', string='DdT Type', default=_default_ddt_type)
    ddt_number = fields.Char(string='DdT Number', copy=False)
    partner_invoice_id = fields.Many2one('res.partner')
    partner_shipping_id = fields.Many2one(
        'res.partner', string="Shipping Address")
    carriage_condition_id = fields.Many2one(
        'stock.picking.carriage_condition',
        string='Carriage Condition')
    goods_description_id = fields.Many2one(
        'stock.picking.goods_description',
        string='Description of Goods')
    transportation_reason_id = fields.Many2one(
        'stock.picking.transportation_reason',
        string='Reason for Transportation')
    transportation_method_id = fields.Many2one(
        'stock.picking.transportation_method',
        string='Method of Transportation')
    carrier_id = fields.Many2one(
        'res.partner', string='Carrier')
    parcels = fields.Integer('Parcels')
    display_name = fields.Char(
        string='Name', compute='_compute_display_name')
    volume = fields.Float('Volume')
    invoice_id = fields.Many2one(
        'account.invoice', string='Invoice',
        readonly=True, copy=False)
    to_be_invoiced = fields.Boolean(
        string='To be Invoiced', store=True,
        compute="_compute_to_be_invoiced",
        help="This depends on 'To be Invoiced' field of the Reason for "
             "Transportation of this DDT")
    weight_manual = fields.Float(
        string="Force Weight",
        help="Fill this field with the value you want to be used as weight. "
             "Leave empty to let the system to compute it")
    gross_weight = fields.Float(string="Gross Weight")
    check_if_picking_done = fields.Boolean(
        compute='_compute_check_if_picking_done',
    )

    @api.multi
    @api.depends('picking_ids',
                 'picking_ids.state')
    def _compute_check_if_picking_done(self):
        for record in self:
            record.check_if_picking_done = False
            for package in record.picking_ids:
                if package.state == 'done':
                    record.check_if_picking_done = True

    @api.onchange('partner_id', 'ddt_type_id')
    def on_change_partner(self):
        if self.ddt_type_id:
            addr = self.partner_id.address_get(['delivery', 'invoice'])
            self.partner_invoice_id = addr['invoice']
            self.partner_shipping_id = addr['delivery']
            self.carriage_condition_id = \
                self.partner_id.carriage_condition_id.id \
                if self.partner_id.carriage_condition_id else False
            self.goods_description_id = \
                self.partner_id.goods_description_id.id \
                if self.partner_id.goods_description_id else False
            self.transportation_reason_id = \
                self.partner_id.transportation_reason_id.id \
                if self.partner_id.transportation_reason_id else False
            self.transportation_method_id = \
                self.partner_id.transportation_method_id.id \
                if self.partner_id.transportation_method_id else False

    @api.multi
    def action_put_in_pack(self):
        for package in self:
            # ----- Check if package has details
            if not package.line_ids:
                raise exceptions.Warning(
                    _("Impossible to put in pack a package without details"))
            # ----- Assign ddt number if ddt type is set
            if package.ddt_type_id and not package.ddt_number:
                package.ddt_number = package.ddt_type_id.sequence_id.get(
                    package.ddt_type_id.sequence_id.code)
        return super(StockPickingPackagePreparation, self).action_put_in_pack()

    @api.multi
    def set_done(self):
        for picking in self.picking_ids:
            if picking.state != 'done':
                raise exceptions.Warning(
                    _("Not every picking is in done status"))
        for package in self:
            if not package.ddt_number:
                package.ddt_number = package.ddt_type_id.sequence_id.get(
                    package.ddt_type_id.sequence_id.code)
        self.write({'state': 'done', 'date_done': fields.Datetime.now()})
        return True

    @api.one
    @api.depends('name', 'ddt_number', 'partner_id', 'date')
    def _compute_display_name(self):
        name = u''
        if self.name:
            name = self.name
        if self.ddt_number and self.name:
            name = u'[{package}] {ddt}'.format(package=self.name,
                                               ddt=self.ddt_number)
        if self.ddt_number and not self.name:
            name = self.ddt_number
        if not name:
            name = u'{partner} of {date}'.format(partner=self.partner_id.name,
                                                 date=self.date)
        self.display_name = name

    @api.one
    @api.depends('package_id',
                 'package_id.children_ids',
                 'package_id.ul_id',
                 'package_id.quant_ids',
                 'picking_ids',
                 'picking_ids.move_lines',
                 'picking_ids.move_lines.quant_ids',
                 'weight_manual')
    def _compute_weight(self):
        res = super(StockPickingPackagePreparation, self)._compute_weight()
        if not self.package_id:
            quants = self.env['stock.quant']
            for picking in self.picking_ids:
                for line in picking.move_lines:
                    for quant in line.quant_ids:
                        if quant.qty >= 0:
                            quants |= quant
            weight = sum(l.product_id.weight * l.qty for l in quants)
            self.net_weight = weight
            self.weight = weight
        if self.weight_manual:
            self.weight = self.weight_manual
        return res

    @api.multi
    def create_invoice(self):
        # ----- Check if sale order related to ddt are invoiced. Show them.
        invoiced_sale = [
            picking.sale_id.id
            for picking in self.picking_ids
            if picking.sale_id and picking.sale_id.invoice_ids]
        if invoiced_sale:
            return {
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'tree,form',
                'res_model': 'sale.order',
                'target': 'current',
                'domain': '[("id", "in", {ids})]'.format(ids=invoiced_sale),
            }
        # ----- Open wizard to create invoices
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'ddt.create.invoice',
            'target': 'new',
        }

    @api.multi
    def unlink(self):
        for ddt in self:
            if ddt.invoice_id:
                raise exceptions.Warning(
                    _("Document {d} has invoice linked".format(
                        d=ddt.ddt_number)))
        return super(StockPickingPackagePreparation, self).unlink()


class StockPickingPackagePreparationLine(models.Model):

    _inherit = 'stock.picking.package.preparation.line'

    invoiceable = fields.Selection(
        [('none', 'None'), ('invoiceable', 'Invoiceable')],
        default='invoiceable')

    @api.multi
    def get_move_data(self):
        move_data = super(StockPickingPackagePreparationLine,
                          self).get_move_data()
        if self.invoiceable == 'invoiceable':
            move_data.update({
                'invoice_state': '2binvoiced',
            })
        return move_data
