# -*- coding: utf-8 -*-
# Copyright 2015  Davide Corio <davide.corio@abstract.it>
# Copyright 2015-2016  Lorenzo Battistini - Agile Business Group
# Copyright 2016  Alessio Gerace - Agile Business Group
# Copyright 2018  Antonio M. Vigliotti - SHS-AV s.r.l.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from odoo.addons.account.tests.account_test_users import AccountTestUsers
from odoo.tools.translate import _


class TestSP(AccountTestUsers):

    def setUp(self):
        super(TestSP, self).setUp()
        self.tax_model = self.env['account.tax']
        self.invoice_model = self.env['account.invoice']
        self.term_model = self.env['account.payment.term']
        self.inv_line_model = self.env['account.invoice.line']
        self.fp_model = self.env['account.fiscal.position']
        self.company = self.env.ref('base.main_company')
        self.company.sp_account_id = self.env['account.account'].search([
            (
                'user_type_id', '=',
                self.env.ref('account.data_account_type_current_assets').id
            )
        ], limit=1)
        self.tax22 = self.tax_model.create({
            'name': '22%',
            'amount': 22,
            'account_id': self.company.sp_account_id.id,
            'refund_account_id': self.company.sp_account_id.id
            })
        self.sp_fp = self.fp_model.create({
            'name': 'Split payment',
            'split_payment': True,
            })
        self.company.sp_tax_id = self.tax22
        account_user_type = self.env.ref(
            'account.data_account_type_receivable')
        self.a_recv = self.account_model.sudo(self.account_manager.id).create(
            dict(
                code="cust_acc",
                name="customer account",
                user_type_id=account_user_type.id,
                reconcile=True,
            ))
        self.a_sale = self.env['account.account'].search([
            (
                'user_type_id', '=',
                self.env.ref('account.data_account_type_revenue').id)
        ], limit=1)
        self.sales_journal = self.env['account.journal'].search(
            [('type', '=', 'sale')])[0]
        self.sales_journal.update_posted = True
        self.term_15_30 = self.term_model.create({
            'name': '15 30',
            'line_ids': [
                (0, 0, {
                    'value': 'percent',
                    'value_amount': 50,
                    'days': 15,
                    'sequence': 1,
                }),
                (0, 0, {
                    'value': 'balance',
                    'days': 30,
                    'sequence': 2,
                })]})
        # Set invoice date to recent date in the system
        # This solves problems with account_invoice_sequential_dates
        self.recent_date = self.invoice_model.search(
            [('date_invoice', '!=', False)], order='date_invoice desc',
            limit=1).date_invoice

    def test_invoice(self):
        invoice = self.invoice_model.create({
            'date_invoice': self.recent_date,
            'partner_id': self.env.ref('base.res_partner_3').id,
            'journal_id': self.sales_journal.id,
            'account_id': self.a_recv.id,
            'fiscal_position_id': self.sp_fp.id,
            'invoice_line_ids': [(0, 0, {
                'name': 'service',
                'account_id': self.a_sale.id,
                'quantity': 1,
                'price_unit': 100,
                'invoice_line_tax_ids': [(6, 0, {
                    self.tax22.id
                    })]
                })]
            })
        self.assertTrue(invoice.split_payment)
        invoice.action_invoice_open()
        self.assertEqual(invoice.amount_sp, -22)
        self.assertEqual(invoice.amount_total, 122)
        self.assertEqual(invoice.residual, 100)
        self.assertEqual(invoice.amount_tax, 22)
        test_res = {
            self.a_recv.id: {'debit': 122, 'credit': 22},
            self.company.sp_account_id.id: {'debit': 22, 'credit': 22},
        }
        for line in invoice.move_id.line_ids:
            if line.account_id.id in test_res:
                if line.debit == test_res[line.account_id.id]['debit']:
                    test_res[line.account_id.id]['debit'] = -1
                elif line.credit == test_res[line.account_id.id]['credit']:
                    test_res[line.account_id.id]['credit'] = -1
                else:
                    raise AssertionError('Invalid invoice line!')
        for id in test_res:
            if test_res[id]['debit'] != -1:
                raise AssertionError('Debit invoice line not found!')
            elif test_res[id]['credit'] != -1:
                raise AssertionError('Credit invoice line not found!')
        # invoice.action_cancel()

        invoice2 = self.invoice_model.create({
            'partner_id': self.env.ref('base.res_partner_3').id,
            'journal_id': self.sales_journal.id,
            'account_id': self.a_recv.id,
            'fiscal_position_id': self.sp_fp.id,
            'payment_term_id': self.term_15_30.id,
            'invoice_line_ids': [(0, 0, {
                'name': 'service',
                'account_id': self.a_sale.id,
                'quantity': 1,
                'price_unit': 100,
                'invoice_line_tax_ids': [(6, 0, {
                    self.tax22.id
                    })]
                })]
            })
        invoice2.action_invoice_open()
        self.assertEqual(invoice2.amount_sp, -22)
        self.assertEqual(invoice2.amount_total, 122)
        self.assertEqual(invoice2.residual, 100)
        self.assertEqual(invoice2.amount_tax, 22)
        vat_line_count = 0
        credit_line_count = 0
        for line in invoice2.move_id.line_ids:
            if line.account_id.id == self.company.sp_account_id.id:
                vat_line_count += 1
                if line.debit:
                    self.assertEqual(line.debit, 22)
                else:
                    self.assertEqual(line.credit, 22)
            if line.account_id.id == self.a_recv.id:
                credit_line_count += 1
                if line.name == _('Split Payment Write Off'):
                    self.assertEqual(line.credit, 22)
                elif line.name == 'Importo + IVA split-payment':
                    self.assertEqual(line.debit, 72)
                else:
                    self.assertEqual(line.debit, 50)
        self.assertEqual(vat_line_count, 2)
        self.assertEqual(credit_line_count, 3)

        # refund
        invoice3 = self.invoice_model.create({
            'date_invoice': self.recent_date,
            'partner_id': self.env.ref('base.res_partner_3').id,
            'journal_id': self.sales_journal.id,
            'account_id': self.a_recv.id,
            'fiscal_position_id': self.sp_fp.id,
            'type': 'out_refund',
            'invoice_line_ids': [(0, 0, {
                'name': 'service',
                'account_id': self.a_sale.id,
                'quantity': 1,
                'price_unit': 100,
                'invoice_line_tax_ids': [(6, 0, {
                    self.tax22.id
                    })]
                })]
        })
        self.assertTrue(invoice3.split_payment)
        invoice3.action_invoice_open()
        self.assertEqual(invoice3.amount_sp, -22)
        self.assertEqual(invoice3.amount_total, 122)
        self.assertEqual(invoice3.residual, 100)
        self.assertEqual(invoice3.amount_tax, 22)
        test_res = {
            self.a_recv.id: {'debit': 22, 'credit': 122},
            self.company.sp_account_id.id: {'debit': 22, 'credit': 22},
        }
        for line in invoice3.move_id.line_ids:
            if line.account_id.id in test_res:
                if line.debit == test_res[line.account_id.id]['debit']:
                    test_res[line.account_id.id]['debit'] = -1
                elif line.credit == test_res[line.account_id.id]['credit']:
                    test_res[line.account_id.id]['credit'] = -1
                else:
                    raise AssertionError('Invalid invoice line!')
        # invoice.action_cancel()
