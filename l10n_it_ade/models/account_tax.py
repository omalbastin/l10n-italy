# -*- coding: utf-8 -*-
#
# Copyright 2017-19 - Associazione Odoo Italia <https://www.odoo-italia.org>
# Copyright 2017-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Code partially inherited by l10n_it_account of OCA
#
from openerp import fields, models
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _


class AccountTax(models.Model):
    _inherit = 'account.tax'

    nature_id = fields.Many2one(
        'italy.ade.tax.nature',
        string='Nature',
        help='Nature of tax code: may be taxable, out of scope, etc ...')
    non_taxable_nature = fields.Selection([
        ('N1', 'escluse ex art. 15'),
        ('N2', 'non soggette'),
        ('N3', 'non imponibili'),
        ('N4', 'esenti'),
        ('N5', 'regime del margine/IVA non esposta'),
        ('N6', 'inversione contabile (acq. in reverse charge)'),
        ('N7', 'IVA assolta in altro stato UE'),
        ('FC', 'FC applicazione IVA'),
    ], string="Non taxable nature (*DEPRECATED*)")
    payability = fields.Selection([
        ('I', 'Immediate payability'),
        ('D', 'Deferred payability'),
        ('S', 'Split payment'),
    ], string="VAT payability",
        default='I')
    law_reference = fields.Char(
        'Law reference', size=128)

    def get_tax_by_invoice_tax(self, cr, uid, invoice_tax, context=None):
        if ' - ' in invoice_tax:
            tax_descr = invoice_tax.split(' - ')[0]
            tax_ids = self.search(cr, uid, [
                ('description', '=', tax_descr),
            ], context=context)
            if not tax_ids:
                raise UserError(
                    _('Error'), _('No tax %s found') %
                    tax_descr)
            if len(tax_ids) > 1:
                raise UserError(
                    _('Error'), _('Too many tax %s found') %
                    tax_descr)
        else:
            tax_name = invoice_tax
            tax_ids = self.search(cr, uid, [
                ('name', '=', tax_name),
            ], context=context)
            if not tax_ids:
                raise UserError(
                    _('Error'), _('No tax %s found') %
                    tax_name)
            if len(tax_ids) > 1:
                raise UserError(
                    _('Error'), _('Too many tax %s found') %
                    tax_name)
        return tax_ids[0]
