# -*- coding: utf-8 -*-
#
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, orm


class AccountJournal(orm.Model):
    _inherit = "account.journal"

    _columns = {
        'rev_charge': fields.boolean(
            'Reverse Charge Journal',
            help="Check if reverse charge EU invoices journal"),
        'anom_sale_receipts': fields.boolean(
            'Anonimous sale receipts journal',
            help="Check if this is the Anonimous Sale Receipts Journal"),
        'proforma': fields.boolean(
            'Proforma journal',
            help="Check if this is a Proforma Journal"),
        'einvoice': fields.boolean(
            'E-Invoice journal',
            help="Check if this is a E-Invoice Journal"),
    }

    _defaults = {
        'rev_charge': False,
        'anom_sale_receipts': False,
        'proforma': False,
        'einvoice': False,
    }

    def onchange_check_subtype(self, cr, uid, ids, name,
                               type, rev_charge, anom_sale_receipts, proforma,
                               einvoice, context=None):
        if name == 'rev_charge' and rev_charge:
            if type != 'sale':
                return {'value': {name: False},
                        'warning': {
                    'title': 'Invalid setting!',
                    'message': 'Journal type must be sale'}
                }
            res = {'value': {name: True,
                             'anom_sale_receipts': False,
                             'proforma': False,
                             'einvoice': False}}
        elif name == 'anom_sale_receipts' and anom_sale_receipts:
            if type != 'sale':
                return {'value': {name: False},
                        'warning': {
                    'title': 'Invalid setting!',
                    'message': 'Journal type must be sale'}
                }
            res = {'value': {name: True,
                             'rev_charge': False,
                             'proforma': False,
                             'einvoice': False}}
        elif name == 'proforma' and proforma:
            if type not in ('purchase', 'sale'):
                return {'value': {name: False},
                        'warning': {
                    'title': 'Invalid setting!',
                    'message': 'Journal type must be sale or purchase'}
                }
            res = {'value': {name: True,
                             'rev_charge': False,
                             'anom_sale_receipts': False,
                             'einvoice': False}}
        elif name == 'einvoice' and einvoice:
            if type not in ('purchase', 'sale'):
                return {'value': {name: False},
                        'warning': {
                    'title': 'Invalid setting!',
                    'message': 'Journal type must be sale or purchase'}
                }
            res = {'value': {name: True,
                             'rev_charge': False,
                             'anom_sale_receipts': False,
                             'proforma': False}}
        else:
            res = {'value': {name: False}}
        return res
