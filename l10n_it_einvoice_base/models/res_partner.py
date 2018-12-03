# -*- coding: utf-8 -*-
# Copyright 2014    - Davide Corio <davide.corio@abstract.it>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from odoo import fields, models


class AccountFiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'

    regime_fiscale = fields.Many2one(
        'fatturapa.fiscal_position', string='Tax Regime')


class ResPartner(models.Model):
    _inherit = "res.partner"

    # 1.2.6 RiferimentoAmministrazione
    pa_partner_code = fields.Char('PA partner reference', size=20)
    # 1.2.1.4
    register = fields.Char('Professional Register', size=60)
    # 1.2.1.5
    register_province = fields.Many2one(
        'res.country.state', string='Register Province')
    # 1.2.1.6
    register_code = fields.Char('Register Code', size=60)
    # 1.2.1.7
    register_regdate = fields.Date('Register Registration Date')
    # 1.2.1.8
    register_fiscalpos = fields.Many2one(
        'fatturapa.fiscal_position',
        string="Register Fiscal Position")
    # 1.1.6
    pec_destinatario = fields.Char(
        "PEC destinatario",
        help="Indirizzo PEC al quale inviare la fattura elettronica. "
             "Da valorizzare "
             "SOLO nei casi in cui l'elemento informativo "
             "<CodiceDestinatario> vale '0000000'"
    )
