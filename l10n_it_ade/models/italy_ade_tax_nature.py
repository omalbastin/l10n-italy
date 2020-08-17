# -*- coding: utf-8 -*-
#
# Copyright 2018    - Associazione Odoo Italia <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Code partially inherited by l10n_it_codice_carica OCA
#
from openerp import fields, models


class ItalyAdeTaxNature(models.Model):
    _name = 'italy.ade.tax.nature'
    _description = 'Tax Italian Nature'

    _sql_constraints = [('code',
                         'unique(code)',
                         'Code already exists!')]

    code = fields.Char(string='Code',
                       size=2)
    name = fields.Char(string='Name')
    help = fields.Text(string='Help')
    active = fields.Boolean(string='Active',
                            default=True)
