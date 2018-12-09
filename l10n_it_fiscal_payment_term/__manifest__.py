# -*- coding: utf-8 -*-
#
# Copyright 2014    - Davide Corio <davide.corio@abstract.it>
# Copyright 2015-16 - Lorenzo Battistini - Agile Business Group
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
{
    'name': 'Fiscal payment term',
    'summary': 'Electronic & Fiscal invoices payment',
    'version': '10.0.1.0.0',
    'category': 'Localization/Italy',
    'author': 'Odoo Italia Associazione,'
              'Odoo Community Association (OCA)',
    'website': 'http://www.odoo-italia.org',
    'license': 'LGPL-3',
    'depends': [
        'account',
        'l10n_it_ade',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/payment_term_view.xml',
        'views/payment_method_view.xml',
        'data/fatturapa_data.xml',
    ],
    'installable': True,
}
