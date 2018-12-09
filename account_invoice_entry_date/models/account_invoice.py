# -*- coding: utf-8 -*-
#
# Copyright 2004-2010, ISA srl <http://www.isa.it>).
# Copyright 2014-2018, Associazione Odoo Italia <https://odoo-italia.org>
# Copyright 2017-2018, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
import time

from odoo import api, fields, models
from odoo.tools.translate import _
from openerp.exceptions import Warning as UserError


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    registration_date = fields.Date(
        'Registration Date',
        states={
            'paid': [('readonly', True)],
            'open': [('readonly', True)],
            'close': [('readonly', True)]
        },
        index=True,
        help="Keep empty to use the current date",
        copy=False)

    @api.multi
    def action_set_registration_date(self):
        for inv in self:
            date_invoice = inv.date_invoice
            reg_date = inv.registration_date
            if inv.type in ('in_invoice', 'in_refund'):
                if not inv.registration_date:
                    if not inv.date_invoice:
                        reg_date = time.strftime('%Y-%m-%d')
                    else:
                        reg_date = inv.date_invoice
                if date_invoice and reg_date and date_invoice > reg_date:
                    raise UserError(
                        _("The invoice date cannot be later than"
                          " the date of registration!"))     # pragma: no cover
            elif inv.type in ('out_invoice', 'out_refund'):
                reg_date = inv.date_invoice
            invoice_values = {'registration_date': reg_date}
            if reg_date != inv.registration_date:
                inv.write(invoice_values)

    @api.multi
    def action_move_create(self):
        self.action_set_registration_date()
        return super(AccountInvoice, self).action_move_create()

    @api.multi
    def action_invoice_open(self):
        self.action_set_registration_date()
        return super(AccountInvoice, self).action_invoice_open()
