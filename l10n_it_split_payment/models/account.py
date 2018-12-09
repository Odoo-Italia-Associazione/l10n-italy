# -*- coding: utf-8 -*-
# Copyright 2015  Davide Corio <davide.corio@abstract.it>
# Copyright 2015-2016  Lorenzo Battistini - Agile Business Group
# Copyright 2016  Alessio Gerace - Agile Business Group
# Copyright 2018  Antonio M. Vigliotti - SHS-AV s.r.l.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import odoo.addons.decimal_precision as dp
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class AccountFiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'

    split_payment = fields.Boolean('Split Payment')

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    amount_sp = fields.Float(
        string='Split Payment',
        digits=dp.get_precision('Account'),
        store=True,
        readonly=True,
        compute='_compute_amount')
    split_payment = fields.Boolean(
        'Split Payment',
        related='fiscal_position_id.split_payment')

    @api.one
    @api.depends(
        'invoice_line_ids.price_subtotal', 'tax_line_ids.amount',
        'currency_id', 'company_id', 'date_invoice'
    )
    def _compute_amount(self):
        super(AccountInvoice, self)._compute_amount()
        self.amount_sp = 0
        if self.fiscal_position_id.split_payment:
            self.amount_sp = - self.amount_tax
            # self.amount_tax = 0
            self.amount_net_pay = self.amount_total + self.amount_sp
        # self.amount_total = self.amount_untaxed + self.amount_tax

    def reconcile_sp_invoice(self, invoice):
        reconcile_model = self.env['account.move.line.reconcile']
        # move_line_model = self.env['account.move.line']
        ids = invoice.get_receivable_line_ids()
        reconcile_model.with_context(
            active_ids=ids).trans_rec_reconcile_full()

    def _build_debit_line(self):
        if not self.company_id.sp_account_id:
            raise UserError(
                _("Please set 'Split Payment Write-off Account' field in"
                  " accounting configuration"))
        if not self.company_id.sp_tax_id:
            raise UserError(
                _("Please set 'Split Payment Write-off Tax' field in"
                  " accounting configuration"))
        vals = {
            'name': _('Split Payment Write Off'),
            'partner_id': self.partner_id.id,
            'account_id': self.company_id.sp_account_id.id,
            'journal_id': self.journal_id.id,
            'date': self.date_invoice,
            'date_maturity': self.date_invoice,
            'debit': abs(self.amount_sp),
            'credit': 0,
            'tax_line_id': self.company_id.sp_tax_id.id,
            }
        if self.type == 'out_refund':
            vals['debit'] = 0
            vals['credit'] = abs(self.amount_sp)
        return vals

    def _build_credit_line(self, invoice):
        move_line_pool = self.env['account.move.line']
        ids = invoice.get_receivable_line_ids()
        if ids:
            account_id = move_line_pool.browse(ids[0]).account_id
        else:
            account_id = self.company_id.sp_account_id
        vals = {
            'name': _('Split Payment Write Off'),
            'partner_id': self.partner_id.id,
            'account_id': account_id.id,
            'journal_id': self.journal_id.id,
            'date': self.date_invoice,
            'date_maturity': self.date_invoice,
            'credit': abs(self.amount_sp),
            'debit': 0,
            'tax_line_id': self.company_id.sp_tax_id.id,
            }
        if self.type == 'out_refund':
            vals['credit'] = 0
            vals['debit'] = abs(self.amount_sp)
        return vals

    @api.multi
    def get_receivable_line_ids(self):
        # return the move line ids with the same account as the invoice self
        if not self.id:
            return []
        query = (
            "SELECT l.id "
            "FROM account_move_line l, account_invoice i "
            "WHERE i.id = %s AND l.move_id = i.move_id "
            "AND l.account_id = i.account_id order by date_maturity"
        )
        self._cr.execute(query, (self.id,))
        return [row[0] for row in self._cr.fetchall()]

    @api.multi
    def get_vat_spl_line_ids(self):
        # return the move line ids with the split payment 
        if not self.id:
            return []
        query = ("""select id,name from account_move_line
                where invoice_id=%d and tax_line_id in
                (select x.tax_dest_id
                from account_fiscal_position f, account_fiscal_position_tax x
                where x.position_id = f.id and f.split_payment = true);""" %
                self.id)
        self._cr.execute(query, (self.id,))
        return [row[0] for row in self._cr.fetchall()]

    @api.multi
    def _compute_split_payments(self):

        def _revaluate_amount(receivable_line, db_cr, vat_assigned):
            receivable_line_amount = receivable_line[db_cr] - (
                invoice.amount_tax * 
                receivable_line[db_cr] /
                invoice.amount_total)
            if not vat_assigned:
                receivable_line_amount += invoice.amount_tax
            diff = receivable_line[db_cr] - receivable_line_amount
            vals = {db_cr: receivable_line_amount}
            if not vat_assigned:
                vals['name'] = _('Importo + IVA split-payment')
            receivable_line.with_context(
                check_move_validity=False
            ).write(vals)
            return diff

        for invoice in self:
            receivable_line_ids = invoice.get_receivable_line_ids()
            move_line_pool = self.env['account.move.line']
            vat_assigned = False
            diff = 0.0
            for receivable_line in move_line_pool.browse(receivable_line_ids):
                if invoice.type == 'out_invoice' and receivable_line.debit:
                    diff += _revaluate_amount(receivable_line,
                                              'debit',
                                              vat_assigned)
                elif invoice.type == 'out_refund' and receivable_line.credit:
                    diff += _revaluate_amount(receivable_line,
                                              'credit',
                                              vat_assigned)
                vat_assigned = True
            if diff:
                receivable_line = move_line_pool.browse(receivable_line_ids[0])
                if invoice.type == 'out_invoice' and receivable_line.debit:
                    vals = {'debit': receivable_line.debit + diff}
                elif invoice.type == 'out_refund' and receivable_line.credit:
                    vals = {'credit': receivable_line.credit + diff}
                receivable_line.with_context(
                    check_move_validity=False
                ).write(vals)

    @api.multi
    def action_move_create(self):
        res = super(AccountInvoice, self).action_move_create()
        for invoice in self:
            if (
                invoice.fiscal_position_id and
                invoice.fiscal_position_id.split_payment
            ):
                if invoice.type in ['in_invoice', 'in_refund']:
                    raise UserError(
                        _("Can't handle supplier invoices with split payment"))
                if invoice.move_id.state == 'posted':
                    posted = True
                    invoice.move_id.state = 'draft'
                self._compute_split_payments()
                line_model = self.env['account.move.line']
                write_off_line_vals = invoice._build_debit_line()
                write_off_line_vals['move_id'] = invoice.move_id.id
                line_model.with_context(
                    check_move_validity=False
                ).create(write_off_line_vals)
                write_off_line_vals = invoice._build_credit_line(invoice)
                write_off_line_vals['move_id'] = invoice.move_id.id
                line_model.with_context(
                    check_move_validity=False
                ).create(write_off_line_vals)
                if posted:
                    invoice.move_id.state = 'posted'
                self.reconcile_sp_invoice(invoice)
        return res
