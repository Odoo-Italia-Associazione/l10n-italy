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
    'name': 'EInvoice + FatturaPA',
    'summary': 'Infrastructure for Italian Electronic Invoice + FatturaPA',
    'version': '10.0.2.1.1',
    'category': 'Localization/Italy',
    'author': 'Odoo Italia Associazione,'
              'Odoo Community Association (OCA)',
    'website': 'http://www.odoo-italia.org',
    'license': 'LGPL-3',
    "depends": [
        'account',
        'l10n_it_fiscalcode',
        'document',
        'l10n_it_fiscal_ipa',
        'l10n_it_rea',
        'base_iban',
        'l10n_it_ade',
        'l10n_it_pec',
        'l10n_it_fiscal_payment_term',
    ],
    "data": [
        'security/ir.model.access.csv',
        'data/fatturapa_fiscal_position.xml',
        'data/fatturapa_data.xml',
        'data/welfare.fund.type.xml',
        'views/account_view.xml',
        'views/company_view.xml',
        'views/regime_fiscale_view.xml',
        'views/fiscal_position_view.xml',
    ],
    # "demo": [
    #     'demo/account_tax.xml',
    #     'demo/res_partner.xml',
    #     'demo/account_invoice_fatturapa.xml',
    # ],
    'installable': True,
    'external_dependencies': {
        'python': [
            'pyxb',  # pyxb 1.2.4
        ],
    }
}
