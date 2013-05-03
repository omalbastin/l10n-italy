# -*- encoding: utf-8 -*-
##############################################################################
#    
#    Copyright (C) 2011 Associazione OpenERP Italia
#    (<http://www.openerp-italia.org>). 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields,osv
from tools.translate import _
import time

class wizard_registro_iva(osv.osv_memory):

    def _get_period(self, cr, uid, context=None):
        ctx = dict(context or {}, account_period_prefer_normal=True)
        period_ids = self.pool.get('account.period').find(cr, uid, context=ctx)
        return period_ids[0]

    _name = "wizard.registro.iva"
    _columns = {
        'period_id': fields.many2one('account.period','Period', required=True),
        'type': fields.selection([
            ('customer', 'Customer Invoices'),
            ('supplier', 'Supplier Invoices'),
            ('corrispettivi', 'Corrispettivi'),
            ], 'Layout', required=True),
        'journal_ids': fields.many2many('account.journal', 'registro_iva_journals_rel', 'journal_id', 'registro_id', 'Journals', help='Select journals you want retrieve documents from', required=True),
        'message': fields.char('Message', size=64, readonly=True),
        }
    _defaults = {
        'type': 'customer',
        'period_id': _get_period,
        }

    def print_registro(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        wizard = self.browse(cr, uid, ids)[0]
        move_obj = self.pool.get('account.move')
        obj_model_data = self.pool.get('ir.model.data')
        move_ids = move_obj.search(cr, uid, [
            ('journal_id', 'in', [j.id for j in wizard.journal_ids]),
            ('period_id', '=', wizard.period_id.id),
            ('state', '=', 'posted'),
            ], order='date')
        if not move_ids:
            self.write(cr, uid,  ids, {'message': _('No documents found in the current selection')})
            model_data_ids = obj_model_data.search(cr, uid, [('model','=','ir.ui.view'), ('name','=','wizard_registro_iva')])
            resource_id = obj_model_data.read(cr, uid, model_data_ids, fields=['res_id'])[0]['res_id']
            return {
                'name': _('No documents'),
                'res_id': ids[0],
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'wizard.registro.iva',
                'views': [(resource_id,'form')],
                'context': context,
                'type': 'ir.actions.act_window',
                'target': 'new',
            }
        datas = {'ids': move_ids}
        datas['model'] = 'account.move'
        datas['period_id'] = wizard.period_id.id
        datas['layout'] = wizard['type']
        res= {
            'type': 'ir.actions.report.xml',
            'datas': datas,
        }
        if wizard['type'] == 'customer':
            res['report_name'] = 'registro_iva_vendite'
        elif wizard['type'] == 'supplier':
            res['report_name'] = 'registro_iva_acquisti'
        elif wizard['type'] == 'corrispettivi':
            res['report_name'] = 'registro_iva_corrispettivi'
        return res
