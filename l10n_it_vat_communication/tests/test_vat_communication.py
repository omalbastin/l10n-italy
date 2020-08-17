# -*- coding: utf-8 -*-
#    Copyright (C) 2017    SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2017: SHS-AV s.r.l.] First version
#
import openerp.release as release
from openerp.tests.common import TransactionCase
# from openerp import netsvc


COMPANY_IT_VAT = 'IT12345670017'
UT_FISCALCODE = 'VGLNTN59H26B963V'
UT_CODICE_CARICA = '1'


class TestCommunication(TransactionCase):
    def env789(self, model):
        """Return model pool"""
        if release.major_version in ('6.1', '7.0'):
            # Return model pool [6.1 / 7.0]
            return self.registry(model)
        # Return model pool [+8.0]
        return self.env[model]

    def ref789(self, model):
        """Return reference id"""
        if release.major_version in ('6.1', '7.0'):
            # Return reference id [6.1 / 7.0]
            return self.ref(model)
        # Return reference id [+8.0]
        return self.env.ref(model).id

    def search789(self,  *args, **kwargs):
        """Search record ids - Syntax search(model, *args, **kwargs)"""
        if release.major_version in ('6.1', '7.0'):
            # Search record ids [6.1 / 7.0]
            model_pool = self.registry(args[0])
            return model_pool.search(self.cr, self.uid, args[1], kwargs)
        # Search record ids [+8.0]
        model_pool = self.env[args[0]]
        return model_pool.search(args[1], kwargs)._ids

    def write789(self, model, id, values):
        """Write existent record [7.0]"""
        if release.major_version in ('6.1', '7.0'):
            # Write existent record [6.1 / 7.0]
            model_pool = self.registry(model)
            return model_pool.write(self.cr, self.uid, [id], values)
        # Write existent record [+8.0]
        model_pool = self.env[model]
        obj = model_pool.search([('id', '=', id)])
        return obj.write(values)

    def write_ref(self, xid, values):
        """Browse and write existent record"""
        obj = self.browse_ref(xid)
        return obj.write(values)

    def create789(self, model, values):
        """Create a new record for test"""
        if release.major_version in ('6.1', '7.0'):
            # Create a new record for test [6.1 / 7.0]
            return self.env789(model).create(self.cr,
                                             self.uid,
                                             values)
        # Create a new record for test [+8.0]
        model_pool = self.env[model]
        return model_pool.create(values).id

    #
    # Because other modules have created invoices and other data, there is no
    # way to know invoices and amounts in the main company.
    # Create a new company with know data in it.
    #
    def setUp(self):
        super(TestCommunication, self).setUp()
        # cr, uid = self.cr, self.uid

        self.ir_model_data_model = self.env789('ir.model.data')
        self.res_users_model = self.env789('res.users')

    def setup_company(self):
        model = 'res.company'
        self.company_IT_id = self.create789(
            model, {'name': 'My Company S.p.A.',
                    'address': 'Via del Campo, 1',
                    'zip': '15100',
                    'city': 'Alessandria',
                    'vat': COMPANY_IT_VAT,
                    })
        country_IT = self.ref789('base.it')
        # Country state Italy shoul be loaded
        ids = self.search789('res.country.state',
                             [('country_id', '=', country_IT),
                              ('code', '=', 'AL')])
        # but 6,1 use province, so get US Alabama instead of Alessandria
        if not ids:
            ids = self.search789('res.country.state',
                                 [('code', '=', 'AL')])
        state_id_AL = ids[0]
        self.write789(model, self.company_IT_id,
                      {'country_id': country_IT,
                       'state_id': state_id_AL})

    def test_vat_communication(self):
        self.setup_company()
        self.vat_communication_id = self.create789(
            'account.vat.communication',
            {'soggetto_codice_fiscale': UT_FISCALCODE,
             'codice_carica': UT_CODICE_CARICA})
