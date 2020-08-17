# -*- coding: utf-8 -*-
#
# Copyright 2017-18 - Associazione Odoo Italia <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Code partially inherited by l10n_it_account of OCA
#
{
    "name": "Definizioni di Base Agenzia delle Entrate",
    "version": "8.0.0.1.10",
    "category": "Localization/Italy",
    "summary": "Codice con le definizioni dei file xml Agenzia delle Entrate",
    "author": "SHS-AV s.r.l.,"
              " Odoo Italia Associazione",
    "maintainer": "Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "license": "AGPL-3",
    "depends": [
        'account',
    ],
    "data": [
        'security/ir.model.access.csv',
        'data/italy_ade_codice_carica.xml',
        'data/italy_ade_invoice_type.xml',
        'data/italy_ade_tax_nature.xml',
        'views/ir_ui_menu.xml',
        'views/codice_carica_view.xml',
        'views/invoice_type_view.xml',
        'views/tax_nature_view.xml',
        'views/account_tax_view.xml',
        'views/account_journal.xml',
    ],
    'installable': True,
    "external_dependencies": {
        "python": ["pyxb"],
    }
}
