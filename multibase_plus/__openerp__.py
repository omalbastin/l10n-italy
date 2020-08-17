# -*- coding: utf-8 -*-
# Copyright 2016 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# License AGPL-30 or later (http://www.gnu.org/licenses/agpl).
{
    'name': "multibase_plus",

    'summary': """Enhanced Odoo Features""",

    'author': "SHS-AV s.r.l.",
    'website': "https://www.zeroincombenze.it/",

    'category': 'Base',
    'license': 'LGPL-3',
    'version': '8.0.0.1.1',

    'depends': ['base',
                'sale'],

    'data': [
        # "views/sale_order_view.xml",
        "views/account_invoice_view.xml",
    ],
    'installable': True
}
