# -*- coding: utf-8 -*-
#
# Copyright 2010-2011, Odoo Italian Community
# Copyright 2011-2017, Associazione Odoo Italia <https://odoo-italia.org>
# Copyright 2014, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, orm


class L10nItConfigSettings(orm.TransientModel):
    _name = 'l10n_it.config.settings'
    _inherit = 'res.config.settings'

    _columns = {
        'module_l10n_it_pec': fields.boolean(
            'Use Pec Mail in Partner Profile',
            help="""Install l10n_it_pec module for pec mail management"""
        ),
        'module_l10n_it_fiscalcode': fields.boolean(
            'Use fiscal code in Partner Profile',
            help="""Install l10n_it_fiscalcode module for fiscal
code management"""
        ),
    }
