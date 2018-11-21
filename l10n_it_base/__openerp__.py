# -*- coding: utf-8 -*-
#
# Copyright 2010-18 - Associazione Odoo Italia <https://odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    'name': 'Italian Localisation - Base',
    'version': '8.0.0.2.15',
    'category': 'Localisation/Italy',
    'author': 'Odoo Italia Associazione,'
              'Odoo Community Association (OCA),'
              'SHS-AV s.r.l.',
    'maintainer': 'Antonio Maria Vigliotti',
    'website': 'https://odoo-italia.org/',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_view.xml',
        'views/res_partner_view.xml',
        'views/city_view.xml',
        'data/res.country.state.csv',
        'data/res.city.csv',
    ],
    # 'test': ['test/res_partner.yml'],
    'installable': True,
}
