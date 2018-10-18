|Maturity| |Build Status| |license gpl| |Coverage Status| |Codecov Status| |OCA project| |Tech Doc| |Help| |Try Me|

.. |icon| image:: https://raw.githubusercontent.com/Odoo-Italia-Associazione/l10n-italy/8.0/l10n_it_fiscal_ipa/static/description/icon.png

==========================
|icon| IPA Code (IndicePA)
==========================

.. contents::


|en|

IPA Code
=========

This module adds IPA (IndicePA) code and Recipient Code fields to partner,
used by Italian Electronic Invoice.

http://www.indicepa.gov.it




|it|

Codice IPA (IndicePA)
======================

Questo modulo permette l'inseriento del codice IPA (IndicePA) e del Codice Destinatario
nell'anagrafica cliente.

Questi dati sono indispensabili per la gestione della Fattura Elettronica B2B e
per la FatturaPA.

http://www.indicepa.gov.it



Features / Funzioni
--------------------

+-------------------------------------------------+----------+----------------------------------------------+
| Feature / Funzione                              |  Status  | Notes / Note                                 |
+-------------------------------------------------+----------+----------------------------------------------+
| Parter: IPA Code / Codice IPA                   | |check|  | Per FatturaPA                                |
+-------------------------------------------------+----------+----------------------------------------------+
| Partner: Recipient Code / Codice Destinatario   | |check|  | EInvoice / Per Fattura Elettronica B2B       |
+-------------------------------------------------+----------+----------------------------------------------+



OCA Differences / Differenze da OCA
------------------------------------

+--------------------------------------+-------------+-------------------+--------------------------------+
| Description / Descrizione            | Odoo Italia | OCA               | Notes / Note                   |
+--------------------------------------+-------------+-------------------+--------------------------------+
| Partner view / Vista cliente         | This Module | This Module       | Different layout               |
+--------------------------------------+-------------+-------------------+--------------------------------+
| IPA Code                             | This Module | This Module       |                                |
+--------------------------------------+-------------+-------------------+--------------------------------+
| Recipient Code / Codice Destinatario | This Module | l10n_it_fatturapa | |warning| Different deployment |
+--------------------------------------+-------------+-------------------+--------------------------------+





|en|


Installation
=============

These instruction are just an example to remember what you have to do.
Installation is based on `Zeroincombenze Tools <https://github.com/zeroincombenze/tools>`__
Deployment is ODOO_DIR/REPOSITORY_DIR/MODULE_DIR where:

| ODOO_DIR is root Odoo directory, i.e. /opt/odoo/8.0
| REPOSITORY_DIR is downloaded git repository directory, currently is: l10n-italy
| MODULE_DIR is module directory, currently is: l10n_it_fiscal_ipa
| MYDB is the database name
|

::

    pip install unidecode
    pip install codicefiscale
    pip install pyxb==1.2.4
    cd $HOME
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    export PATH=$HOME/dev:$PATH
    odoo_install_repository l10n-italy -b 8.0 -O oia


From UI: go to:

|menu| Setting > Modules > Update Modules List

|menu| Setting > Local Modules |right_do| Select **l10n_it_fiscal_ipa** > Install

|warning| If your Odoo instance crashes, you can do following instruction
to recover installation status:

``run_odoo_debug 8.0 -um l10n_it_fiscal_ipa -s -d MYDB``








Known issues / Roadmap
=======================

|warning| Questo modulo rimpiazza il modulo OCA. Leggete attentamente il
paragrafo relativo alle funzionalità e differenze.





Issue Tracker
==============

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/Odoo-Italia-Associazione/l10n-italy/issues>`_.

In case of trouble, please check there if your issue has already been reported.


Proposals for enhancement
--------------------------

If you have a proposal to change this module, you may want to send an email to
<moderatore@odoo-italia.org> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.






Credits
========

Authors
--------


* `KTec S.r.l. <https://www.ktec.it/>`__
* `Agile Business Group sagl <https://www.agilebg.com/>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__

Contributors
-------------


* Luigi Di Naro <luigi.dinaro@ktec.it>
* Alex Comba <alex.comba@agilebg.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

Maintainers
------------

|Odoo Italia Associazione|

This module is maintained by the Odoo Italia Associazione.

To contribute to this module, please visit https://odoo-italia.org/.




----------------

**Odoo** is a trademark of `Odoo S.A. <https://www.odoo.com/>`__
(formerly OpenERP)

**OCA**, or the `Odoo Community Association <http://odoo-community.org/>`__,
is a nonprofit organization whose mission is to support
the collaborative development of Odoo features and promote its widespread use.

**Odoo Italia Associazione**, or the `Associazione Odoo Italia <https://www.odoo-italia.org/>`__
is the nonprofit Italian Community Association whose mission
is to support the collaborative development of Odoo designed for Italian law and markeplace.
Since 2017 Odoo Italia Associazione issues modules for Italian localization not developed by OCA
or available only with Odoo Proprietary License.
Odoo Italia Associazione distributes code under `AGPL <https://www.gnu.org/licenses/agpl-3.0.html>`__
or `LGPL <https://www.gnu.org/licenses/lgpl.html>`__ free license.

`Odoo Italia Associazione <https://www.odoo-italia.org/>`__ è un'Associazione senza fine di lucro
che dal 2017 rilascia moduli per la localizzazione italiana non sviluppati da OCA
o disponibili solo con `Odoo Proprietary License <https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html>`__

Odoo Italia Associazione distribuisce il codice esclusivamente con licenza `AGPL <https://www.gnu.org/licenses/agpl-3.0.html>`__
o `LGPL <https://www.gnu.org/licenses/lgpl.html>`__



.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=8.0
    :target: https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |Coverage Status| image:: https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=8.0
    :target: https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=8.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/8.0/graph/badge.svg
    :target: https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/8.0
    :alt: Codecov
.. |OCA project| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg
    :target: https://github.com/OCA/l10n-italy/tree/8.0
    :alt: OCA
.. |Tech Doc| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg
    :target: http://wiki.zeroincombenze.org/en/Odoo/8.0/dev
    :alt: Technical Documentation
.. |Help| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg
    :target: http://wiki.zeroincombenze.org/it/Odoo/8.0/man
    :alt: Technical Documentation
.. |Try Me| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg
    :target: https://odoo8.odoo-italia.org
    :alt: Try Me
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
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/DesktopTelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/fatturapa.md
   

