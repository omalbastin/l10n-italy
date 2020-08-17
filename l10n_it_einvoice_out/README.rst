
==================================================
|icon| Italian Localization - FatturaPA - Emission
==================================================


**Electronic invoices emission**

.. |icon| image:: https://raw.githubusercontent.com/Odoo-Italia-Associazione/l10n-italy/8.0/l10n_it_einvoice_out/static/description/icon.png

|Maturity| |Build Status| |Coverage Status| |Codecov Status| |license gpl| |Tech Doc| |Help| |Try Me|

.. contents::


Overview / Panoramica
=====================

|en| EInvoice + FatturaPA
====================

This module allows you to generate the fatturaPA XML file version 1.2
which will be sent to the SdI (Exchange System by Italian Tax Authority)

http://www.fatturapa.gov.it/export/fatturazione/it/normativa/norme.htm

|warning| Read carefully note of module l10n_it_einvoice_base before install this module

|halt| Do not use this module on production environment: it is an aplha release
subjected to update.

|

|it| Fattura Elettronica + FatturaPA
===============================

Questo modulo permette di generare il file xml della fatturaPA versione 1.2
da trasmettere al sistema di interscambio SdI.

|warning| Lo schema di definizione dei file xml, pubblicato
con urn:www.agenziaentrate.gov.it:specificheTecniche è base per tutti i file
xml dell'Agenzia delle Entrate; come conseguenza nasce un conflitto tra
moduli diversi che riferiscono allo schema dell'Agenzia delle Entrate,
segnalato dall'errore:

|exclamation| **name CryptoBinary used for multiple values in typeBinding**

Tutti i moduli della localizzazione italiana che generano file xml dipendenti
dallo schema dell'Agenzia delle Entrate **devono** dichiare il modulo
`l10n_it_ade <../l10n_it_ade>`__ come dipendenza.

Per maggiori informazioni visitare il sito www.odoo-italia.org o contattare
l'ultimo autore: Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>.

|halt| Non utilizzare ancora questo modulo in produzione: alpha release soggetta
ad ulteriori modifiche

|

Features / Caratteristiche
--------------------------

Features / Funzioni
-------------------

+--------------------------------------+----------+----------------------------------------------+
| Feature / Funzione                   |  Status  | Notes / Note                                 |
+--------------------------------------+----------+----------------------------------------------+
| Emissione FatturaPA                  | |check|  | Genera file .xml versione 1.2                |
+--------------------------------------+----------+----------------------------------------------+
| Emissione Fattura B2B                | |check|  | Genera file .xml versione 1.2                |
+--------------------------------------+----------+----------------------------------------------+
| Dati azienda da fattura              | |check|  | Versione OCA utilizza dati azienda da utente |
+--------------------------------------+----------+----------------------------------------------+
| Controllo dati durante inserimento   | |check|  |                                              |
+--------------------------------------+----------+----------------------------------------------+


|
|

Certifications / Certificazioni
-------------------------------

Certifications / Certificazioni
-------------------------------

+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| Logo                 | Ente/Certificato                                                                                                                                                                                                  | Data inizio   | Da fine      | Note                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| |xml\_schema|        | `ISO + Agenzia delle Entrate <http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/>`__                             | 01-06-2017    | 31-12-2018   | Validazione contro schema xml                |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| |FatturaPA|          | `FatturaPA <https://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Schede/Comunicazioni/Fatture+e+corrispettivi/Fatture+e+corrispettivi+ST/ST+invio+di+fatturazione+elettronica/?page=schedecomunicazioni/>`__  | 01-06-2017    | 31-12-2018   | Controllo tramite sito Agenzia delle Entrate |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+


|

Usage / Utilizzo
----------------

Usage / Uso
===========

|menu| Configurazione > Configurazione > Contabilità > Fattura PA |do_right| Impostare i vari parametri
|menu| Contabilità > Configurazione > Sezionali > Sezionali |do_right| Impostare sezionale fattura elettronica
|menu| Contabilità > Configurazione > Imposte > Imposte |do_right| Impostare natura codici IVA
|menu| Contabilità > Configurazione > Management > Termini di pagamento |do_right| Collegare i termini di pagamento con i relativi termini fiscali
|menu| Contabilità > Clienti > Clienti |do_right| Impostare Codice Destinatario o PEC o IPA, nazione, partita IVA, codice fiscale
|menu| Contabilità > Configurazione > Contabilità > Posizioni fiscali |do_right| Collegare posizioni fiscali con regimi fiscali

Per consultazione (non modificare):

|menu| Contabilità > Configurazione > Contabilità > Definizioni Agenzia delle Entrate > Natura dell'IVA
|menu| Contabilità > Configurazione > Contabilità > Definizioni Agenzia delle Entrate > Tipi Fattura


|

OCA comparation / Confronto con OCA
-----------------------------------

OCA Differences / Differenze da OCA
-----------------------------------

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


|
|

Getting started / Come iniziare
===============================

|Try Me|


Prerequisites / Prerequisiti
----------------------------


* python
* postgresql 9.2+

|

Installation / Installazione
----------------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| These instruction are just an   | Istruzioni di esempio valide solo per    |
| example to remember what        | distribuzioni Linux CentOS 7, Ubuntu 14+ |
| you have to do on Linux.        | e Debian 8+                              |
|                                 |                                          |
| Installation is built with:     | L'installazione è costruita con:         |
+---------------------------------+------------------------------------------+
| `Zeroincombenze Tools <https://github.com/zeroincombenze/tools>`__         |
+---------------------------------+------------------------------------------+
| Suggested deployment is:        | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| /opt/odoo/8.0/l10n-italy/                                                  |
+----------------------------------------------------------------------------+

::

    cd $HOME
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    export PATH=$HOME/dev:$PATH
    odoo_install_repository l10n-italy -b 8.0 -O oia
    for pkg in os0 z0lib; do
        pip install $pkg -U
    done
    sudo manage_odoo requirements -b 8.0 -vsy -o /opt/odoo/8.0

From UI: go to:

* |menu| Setting > Modules > Update Modules List
* |menu| Setting > Local Modules |right_do| Select **l10n_it_einvoice_out** > Install

|

Upgrade / Aggiornamento
-----------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| When you want upgrade and you   | Per aggiornare, se avete installato con  |
| installed using above           | le istruzioni di cui sopra:              |
| statements:                     |                                          |
+---------------------------------+------------------------------------------+

::

    odoo_install_repository l10n-italy -b 8.0 -O oia -U
    # Adjust following statements as per your system
    sudo systemctl restart odoo

From UI: go to:

* |menu| Setting > Modules > Update Modules List
* |menu| Setting > Local Modules |right_do| Select **l10n_it_einvoice_out** > Update

|

Support / Supporto
------------------


|Odoo Italia Associazione| This module is maintained by the Odoo Italia Associazione and free support is supplied through its `forum <https://odoo-italia.org/index.php/kunena/recente>`__


|
|

Get involved / Ci mettiamo in gioco
===================================

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/Odoo-Italia-Associazione/l10n-italy/issues>`_.

In case of trouble, please check there if your issue has already been reported.

Proposals for enhancement
-------------------------


If you have a proposal to change this module, you may want to send an email to <moderatore@odoo-italia.org> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.

|
|

Credits / Titoli di coda
========================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)



|

Authors / Autori
----------------

* `Agile Business Group sagl <https://www.agilebg.com/>`__
* `Innoviu srl <http://www.innoviu.com>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__

Contributors / Collaboratori
----------------------------

* Davide Corio <davide.corio@abstract.it>
* Roberto Onnis <roberto.onnis@innoviu.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Alessio Gerace <alessio.gerace@agilebg.com>
* Alex Comba <alex.comba@agilebg.com>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

|

----------------


|en| **Odoo Italia Associazione**, or the `Associazione Odoo Italia <https://www.odoo-italia.org/>`__ is the nonprofit Italian Community Association born in 2011, whose mission is promote use of Odoo to cover Italian law and markeplace.
Since 2017 Odoo Italia Associazione issues modules for Italian localization developed by OCA and others not released under `Odoo Proprietary License <https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html>`__

Odoo Italia Associazione distributes code under `AGPL <https://www.gnu.org/licenses/agpl-3.0.html>`__ or `LGPL <https://www.gnu.org/licenses/lgpl.html>`__ free licenses.

Read carefully published README for more info about authors.

|it| `Odoo Italia Associazione <https://www.odoo-italia.org/>`__ è un'Associazione senza fine di lucro, nata nel 2011 che dal 2017 rilascia moduli per la localizzazione italiana sviluppati da OCA o da terze parti che non siano rilasciati con `Odoo Proprietary License <https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html>`__

Odoo Italia Associazione distribuisce il codice esclusivamente con licenze `AGPL <https://www.gnu.org/licenses/agpl-3.0.html>`__ o `LGPL <https://www.gnu.org/licenses/lgpl.html>`__

Leggere con attenzione i file README per maggiori informazioni sugli autori.


|chat_with_us|


|

Last Update / Ultimo aggiornamento: 2018-11-21

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=8.0
    :target: https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Coverage Status| image:: https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=8.0
    :target: https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=8.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/8.0/graph/badge.svg
    :target: https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/8.0
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
    :target: https://odoo8.odoo-italia.org
    :alt: Try Me
.. |OCA Codecov Status| image:: Unknown badge-oca-codecov
    :target: Unknown oca-codecov-URL
    :alt: Codecov
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |Zeroincombenze| image:: https://avatars0.githubusercontent.com/u/6972555?s=460&v=4
   :target: https://www.zeroincombenze.it/
   :alt: Zeroincombenze
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
.. |chat_with_us| image:: https://www.shs-av.com/wp-content/chat_with_us.gif
   :target: https://gitter.im/odoo_italia/development
