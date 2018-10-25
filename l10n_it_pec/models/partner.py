# -*- coding: utf-8 -*-
#
# Copyright 2014    Associazione Odoo Italia (<https://www.odoo-italia.org>)
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    pec_mail = fields.Char(string='PEC Mail')
