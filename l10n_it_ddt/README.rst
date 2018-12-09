[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=10.0)](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy)
[![license lgpl](https://img.shields.io/badge/licence-LGPL--3-7379c3.svg)](https://www.gnu.org/licenses/lgpl.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=10.0)](https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=10.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/10.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/10.0)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](https://erp10.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================================================
Italian Localization - DDT: Documento di trasporto
==================================================

This modules extends stock_picking_package_preparation module adding DDT data

Installation
------------

Configuration
-------------

Usage
-----

=====

English

You can automatically create a DDT From a Sale Order, setting
'Automatically create the DDT' field that will automatically create the DDT on
Sale Order confirmation.

You can also directly create a DDT using
Inventory -> Operations -> DDT
menu and add existings delivery orders to it, in the 'transfers' tab.

You can add lines to an existing DDT using the 'Details' tab.
Lines can be descriptive or linked to a product. If linked to a product,
the stock movement will also be created.

When you work with delivery orders, you can create a DDT selecting 1 or more
pickings and launching the action 'DDT from pickings'.

Also, you can select 1 or more pickings and run 'add pickings to DDT' to add
the selected delivery orders to an existing DDT

If the state of the delivery orders allows it, you can deliver them from the
DDT directly, clicking 'put in pack' and 'package done'.

Otherwise, you can process delivery orders separately, then go to the DDT and
click on 'set done'.

Finally you can create your invoice directly from the DDT using the 
'Create Invoice' button that creates a new Invoice with the ddt lines as 
invoice lines

Italian

È possibile creare automaticamente un DDT da un ordine di vendita, impostando
il campo 'crea automaticamente il DDT' che creerà il DDT alla conferma
dell'ordine.

È anche possibile creare un DDT direttamente, usando
Inventario -> Operazioni -> DDT
e aggiungendo degli ordini di consegna esistenti al DDT, nel tab
'trasferimenti'.

È possibile aggiungere righe ad un DDT esistente usando il tab 'Dettaglio'.
Le righe possono essere descrittive o collegate a prodotti. Le righe collegate
ad un prodotto creeranno anche i movimenti di magazzino.

Se si lavora con gli ordini di consegna, è possibile creare un DDT selezionando
1 o più ordini di consegna ed eseguendo l'azione 'DDT da Picking'.

Inoltre, è possibile selezionare 1 o più ordini di consegna ed eseguire
'aggiungi Picking al DDT' per aggiungere gli ordini selezionati ad un DDT
esistente.

Se lo stato degli ordini di consegna lo permette, è possibile consegnarli tutti
direttamente dal DDT, cliccando sui bottoni 'metti nel pacco' e
'pacco completato'.

Altrimenti, è possibile processare gli ordini di consegna separatamente, poi
andare sul DDT e cliccare su 'imposta completato'.

Infine, è possibile creare la fattura direttamente dal DDT usando il bottone
'crea fattura' il quale crea una nuova fattura usando le righe del DDT.

E' possibile fatturare i DDT che hanno una 'Causale trasporto' impostata come 'da fatturare'

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/122/10.0

Known issues / Roadmap
----------------------

Bug Tracker
-----------

Credits
-------

### Contributors

* Davide Corio <davide.corio@abstract.it>
* Nicola Malcontenti <nicola.malcontenti@agilebg.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Francesco Apruzzese <f.apruzzese@apuliasoftware.it>
* Andrea Gallina <a.gallina@apuliasoftware.it>
* Alex Comba <alex.comba@agilebg.com>
* Andrea Cometa <a.cometa@apuliasoftware.it>
* Alessandro Camilli <alessandrocamilli@openforce.it>
* Antonio Maria Vigliotti <info@shs-av.com>

### Funders

### Maintainer

.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose mission is to support the collaborative development of Odoo features and promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.

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







