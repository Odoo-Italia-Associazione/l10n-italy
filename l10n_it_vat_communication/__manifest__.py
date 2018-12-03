# -*- coding: utf-8 -*-
#    Copyright (C) 2017    SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2017: SHS-AV s.r.l.] First version
{
    "name": "Comunicazione periodica IVA",
    "version": "10.0.0.1.12",
    'category': 'Generic Modules/Accounting',
    'license': 'LGPL-3',
    "depends": [
        "l10n_it_ade",
        "l10n_it_fiscalcode",
        "account_invoice_entry_date",
        # "l10n_it_vat_registries",
    ],
    "author": "SHS-AV s.r.l.,"
    " Odoo Italia Associazione",
    'maintainer': 'Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>',
    'website': 'https://odoo-italia.org',
    'data': ['security/ir.model.access.csv',
             'views/set_date_range.xml',
             'views/account_view.xml',
    #          'views/wizard_export_view.xml',
    #          'communication_workflow.xml',
             ],
    'external_dependencies': {
        'python': ['pyxb', 'unidecode'],
    },
    'demo': [],
    'installable': False,
}
