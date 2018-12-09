[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=10.0)](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy)
[![license lgpl](https://img.shields.io/badge/licence-LGPL--3-7379c3.svg)](https://www.gnu.org/licenses/lgpl.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=10.0)](https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=10.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/10.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/10.0)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](https://erp10.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=======================
Italian Withholding Tax
=======================

La ritenuta d’acconto odoo provvede a calcolare automaticamente i valori delle diverse tipologie di ritenuta presenti nella contaiblità italiana.

In odoo ritenuta d’acconto è possibile, tramite apposito workflow, gestire i diversi passaggi di stato delle ritenute rilevate: dovuta, applicata, versata

Installation
------------

Configuration
-------------

Usage
-----

=====

Per prima cosa dovremo creare una ritenuta d’acconto odoo dove inserire tutti i campi necessari per un corretto calcolo.

Visto che le aliquote possono variare nel corso del tempo, nella codifica sono previsti scaglioni temporali di competenza.

E’ necessario anche inserire i conti contabili che verranno utilizzati quando il modulo si occuperà di generare registrazioni contabili per la rilevazione della ritenuta.

.. figure:: https://raw.githubusercontent.com/OCA/l10n-italy/10.0/l10n_it_withholding_tax/static/img/ritenuta-acconto-odoo-codifica-768x457.png
   :alt: alternative description
   :width: 600 px

Una volta aggiunta, nella tabella ritenute, potrà essere utilizzata all’interno della fattura, in corrispondenza delle righe soggette a ritenute.

Per ogni riga è possibile utilizzare più di una ritenuta. Per alcune casistiche il moduo ritenute viene usato anche per rilevare le trattenute INPS.

Il modulo ritenute per Odoo calcolerà i valori corrispondenti e ne mostrerà il dettaglio nell’apposita area ritenute, dove è possibile verificare per ogni codice ritenuta usato, l’imponibile e l’importo ritenuta applicato.

In calce ai totali, verrà totalizzato l’ammontare della ritenuta e il netto a pagare. Questa sezione sarà visibile solamente in presenza di almeno una ritenuta

.. figure:: https://raw.githubusercontent.com/OCA/l10n-italy/10.0/l10n_it_withholding_tax/static/img/fattura-fornitore-768x517.png
   :alt: alternative description
   :width: 600 px

Successivamente andando nella sezione situazione ritenute d’acconto odoo vi mostrerà una situazione riepilogativa delle varie ritenute divisa per documento di origine.

I campi principalmente da tenere in considerazione in questa tabella sono: ritenuta dovuta, ritenuta applicata e ritenuta versata.

*Ritenuta dovuta* contiene il valore della ritenuta contenuta nella fattura.

*Ritenuta applicata* mostra il valore della ritenuta rilevata al momento del pagamento della fattura.

*Ritenuta versata* contiene l’importo di ritenuta, già applicata, che è stata versata all’erario

.. figure:: https://raw.githubusercontent.com/OCA/l10n-italy/10.0/l10n_it_withholding_tax/static/img/foto-3-1-1024x505.png
   :alt: alternative description
   :width: 600 px

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/122/8.0

Known issues / Roadmap
----------------------

Bug Tracker
-----------

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/l10n-italy/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback

Credits
-------

### Contributors

* Alessandro Camilli <alessandrocamilli@openforce.it>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>

### Funders

### Maintainer

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.

Sponsor

'Odoo Italia Network <http://www.odoo-italia.net/>'_

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







