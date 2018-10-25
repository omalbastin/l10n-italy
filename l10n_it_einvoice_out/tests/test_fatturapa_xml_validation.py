# -*- coding: utf-8 -*-
#
# Copyright 2014    Davide Corio <davide.corio@lsweb.it>
# Copyright 2015    Lorenzo Battistini <lorenzo.battistini@agilebg.com>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#

import base64
import os
import shutil
import tempfile
from datetime import datetime

from lxml import etree

import openerp.release as release
import openerp.tests.common as test_common
from openerp import workflow
from openerp.modules.module import get_module_resource


class TestFatturaPAXMLValidation(test_common.SingleTransactionCase):

    def env612(self, model):
        """Return model pool"""
        if int(release.major_version.split('.')[0]) < 8:
            return self.registry(model)
        return self.env[model]

    def ref612(self, model):
        """Return reference id"""
        if int(release.major_version.split('.')[0]) < 8:
            return self.ref(model)
        return self.env.ref(model).id

    def search612(self, model, *args):
        """Search record ids - Syntax search(model, *args)
        Warning! On Odoo 7.0 result may fail!"""
        return self.registry(model).search(self.cr, self.uid, *args)

    def browse612(self, model, id):
        return self.registry(model).browse(self.cr, self.uid, id)

    def write612(self, model, id, values):
        """Write existent record [7.0]"""
        if int(release.major_version.split('.')[0]) < 8:
            return self.registry(model).write(self.cr, self.uid, [id], values)
        return self.env[model].search([('id', '=', id)]).write(values)

    def write_ref(self, xid, values):
        """Browse and write existent record"""
        return self.browse_ref(xid).write(values)

    def create612(self, model, values):
        """Create a new record for test"""
        if int(release.major_version.split('.')[0]) < 8:
            return self.env612(model).create(self.cr,
                                             self.uid,
                                             values)
        return self.env612(model).create(values).id

    def workflow612(self, model, action, id):
        if int(release.major_version.split('.')[0]) < 8:
            wf_service = netsvc.LocalService("workflow")
            wf_service.trg_validate(
                self.uid, model, id, action, self.cr
            )
        else:
            workflow.trg_validate(
                self.uid, model, id, action, self.cr
            )

    def getFilePath(self, filepath):
        with open(filepath) as test_data:
            with tempfile.TemporaryFile() as out:
                base64.encode(test_data, out)
                out.seek(0)
                return filepath, out.read()

    def getAttacment(self, name):
        path = get_module_resource(
            'l10n_it_einvoice_out',
            'tests', 'data', 'attach_base.pdf'
        )
        currDir = os.path.dirname(path)
        new_file = '%s/%s' % (currDir, name)
        shutil.copyfile(path, new_file)
        return self.getFilePath(new_file)

    def getFile(self, filename):
        path = get_module_resource(
            'l10n_it_einvoice_out', 'tests', 'data', filename)
        return self.getFilePath(path)

    def setUp(self):
        super(TestFatturaPAXMLValidation, self).setUp()
        self.wizard_model = self.registry('wizard.export.fatturapa')
        self.data_model = self.registry('ir.model.data')
        self.attach_model = self.registry('fatturapa.attachment.out')
        self.invoice_model = self.registry('account.invoice')
        self.company_model = self.registry('res.company')
        self.fatturapa_attach = self.registry('fatturapa.attachments')
        self.context = {}
        self.maxDiff = None
        self.company = self.env.ref('base.main_company')
        self.company.sp_account_id = self.env.ref('account.ova')
        self.company.sp_journal_id = self.env.ref(
            'account.miscellaneous_journal')
        self.company.email = 'info@yourcompany.com'

    def attachFileToInvoice(self, InvoiceId, filename):
        self.fatturapa_attach.create(
            self.cr, self.uid,
            {
                'name': filename,
                'invoice_id': InvoiceId,
                'datas': self.getAttacment(filename)[1],
                'datas_fname': filename
            }
        )

    def checkCreateFiscalYear(self, date_to_check):
        '''
        with this method you can check if a date
        passed in param date_to_check , is in
        current fiscal year .
        If not present, it creates a fiscal year and
        a sequence for sale_journal,
        consistent with date, in date_to_check.
        '''
        cr, uid = self.cr, self.uid
        self.fy_model = self.registry('account.fiscalyear')
        if not self.fy_model.find(
            cr, uid, dt=date_to_check, exception=False
        ):
            ds = datetime.strptime(date_to_check, '%Y-%m-%d')
            seq_id = self.data_model.get_object_reference(
                cr, uid, 'account', 'sequence_sale_journal')
            year = ds.date().year
            name = '%s' % year
            code = 'FY%s' % year
            start = '%s-01-01' % year
            stop = '%s-12-31' % year
            fy_id = self.fy_model.create(
                cr, uid,
                {
                    'name': name,
                    'code': code,
                    'date_start': start,
                    'date_stop': stop
                }
            )
            self.fy_model.create_period(cr, uid, [fy_id])
            self.fiscalyear_id = fy_id
            seq_name = 'seq%s' % name
            self.context['fiscalyear_id'] = self.fiscalyear_id
            prefix = 'SAJ/%s/' % year
            s_id = self.registry('ir.sequence').create(
                cr, uid,
                {
                    'name': seq_name,
                    'padding': 3,
                    'prefix': prefix
                }
            )
            self.context['sequence_id'] = s_id
            self.registry('account.sequence.fiscalyear').create(
                cr, uid,
                {
                    "sequence_id": s_id,
                    'sequence_main_id': seq_id[1],
                    "fiscalyear_id": self.fiscalyear_id
                },
                context=self.context
            )

    def set_sequences(self, file_number, invoice_number):
        cr, uid = self.cr, self.uid
        seq_pool = self.registry('ir.sequence')
        seq_id = self.data_model.get_object_reference(
            cr, uid, 'l10n_it_einvoice_base', 'seq_fatturapa')
        seq_pool.write(cr, uid, [seq_id[1]], {
            'implementation': 'no_gap',
            'number_next_actual': file_number,
            }
        )
        if self.context.get('fiscalyear_id'):
            seq_id = (0, self.context.get('sequence_id'))
        else:
            seq_id = self.data_model.get_object_reference(
                cr, uid, 'account', 'sequence_sale_journal')
        seq_pool.write(
            cr, uid, [seq_id[1]],
            {
                'implementation': 'no_gap',
                'number_next_actual': invoice_number,
            },
            context=self.context
        )

    def confirm_invoice(self, invoice_xml_id, attach=False):
        cr, uid = self.cr, self.uid

        invoice_id = self.data_model.get_object_reference(
            cr, uid, 'l10n_it_einvoice_base', invoice_xml_id)
        if invoice_id:
            invoice_id = invoice_id and invoice_id[1] or False
        # this  write updates context with
        # fiscalyear_id
        if attach:
            self.attachFileToInvoice(invoice_id, 'test1.pdf')
            self.attachFileToInvoice(invoice_id, 'test2.pdf')
        self.invoice_model.write(
            cr, uid, invoice_id, {}, context=self.context)
        self.workflow612('account.invoice', 'invoice_open', invoice_id)

    def run_wizard(self, invoice_id):
        cr, uid = self.cr, self.uid
        wizard_id = self.wizard_model.create(cr, uid, {})
        return self.wizard_model.exportFatturaPA(
            cr, uid, wizard_id, context={'active_ids': [invoice_id]})

    def check_content(self, xml_content, file_name):
        parser = etree.XMLParser(remove_blank_text=True)
        test_fatt_data = self.getFile(file_name)[1]
        test_fatt_content = test_fatt_data.decode('base64')
        test_fatt = etree.fromstring(test_fatt_content, parser)
        xml = etree.fromstring(xml_content, parser)
        # fd = open('/opt/odoo/tmp/tmp_test_fatt.log', 'w')       # debug
        # fd.write(etree.tostring(test_fatt))                     # debug
        # fd.close()                                              # debug
        # fd = open('/opt/odoo/tmp/tmp_test_xml.log', 'w')        # debug
        # fd.write(etree.tostring(xml))                           # debug
        # fd.close()                                              # debug
        self.assertEqual(etree.tostring(test_fatt), etree.tostring(xml))

    def test_0_xml_export(self):
        cr, uid = self.cr, self.uid
        self.checkCreateFiscalYear('2018-01-07')
        # self.context['fiscalyear_id'] = self.fiscalyear_id
        self.set_sequences(1, 13)
        invoice_id = self.confirm_invoice('fatturapa_invoice_0')
        res = self.run_wizard(invoice_id)

        self.assertTrue(res, 'Export failed.')
        attachment = self.attach_model.browse(cr, uid, res['res_id'])
        self.assertEqual(attachment.datas_fname, 'IT06363391001_00001.xml')

        # XML doc to be validated
        xml_content = attachment.datas.decode('base64')
        self.check_content(xml_content, 'IT06363391001_00001.xml')

    def test_1_xml_export(self):
        cr, uid = self.cr, self.uid
        self.checkCreateFiscalYear('2018-06-15')
        self.set_sequences(2, 14)
        invoice_id = self.confirm_invoice('fatturapa_invoice_1')
        res = self.run_wizard(invoice_id)
        attachment = self.attach_model.browse(cr, uid, res['res_id'])
        xml_content = attachment.datas.decode('base64')
        self.check_content(xml_content, 'IT06363391001_00002.xml')

    def test_2_xml_export(self):
        cr, uid = self.cr, self.uid
        self.checkCreateFiscalYear('2018-06-15')
        self.set_sequences(3, 15)
        invoice_id = self.confirm_invoice('fatturapa_invoice_2', attach=True)
        res = self.run_wizard(invoice_id)
        attachment = self.attach_model.browse(cr, uid, res['res_id'])
        xml_content = attachment.datas.decode('base64')
        self.check_content(xml_content, 'IT06363391001_00003.xml')

    def test_3_xml_export(self):
        cr, uid = self.cr, self.uid
        self.checkCreateFiscalYear('2018-06-15')
        self.set_sequences(4, 16)
        invoice_id = self.confirm_invoice('fatturapa_invoice_3')
        res = self.run_wizard(invoice_id)
        attachment = self.attach_model.browse(cr, uid, res['res_id'])
        xml_content = attachment.datas.decode('base64')
        self.check_content(xml_content, 'IT06363391001_00004.xml')

    def test_4_xml_export(self):
        cr, uid = self.cr, self.uid
        self.checkCreateFiscalYear('2018-06-15')
        self.set_sequences(5, 17)
        invoice_id = self.confirm_invoice('fatturapa_invoice_4')
        res = self.run_wizard(invoice_id)
        attachment = self.attach_model.browse(cr, uid, res['res_id'])
        xml_content = attachment.datas.decode('base64')
        self.check_content(xml_content, 'IT06363391001_00005.xml')
