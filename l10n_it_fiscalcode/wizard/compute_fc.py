# -*- coding: utf-8 -*-
#    Copyright (C) 2010-2012 Associazione Odoo Italia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
import datetime
from openerp.tools.translate import _
from openerp.osv import fields, orm, osv


# _logger = logging.getLogger(__name__)
# try:
#     from codicefiscale import build
# except ImportError:
#     _logger.warning(
#         'codicefiscale library not found. '
#         'If you plan to use it, please install the codicefiscale library '
#        'from https://pypi.python.org/pypi/codicefiscale')


class wizard_compute_fc(orm.TransientModel):

    _name = "wizard.compute.fc"
    _description = "Compute Fiscal Code"
    _columns = {
        'fiscalcode_surname': fields.char('Surname', size=64),
        'fiscalcode_firstname': fields.char('First name', size=64),
        'birth_date': fields.date('Date of birth'),
        'birth_city': fields.many2one('res.city', 'City of birth'),
        'sex': fields.selection([('M', 'Male'),
                                 ('F', 'Female'),
                                 ], "Sex"),
    }

    def _codicefiscale(
        self, cognome, nome, giornonascita, mesenascita, annonascita, sesso,
        cittanascita
    ):

        MESI = 'ABCDEHLMPRST'
        CONSONANTI = 'BCDFGHJKLMNPQRSTVWXYZ'
        VOCALI = 'AEIOU'
        LETTERE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        REGOLECONTROLLO = {
            'A': (0, 1), 'B': (1, 0), 'C': (2, 5), 'D': (3, 7),
            'E': (4, 9),
            'F': (5, 13), 'G': (6, 15), 'H': (7, 17), 'I': (8, 19),
            'J': (9, 21),
            'K': (10, 2), 'L': (11, 4), 'M': (12, 18), 'N': (13, 20),
            'O': (14, 11),
            'P': (15, 3), 'Q': (16, 6), 'R': (17, 8), 'S': (18, 12),
            'T': (19, 14),
            'U': (20, 16), 'V': (21, 10), 'W': (22, 22), 'X': (23, 25),
            'Y': (24, 24),
            'Z': (25, 23),
            '0': (0, 1), '1': (1, 0), '2': (2, 5), '3': (3, 7),
            '4': (4, 9),
            '5': (5, 13), '6': (6, 15), '7': (7, 17), '8': (8, 19),
            '9': (9, 21)
        }

        # Funzioni per il calcolo del C.F.
        def _surname(stringa):
            """Ricava, da stringa, 3 lettere in base alla convenzione dei C.F.
            """
            cons = [c for c in stringa if c in CONSONANTI]
            voc = [c for c in stringa if c in VOCALI]
            chars = cons + voc
            if len(chars) < 3:
                chars += ['X', 'X']
            return chars[:3]

        def _name(stringa):
            """Ricava, da stringa, 3 lettere in base alla convenzione dei C.F.
            """
            cons = [c for c in stringa if c in CONSONANTI]
            voc = [c for c in stringa if c in VOCALI]
            if len(cons) > 3:
                cons = [cons[0]] + [cons[2]] + [cons[3]]
            chars = cons + voc
            if len(chars) < 3:
                chars += ['X', 'X']
            return chars[:3]

        def _datan(giorno, mese, anno, sesso):
            """Restituisce il campo data del CF."""
            chars = (list(anno[-2:]) + [MESI[int(mese) - 1]])
            gn = int(giorno)
            if sesso == 'F':
                gn += 40
            chars += list("%02d" % gn)
            return chars

        def _codicecontrollo(c):
            """Restituisce il codice di controllo, l'ultimo carattere del
            C.F."""
            sommone = 0
            for i, car in enumerate(c):
                j = 1 - i % 2
                sommone += REGOLECONTROLLO[car][j]
            resto = sommone % 26
            return [LETTERE[resto]]

        # Restituisce il C.F costruito sulla base degli argomenti.
        nome = nome.upper()
        cognome = cognome.upper()
        sesso = sesso.upper()
        cittanascita = cittanascita.upper()
        chars = (_surname(cognome) +
                 _name(nome) +
                 _datan(giornonascita, mesenascita, annonascita, sesso) +
                 list(cittanascita))
        chars += _codicecontrollo(chars)
        return ''.join(chars)

    def compute_fc(self, cr, uid, ids, context):
        active_id = context.get('active_id', [])
        partner = self.pool.get('res.partner').browse(
            cr, uid, active_id, context)
        form_obj = self.browse(cr, uid, ids, context)
        for wizard in form_obj:
            if (
                not wizard.fiscalcode_surname or
                not wizard.fiscalcode_firstname or not wizard.birth_date or
                not wizard.birth_city or not wizard.sex
            ):
                raise osv.except_osv(
                    _('Error'), _('One or more fields are missing'))
            if not wizard.birth_city.cadaster_code:
                raise osv.except_osv(_('Error'), _('Cataster code is missing'))
            birth_date = datetime.datetime.strptime(
                wizard.birth_date, "%Y-%m-%d")
            CF = self._codicefiscale(
                wizard.fiscalcode_surname, wizard.fiscalcode_firstname, str(
                    birth_date.day),
                str(birth_date.month), str(birth_date.year), wizard.sex,
                wizard.birth_city.cadaster_code)
            if partner.fiscalcode and partner.fiscalcode != CF:
                raise osv.except_osv(
                    _('Error'),
                    _('Existing fiscal code %s is different from the computed '
                      'one (%s). If you want to use the computed one, remove '
                      'the existing one') % (partner.fiscalcode, CF))
            self.pool.get('res.partner').write(
                cr, uid, active_id, {'fiscalcode': CF, 'individual': True})
        return {}
