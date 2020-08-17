# -*- coding: utf-8 -*-
#    Copyright (C) 2016    Apulia Software srl <info@apuliasoftware.it>
#    Copyright (C) 2017-18 SHS-AV s.r.l. <https://www.zeroincombenze.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models, _
from openerp.exceptions import Warning as UserError


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.one
    def _inv_check4date(self, invoice, date_invoice):
        where = [('type', '=', invoice.type),
                 ('journal_id', '=', invoice.journal_id.id),
                 ('date_invoice', '>', date_invoice),
                 ('state', '!=', 'draft'),
                 ('state', '!=', 'cancel'),
                 ]
        if invoice.period_id:
            period_model = self.env['account.period']
            fiscalyear_id = period_model.browse(
                invoice.period_id.id).fiscalyear_id.id
            periods = period_model.search([('fiscalyear_id',
                                            '=',
                                            fiscalyear_id)]).ids
            where.append(('period_id', 'in', periods))
        return self.search(where)

    @api.multi
    def action_number(self):
        res = True
        for invoice in self:
            # if invoice.journal_id.proforma:
            #     continue
            inv_type = invoice.type
            if inv_type == 'in_invoice' or inv_type == 'in_refund':
                date_invoice = invoice.registration_date
                res = self._inv_check4date(invoice, date_invoice)
            elif inv_type == 'out_invoice' or inv_type == 'out_refund':
                date_invoice = invoice.date_invoice
                res = self._inv_check4date(invoice, date_invoice)
            if not res:
                raise UserError(
                    _('Cannot create invoice!'
                      ' Post the invoice with a greater date'))
        return super(AccountInvoice, self).action_number()

    @api.multi
    def copy(self, default=None):
        default = default or {}
        default.update({
            'registration_date': False,
        })
        return super(AccountInvoice, self).copy(default=default)
