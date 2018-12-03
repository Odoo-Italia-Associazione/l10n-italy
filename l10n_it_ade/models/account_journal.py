# -*- coding: utf-8 -*-
#
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp import api, fields, models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    rev_charge = fields.Boolean(
        'Reverse Charge Journal',
        default=False,
        help="Check if reverse charge EU invoices journal")
    anom_sale_receipts = fields.Boolean(
        'Anonimous sale receipts journal',
        default=False,
        help="Check if this is the Anonimous Sale Receipts Journal")
    proforma = fields.Boolean(
        'Proforma journal',
        default=False,
        help="Check if this is a Proforma Journal")
    einvoice = fields.Boolean(
        'E-Invoice journal',
        default=False,
        help="Check if this is a E-Invoice Journal")

    @api.v8
    def onchange_check_subtype(self, name):
        if name in ('rev_charge', 'anom_sale_receipts') and self[name]:
            if self.type != 'sale':
                return {'value': {name: False},
                        'warning': {
                    'title': 'Invalid setting!',
                    'message': 'Journal type must be sale'}
                }
        elif name in ('proforma', 'einvoice') and self[name]:
            if self.type not in ('purchase', 'sale'):
                return {'value': {name: False},
                        'warning': {
                    'title': 'Invalid setting!',
                    'message': 'Journal type must be sale or purchase'}
                }
        for p in ('rev_charge', 'anom_sale_receipts', 'proforma', 'einvoice'):
            if p != name:
                self[p] = False

    @api.onchange('rev_charge')
    def onchange_rev_charge(self):
        return self.onchange_check_subtype('rev_charge')

    @api.onchange('anom_sale_receipts')
    def onchange_sale_receipts(self):
        return self.onchange_check_subtype('anom_sale_receipts')

    @api.onchange('proforma')
    def onchange_proforma(self):
        return self.onchange_check_subtype('proforma')

    @api.onchange('einvoice')
    def onchange_einvoice(self):
        return self.onchange_check_subtype('einvoice')
