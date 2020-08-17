# -*- coding: utf-8 -*-
#
# Copyright 2017    SHS-AV s.r.l. <https://www.zeroincombenze.it>
# Copyright 2017    Didotech srl <http://www.didotech.com>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2017: SHS-AV s.r.l.] First version
#
import logging

import openerp.release as release
from openerp.osv import fields

_logger = logging.getLogger(__name__)
try:
    if release.major_version in ('6.1', '7.0'):
        import decimal_precision as dp
    else:
        import decimal_precision as dp
except ImportError as err:
    _logger.debug(err)


class AccountInvoice(orm.Model):
    _inherit = "account.invoice"

    # TODO :merge with fatturapa to avoid duplicate definition
    _columns = {
        'sub_type': fields.selection([
            ('', 'Ordinary'),
            ('TD04', 'Credit Note'),
            ('TD05', 'Debit Note'),
            ('TD07', 'Receipt or Simple Invoice'),
            ('TD08', 'Refund Receipt'),
            ('TD10', 'Purchase invoice of goods'),
            ('TD11', 'Purchase invoice of services'),
            ('ANOM_RECEIPT', 'Anonimous Receipt'),
            ('PROFORMA', 'Proforma'),
            ('SELF', 'Self-invoice'),
        ], string="Invoice sub-type"),
    }
