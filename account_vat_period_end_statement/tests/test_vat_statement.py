# -*- coding: utf-8 -*-
#
#    Copyright (C) 2015 Agile Business Group <http://www.agilebg.com>
#    About License, see __openerp__.py
#

from openerp.tests.common import TransactionCase


UT_DEBIT_AMT_PRICE = 100
UT_DEBIT_AMT_QTY = 10
UT_DEBIT_AMT_TAXABLE = 1000
UT_DEBIT_AMT_VAT = 220
UT_CREDIT_AMT_PRICE = 60
UT_CREDIT_AMT_QTY = 10
UT_CREDIT_AMT_TAXABLE = 600
UT_CREDIT_AMT_VAT = 132
UT_VAT_TO_PAY = 88
UT_FISCALCODE = 'VGLNTN59H26B963V'


class TestTax(TransactionCase):

    def setUp(self):
        super(TestTax, self).setUp()
        self.tax_model = self.env['account.tax']
        self.tax_code_model = self.env['account.tax.code']
        self.account_model = self.env['account.account']
        self.term_model = self.env['account.payment.term']
        self.term_line_model = self.env['account.payment.term.line']
        self.invoice_model = self.env['account.invoice']
        self.invoice_line_model = self.env['account.invoice.line']
        self.period_model = self.env['account.period']
        self.vat_statement_model = self.env['account.vat.period.end.statement']

        self.company_id = self.env.ref('base.main_company').id

        # ----- Set invoice date to recent date in the system
        # ----- This solves problems with account_invoice_sequential_dates
        self.recent_date = self.invoice_model.search(
            [('date_invoice', '!=', False)], order='date_invoice desc',
            limit=1).date_invoice
        self.current_period = self.period_model.find(dt=self.recent_date)

        self.account_tax_code_22 = self.tax_code_model.create({
            'name': '22%',
            'vat_statement_type': 'debit',
            'vat_statement_sign': 1,
            'vat_statement_account_id': self.env.ref('account.ova').id,
            })
        self.account_tax_code_22_imp = self.tax_code_model.create({
            'name': '22% IMP',
            })
        self.account_tax_code_22_credit = self.tax_code_model.create({
            'name': '22% credit',
            'vat_statement_type': 'credit',
            'vat_statement_sign': -1,
            'vat_statement_account_id': self.env.ref('account.iva').id,
            })
        self.account_tax_code_22_imp_credit = self.tax_code_model.create({
            'name': '22% IMP credit',
            })

        self.account_tax_22 = self.tax_model.create({
            'name': '22%',
            'amount': 0.22,
            'tax_code_id': self.account_tax_code_22.id,
            'base_code_id': self.account_tax_code_22_imp.id,
            'base_sign': 1,
            'tax_sign': 1,
            })
        self.account_tax_22_credit = self.tax_model.create({
            'name': '22% credit',
            'amount': 0.22,
            'tax_code_id': self.account_tax_code_22_credit.id,
            'base_code_id': self.account_tax_code_22_imp_credit.id,
            'base_sign': -1,
            'tax_sign': -1,
            })

        self.vat_authority = self.account_model.create({
            'code': 'VAT AUTH',
            'name': 'VAT Authority',
            'parent_id': self.env.ref('account.cli').id,
            'type': 'payable',
            'reconcile': True,
            'user_type': self.env.ref('account.data_account_type_payable').id,
            })

        self.account_payment_term = self.term_model.create({
            'name': '16 Days End of Month',
            'note': '16 Days End of Month',
            })
        self.term_line_model.create({
            'value': 'balance',
            'days': 16,
            'days2': -1,
            'payment_id': self.account_payment_term.id,
            })

    def test_vat_statement(self):
        out_invoice = self.invoice_model.create({
            'date_invoice': self.recent_date,
            'account_id': self.env.ref('account.a_recv').id,
            'journal_id': self.env.ref('account.sales_journal').id,
            'partner_id': self.env.ref('base.res_partner_3').id,
            'type': 'out_invoice',
            })
        self.invoice_line_model.create({
            'invoice_id': out_invoice.id,
            'account_id': self.env.ref('account.a_sale').id,
            'name': 'service',
            'price_unit': UT_DEBIT_AMT_PRICE,
            'quantity': UT_DEBIT_AMT_QTY,
            'invoice_line_tax_id': [(6, 0, [self.account_tax_22.id])],
            })
        out_invoice.signal_workflow('invoice_open')

        in_invoice = self.invoice_model.create({
            'date_invoice': self.recent_date,
            'account_id': self.env.ref('account.a_pay').id,
            'journal_id': self.env.ref('account.expenses_journal').id,
            'partner_id': self.env.ref('base.res_partner_4').id,
            'type': 'in_invoice',
            })
        self.invoice_line_model.create({
            'invoice_id': in_invoice.id,
            'account_id': self.env.ref('account.a_expense').id,
            'name': 'service',
            'price_unit': UT_CREDIT_AMT_PRICE,
            'quantity': UT_CREDIT_AMT_QTY,
            'invoice_line_tax_id': [(6, 0, [self.account_tax_22_credit.id])],
            })
        in_invoice.signal_workflow('invoice_open')

        self.vat_statement = self.vat_statement_model.create({
            'journal_id': self.env.ref('account.miscellaneous_journal').id,
            'authority_vat_account_id': self.vat_authority.id,
            'payment_term_id': self.account_payment_term.id,
            'soggetto_codice_fiscale': UT_FISCALCODE
            })
        self.current_period.vat_statement_id = self.vat_statement
        self.vat_statement.compute_amounts()
        # Test must ignore invoice records written by other unit tests
        debit_line = False
        for line in self.vat_statement.debit_vat_account_line_ids:
            if line.tax_code_id.id == self.account_tax_code_22.id:
                debit_line = line
                break
        credit_line = False
        for line in self.vat_statement.credit_vat_account_line_ids:
            if line.tax_code_id.id == self.account_tax_code_22_credit.id:
                credit_line = line
                break
        self.assertTrue(debit_line)
        self.assertTrue(credit_line)
        self.assertEqual(debit_line.amount, UT_DEBIT_AMT_VAT)
        self.assertEqual(credit_line.amount, UT_CREDIT_AMT_VAT)
        # self.assertEqual(debit_line.base_amount, UT_DEBIT_AMT_TAXABLE)
        # self.assertEqual(credit_line.base_amount, UT_CREDIT_AMT_TAXABLE)
        self.assertEqual(self.vat_statement.authority_vat_amount,
                         UT_VAT_TO_PAY)
        self.assertEqual(self.vat_statement.deductible_vat_amount,
                         UT_CREDIT_AMT_VAT)
        self.assertEqual(self.vat_statement.payable_vat_amount,
                         UT_DEBIT_AMT_VAT)
        self.assertEqual(self.vat_statement.residual, 0)
        self.vat_statement.signal_workflow('create_move')
        self.assertEqual(self.vat_statement.state, 'confirmed')
        self.assertTrue(self.vat_statement.move_id)
        # TODO payment
