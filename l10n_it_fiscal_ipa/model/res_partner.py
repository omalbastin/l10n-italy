# -*- coding: utf-8 -*-
#
# Copyright 2014    KTec S.r.l.
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    ipa_code = fields.Char(string='IPA Code')
    codice_destinatario = fields.Char(
        "Recipient Code",
        help="Il codice, di 7 caratteri, assegnato dal Sdi ai soggetti che "
             "hanno accreditato un canale; qualora il destinatario non abbia "
             "accreditato un canale presso Sdi e riceva via PEC le fatture, "
             "l'elemento deve essere valorizzato con tutti zeri ('0000000'). ")
