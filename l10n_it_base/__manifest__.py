# -*- coding: utf-8 -*-
#
# Copyright 2017-2018, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2010-2018, Associazione Odoo Italia <https://odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    'name': 'Italian Localisation - Base',
    'version': '10.0.0.2.15',
    'category': 'Localisation/Italy',
    'description': """(en)
Italian Localization module - Base version

Italian Localization - Base version
-----------------------------------

 Funcionalities:

- Italian cities
- Titles
- Provinces (districts) and Regions

(it)
Localizzazione italiana - Versione base
---------------------------------------

Funzionalità

- Comuni italiani (aggiornati al 2008)
- Titoli
- Province e regioni
- Automatistmi su res.partner.address
""",
    'author': "Odoo Italian Community,Odoo Community Association (OCA),"
              "SHS-AV s.r.l.",
    'maintainer': 'Antonio Maria Vigliotti',
    'website': 'https://odoo-italia.org/',
    'license': 'LGPL-3',
    "depends": ['base', 'sale'],
    "data": [
        'security/ir.model.access.csv',
        # 'views/res_config_view.xml',
        'views/res_partner_view.xml',
        'views/city_view.xml',
        # 'data/res.country.state.csv',
        'data/res.city.csv',
    ],
    'installable': True
}
