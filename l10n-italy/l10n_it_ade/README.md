[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=7.0)](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=7.0)](https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=7.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/7.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/7.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg)](https://github.com/OCA/l10n-italy/tree/7.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](https://erp7.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

[![icon](static/src/img/icon.png)](https://travis-ci.org/zeroincombenze)


Base xml Agenzia delle Entrate
==============================

This module has no any specific function for End-user. It is base for modules
generate xml file like FatturaPA o VAT settlement.



[![it](https://github.com/zeroincombenze/grymb/blob/master/flags/it_IT.png)](https://www.facebook.com/groups/openerp.italia/)

Localizzazione italiana - Definizioni per file xml
==================================================

Questo modulo non ha funzioni specifice per l'utente finale. Serve come base
per i moduli che generano file xml in formato stabilito dall'Agenzia delle
Entrate, come FatturaPA o Liquidazione IVA elettronica.

:warning: Lo schema di definizione dei file xml, pubblicato
con urn:www.agenziaentrate.gov.it:specificheTecniche è base per tutti i file
xml dell'Agenzia delle Entrate; come conseguenza nasce un conflitto tra
moduli diversi che riferiscono allo schema dell'Agenzia delle Entrate,
segnalato dall'errore:

:heavy_exclamation_mark: *name CryptoBinary used for multiple values in typeBinding*

Tutti i moduli della localizzazione italiana che generano file xml dipendenti
dallo schema dell'Agenzia delle Entrate *devono* dichiare questo modulo
come dipendenza.

Per maggiori informazioni visitare il sito www.odoo-italia.org o contattare
l'ultimo autore: Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>.

### Schemi

Il modulo rende disponibili i seguenti schemi:

* Liquidazione IVA elettronica versione 1.0
* Comunicazione clienti e fornitori (spesometro light 2018) versione 2.1
* FatturaPA versione 1.2


Per aggiungere nuovi schemi o modificare o aggiornare gli schemi gestiti:

- Aggiungere o modificare gli schemi nella directory ./binding
- Eseguire da una macchina CentOS lo script ./pyxbgen.sh -u



### Funzionalità & Certificati

Funzione | Status | Note
--- | --- | ---
Definizione sezionale autofatture | :white_check_mark: |
Definizione sezionale corrispettivi | :white_check_mark: | Funzionalità modulo OCA duplicata
Definizione sezionale avvisi di parcella | :white_check_mark: | Necessario per modulo RA
Definizione sezionale fattura elettronica | :white_check_mark: | Necessario per fattura elettronica


Logo | Ente/Certificato | Data inizio | Da fine | Note
--- | --- | --- | --- | ---
[![xml_schema](https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/icons/xml-schema.png)](https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/scope/xml-schema.md) | [ISO + Agenzia delle Entrate](http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/) | 01-10-2017 | 31-12-2017 | Validazione contro schema xml
[![xml_schema](https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/icons/fatturapa.png)](https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/fatturapa.md) | [Agenzia delle Entrate](http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/) | 05-10-2017 | 31-12-2017 | Modulo [l10n_it_vat_communication](l10n_it_vat_communication/)
[![fatturapa](https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/icons/fatturapa.png)](https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/fatturapa.md) | [FatturaPA](http://www.fatturapa.gov.it/export/fatturazione/it/fattura_PA.htm) | 22-09-2017 | 31-12-2017 | Modulo [l10n_it_fatturapa](l10n_it_fatturapa/)



Installation
------------

These instruction are just an example to remember what you have to do:

    pip install PyXB==1.2.4
    git clone https://github.com/zeroincombenze/l10n-italy
    cp -R l10n-italy/l10n_it_ade ODOO_DIR/l10n-italy/
    sudo service odoo-server restart -i l10n_it_ade -d MYDB

From UI: go to Setup > Module > Install


Configuration
-------------

:mute:


Usage
-----

For furthermore information, please visit http://wiki.zeroincombenze.org/it/Odoo/7.0/man/FI


Known issues / Roadmap
----------------------

:ticket: This module replace OCA module; PR will be issued
In order to use this module you have to use:

* [l10n_it_base](l10n_it_base/) replaces OCA module


Bug Tracker
-----------

Have a bug? Please visit https://odoo-italia.org/index.php/kunena/home

Credits
-------

### Contributors

* Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
* Andrei Levin <andrei.levin@didotech.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>

### Funders

This module has been financially supported by

* SHS-AV s.r.l. <https://www.zeroincombenze.it/>
* Didotech srl <http://www.didotech.com>

### Maintainer

[![Odoo Italia Associazione](https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png)](https://odoo-italia.org)

Odoo Italia is a nonprofit organization whose develops Italian Localization for
Odoo.

To contribute to this module, please visit <https://odoo-italia.org/>.


[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**Odoo Italia Associazione**, or the [Associazione Odoo Italia](https://www.odoo-italia.org/)
is the nonprofit Italian Community Association whose mission
is to support the collaborative development of Odoo designed for Italian law and markeplace.
Since 2017 Odoo Italia Associazione issues modules for Italian localization not developed by OCA
or available only with Odoo Proprietary License.
Odoo Italia Associazione distributes code under [AGPL](https://www.gnu.org/licenses/agpl-3.0.html) or [LGPL](https://www.gnu.org/licenses/lgpl.html) free license.

[Odoo Italia Associazione](https://www.odoo-italia.org/) è un'Associazione senza fine di lucro
che dal 2017 rilascia moduli per la localizzazione italiana non sviluppati da OCA
o disponibili solo con [Odoo Proprietary License](https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html).

Odoo Italia Associazione distribuisce il codice esclusivamente con licenza [AGPL](https://www.gnu.org/licenses/agpl-3.0.html) o [LGPL](https://www.gnu.org/licenses/lgpl.html)

[//]: # (end copyright)

[//]: # (addons)

[//]: # (end addons)



[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
