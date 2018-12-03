# -*- coding: utf-8 -*-
#
# Copyright 2014    - KTec S.r.l.
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    ipa_code = fields.Char(string='IPA Code')
    is_pa = fields.Boolean("Public administration")
    # FatturaPa  1.1.4
    codice_destinatario = fields.Char(
        "Recipient Code",
        help="Il codice, di 7 caratteri, assegnato dal Sdi ai soggetti che "
             "hanno accreditato un canale; qualora il destinatario non abbia "
             "accreditato un canale presso Sdi e riceva via PEC le fatture, "
             "l'elemento deve essere valorizzato con tutti zeri ('0000000'). ")
    electronic_invoice_subjected = fields.Boolean(
        "Subjected to electronic invoice")
    eori_code = fields.Char('EORI Code', size=20)
    license_number = fields.Char('License Code', size=20)
    # FatturaPA 1.1.6
    pec_destinatario = fields.Char(
        "PEC destinatario",
        help="Indirizzo PEC al quale inviare la fattura elettronica, "
             "se diversa da PEC legale. Viene utilizzata solo "
             "se il codice destinatario vale '0000000'")

    @api.onchange('electronic_invoice_subjected')
    def onchange_electronic_invoice_subjected(self):
        if self.vat and not self.codice_destinatario:
            self.codice_destinatario = '0000000'

    @api.multi
    @api.constrains(
        'is_pa', 'ipa_code', 'codice_destinatario',
        'electronic_invoice_subjected', 'vat'
    )
    def _check_codice_destinatario(self):
        for partner in self:
            if partner.electronic_invoice_subjected and partner.is_pa:
                raise ValidationError(_(
                    'Partner %s dichiarato sia PA che Fattura B2B!'
                ) % partner.name)
            if partner.is_pa and (
                not partner.ipa_code or len(partner.ipa_code) != 6
            ):
                raise ValidationError(_(
                    'Il partner %s è una PA: '
                    'deve avere il codice IPA di 6 caratteri'
                ) % partner.name)
            if partner.electronic_invoice_subjected:
                if not partner.vat and not partner.fiscalcode:
                    raise ValidationError(_(
                        'Partner %s, soggetto a Fattura Elettronica '
                        'ma senza P.IVA ne codice fiscale'
                    ) % partner.name)
                if (
                    not partner.codice_destinatario or
                    len(partner.codice_destinatario) != 7
                ):
                    raise ValidationError(_(
                        'Partner %s, soggetto a Fattura Elettronica: '
                        'deve avere il codice destinatario di 7 caratteri '
                        'eventualmente valorizzato con 0000000'
                    ) % partner.name)
