|Maturity| |Build Status| |license gpl| |Coverage Status| |Codecov Status| |OCA project| |Tech Doc| |Help| |Try Me|

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/8.0/l10n_it_ade/static/description/icon.png

================================================
|icon| Definizioni di Base Agenzia delle Entrate
================================================

.. contents::


|en|

Tax Authority Definitions
==========================

This module has no specific function for End-user.

It defines the structures by Italian Tax Authority to manage
all fiscal communications.
Inside there are xml schema files used by FatturaPA, EInvoice and VAT settlement.

This module requires `PyXB 1.2.4 <http://pyxb.sourceforge.net/>`__


|it|

Definizioni Agenzia delle Entrate
==================================

Questo modulo non ha funzioni specifiche per l'utente finale.
Contiene dati e definizioni stabilite dall'Agenzia delle Entrate
All'interno sono presenti gli schemi xml usati da FatturaPA,
Fattura Elettronica B2B, Liquidazione IVA elettronica e Comunicazione IVA.

|info| Questo modulo è incompatibile con alcuni moduli OCA.

|warning| Lo schema di definizione dei file xml, pubblicato
con urn:www.agenziaentrate.gov.it:specificheTecniche è base per tutti i file
xml dell'Agenzia delle Entrate; come conseguenza nasce un conflitto tra
moduli diversi che riferiscono allo schema dell'Agenzia delle Entrate,
segnalato dall'errore:

|exclamation| name CryptoBinary used for multiple values in typeBinding

Tutti i moduli della localizzazione italiana che generano file xml dipendenti
dallo schema dell'Agenzia delle Entrate devono dichiare il modulo
`l10n_it_ade <https://github.com/zeroincombenze/l10n-italy/tree/8.0/l10n_it_ade>`__ come dipendenza.

Per maggiori informazioni visitare il sito www.odoo-italia.org o contattare
l'ultimo autore: Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>.

Features / Funzioni
--------------------

+------------------------------------------------------+----------+----------------------------------------------+
| Feature / Funzione                                   |  Status  | Notes / Note                                 |
+------------------------------------------------------+----------+----------------------------------------------+
| Generate / Emissione FatturaPA                       | |check|  | Genera file .xml versione 1.2                |
+------------------------------------------------------+----------+----------------------------------------------+
| Generate / Emissione Fattura B2B                     | |check|  | Genera file .xml versione 1.2                |
+------------------------------------------------------+----------+----------------------------------------------+
| Company info form invoice / Dati azienda da fattura  | |check|  | Versione OCA utilizza dati azienda da utente |
+------------------------------------------------------+----------+----------------------------------------------+
| Validation suring editing / Controlli in tempo reale | |check|  |                                              |
+------------------------------------------------------+----------+----------------------------------------------+


OCA Differences / Differenze da OCA
------------------------------------

+--------------------------------------+-------------------------+-------------------------+--------------------------------+
| Description / Descrizione            | Odoo Italia             | OCA                     | Notes / Note                   |
+--------------------------------------+-------------------------+-------------------------+--------------------------------+
| Company / Azienda                    | By User / Da Utente     | By Invoice / Da Fattura | Different layout               |
+--------------------------------------+-------------------------+-------------------------+--------------------------------+
| PEC                                  | PEC fattura o aziendale | Solo PEC fattura        |                                |
+--------------------------------------+-------------------------+-------------------------+--------------------------------+
| Phone + Fax / Telefono + Fax         | Formato libero          | Solo numeri senza segni |                                |
+--------------------------------------+-------------------------+-------------------------+--------------------------------+
| Controllo dati durante inserimento   | |check|                 | |no_check|              |                                |
+--------------------------------------+-------------------------+-------------------------+--------------------------------+
| Strutturazione dati                  |                         |                         | Mix moduli con compatibile     |
+--------------------------------------+-------------------------+-------------------------+--------------------------------+


Certifications / Certificazioni
--------------------------------

+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| Logo                 | Ente/Certificato                                                                                                                                                                                                  | Data inizio   | Da fine      | Note                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| |xml\_schema|        | `ISO + Agenzia delle Entrate <http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/>`__                             | 01-06-2017    | 31-12-2018   | Validazione contro schema xml                |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| |FatturaPA|          | `FatturaPA <https://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Schede/Comunicazioni/Fatture+e+corrispettivi/Fatture+e+corrispettivi+ST/ST+invio+di+fatturazione+elettronica/?page=schedecomunicazioni/>`__  | 01-06-2017    | 31-12-2018   | Controllo tramite sito Agenzia delle Entrate |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+



|en|


Installation / Installazione
=============================

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| These instruction are just an   | Istruzioni di esempio valide solo per    |
| example to remember what        | distribuzioni Linux CentOS 7, Ubuntu 14+ |
| you have to do on Linux.        | e Debian 8+                              |
|                                 |                                          |
| Installation is based on:       | L'installazione è basata su:             |
+---------------------------------+------------------------------------------+
| `Zeroincombenze Tools <https://github.com/zeroincombenze/tools>`__         |
+---------------------------------+------------------------------------------+
| Suggested deployment is         | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| **/opt/odoo/8.0/l10n-italy/**                                              |
+----------------------------------------------------------------------------+

|

::

    cd $HOME
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    export PATH=$HOME/dev:$PATH
    odoo_install_repository l10n-italy -b 8.0 -O zero
    for pkg in os0 z0lib; do
        pip install $pkg -U
    done
    sudo manage_odoo requirements -b 8.0 -vsy -o /opt/odoo/8.0


|

From UI: go to:

|menu| Setting > Modules > Update Modules List

|menu| Setting > Local Modules |right_do| Select **l10n_it_ade** > Install

|warning| If your Odoo instance crashes, you can do following instruction
to recover installation status:

``run_odoo_debug 8.0 -um l10n_it_ade -s -d MYDB``

Upgrade / Aggiornamento
------------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| When you want upgrade and you   | Per aggiornare, se avete installato con  |
| installed using above           | le istruzioni di cui sopra:              |
| statements:                     |                                          |
+---------------------------------+------------------------------------------+

::

    cd /opt/odoo/8.0/l10n-italy/
    git pull origin 8.0
    # Adjust following statements as per your system
    sudo systemctl restart odoo





Usage / Uso
============

|menu| Contabilità > Configurazione > Contabilità > Definizioni Agenzia delle Entrate > Natura dell'IVA

|menu| Contabilità > Configurazione > Contabilità > Definizioni Agenzia delle Entrate > Tipi Fattura

|menu| Contabilità > Configurazione > Contabilità > Definizioni Agenzia delle Entrate > Codice Carica




Known issues / Roadmap
=======================

|warning| Questo modulo rimpiazza il modulo OCA. Leggete attentamente il
paragrafo relativo alle funzionalità e differenze.




Issue Tracker
==============

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/zeroincombenze/l10n-italy/issues>`_.

In case of trouble, please check there if your issue has already been reported.


Proposals for enhancement
--------------------------

If you have a proposal to change this module, you may want to send an email to
<moderatore@odoo-italia.org> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.





Credits / Riconoscimenti
=========================

Authors / Autori
-----------------


* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__

Contributors / Contributi
--------------------------


* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

Maintainers / Manutezione
--------------------------

|Odoo Italia Associazione|

This module is maintained by the Odoo Italia Associazione.

To contribute to this module, please visit https://odoo-italia.org/.



----------------

**Odoo** is a trademark of `Odoo S.A. <https://www.odoo.com/>`__
(formerly OpenERP)

**OCA**, or the `Odoo Community Association <http://odoo-community.org/>`__,
is a nonprofit organization whose mission is to support
the collaborative development of Odoo features and promote its widespread use.

**zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes **Odoo** ready-to-use on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://wiki.zeroincombenze.org/en/Odoo>`__
is mainly designed for Italian law and markeplace.

Users can download from `Zeroincombenze® distribution <https://github.com/zeroincombenze/OCB>`__
and deploy on local server.


|

Last Update / Ultimo aggiornamento: 2018-10-26

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=8.0
    :target: https://travis-ci.org/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=8.0
    :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=8.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/8.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/8.0
    :alt: Codecov
.. |OCA project| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg
    :target: https://github.com/OCA/l10n-italy/tree/8.0
    :alt: OCA
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/8.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/8.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg
    :target: https://erp8.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov Status| image:: badge-oca-codecov
    :target: oca-codecov-URL
    :alt: Codecov
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/check.png
.. |no_check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/no_check.png
.. |menu| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/menu.png
.. |right_do| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/right_do.png
.. |exclamation| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/exclamation.png
.. |warning| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/warning.png
.. |same| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/same.png
.. |late| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/late.png
.. |halt| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/halt.png
.. |info| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/info.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/DesktopTelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/fatturapa.md


