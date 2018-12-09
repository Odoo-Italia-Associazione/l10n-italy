# -*- coding: utf-8 -*-
#    Copyright (C) 2014-2018 Associazione Odoo Italia (<http://www.odoo-italia.org>)
#    Copyright (C) 2016      Andrea Gallina (Apulia Software)
#    Copyright (C) 2018      Antonio Vigliotti <https://www.zeroincombenze.it>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#
{
    'name': 'Italian Localisation - Fiscal Code',
    'version': '10.0.1.0.2',
    'category': 'Localisation/Italy',
    'author': "Odoo Italia Network, Odoo Community Association (OCA)",
    'website': 'https://odoo-community.org/',
    'license': 'AGPL-3',
    'depends': ['base_vat'],
    'external_dependencies': {
        'python': ['codicefiscale'],
    },
    'data': [
        'views/fiscalcode_view.xml',
        'wizard/compute_fc_view.xml',
        'data/res.city.it.code.csv',
        "security/ir.model.access.csv"
    ],
    'installable': True
}
