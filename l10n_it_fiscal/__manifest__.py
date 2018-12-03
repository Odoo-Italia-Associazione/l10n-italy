# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) SHS-AV s.r.l. (<http://www.zeroincombenze.it>)
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Italy - Fiscal localization by zeroincombenze(R)',
    'version': '10.0.0.2.0',
    'depends': ['base_vat', 'base_iban'],
    'author': 'SHS-AV s.r.l.',
    'description': """
Italian fiscal and legal localization
=====================================


(en) Chart of Account and Tax codes
-----------------------------------
Very detailed Chart of Account, available to any Italian Company.
Tree structure may be expanded by end-user, adding new records.

Code has 6 digits; users should not add codes ending with '0'.

Tax codes cover most of variety italian fiscal cases:

- Ordinary regime
- Simplified regime
- Cash VAT
- Subjects without VAT


(it) Piano dei conti e Codici IVA
---------------------------------
Piano dei conti molto dettagliato utilizzabile da qualsiasi impresa italiana.
La struttura può  essere ulteriormente espansa dall'utente finale
con l'inserimento di nuovi record.

La codifica è di 6 cifre;
l'utente finale non dovrebbe inserire codici terminanti con '0'.


I codici IVA coprono una grande varietà di casistiche fiscali:

- Regime Ordinario
- Regime semplificato (contribuenti minimi L.244/07)
- Regime IVA per cassa (L.185/08 e art.6 DPR633/72)
- Operazioni senza IVA (L.98/11)


See http://www.zeroincombenze.it/il-piano-dei-conti-2/
    """,
    'category': 'Localization/Account Charts',
    'data': [
        'data/l10n_it_chart_data.xml',
        'data/account.account.template.csv',
        'data/account.tax.template.csv',
        'data/account.fiscal.position.template.csv',
        'data/account.chart.template.csv',
        'data/account_chart_template_data.yml',
    ],
    'maintainer': 'Antonio Maria Vigliotti',
    'license': 'AGPL-3',
    'website': 'http://www.zeroincombenze.it',
    'installable': True,
}
