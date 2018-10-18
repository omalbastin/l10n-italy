
Generalization of l10n_es_fiscal_year_closing
See http://apps.openerp.com/addon/4506

Fiscal Year Closing Wizard


Replaces the default OpenERP end of year wizards (from account module)
with a more advanced all-in-one wizard that will let the users:
  - Check for unbalanced moves, moves with invalid dates
    or period or draft moves on the fiscal year to be closed.
  - Create the Loss and Profit entry.
  - Create the Net Loss and Profit entry.
  - Create the Closing entry.
  - Create the Opening entry.

It is stateful, saving all the info about the fiscal year closing, so the
user can cancel and undo the operations easily.
    