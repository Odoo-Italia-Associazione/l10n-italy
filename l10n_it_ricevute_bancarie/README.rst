[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=10.0)](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy)
[![license lgpl](https://img.shields.io/badge/licence-LGPL--3-7379c3.svg)](https://www.gnu.org/licenses/lgpl.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=10.0)](https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=10.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/10.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/10.0)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](https://erp10.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=================
Ricevute Bancarie
=================

Configurazione

Nella configurazione delle Ri.Ba. è possibile specificare se si tratti di
'salvo buon fine' o 'al dopo incasso', che hanno un flusso completamente diverso.

 - Al dopo incasso: nessuna registrazione verrà effettuata automaticamente e le fatture risulteranno pagate solo al momento dell'effettivo incasso.
 - Salvo buon fine: le registrazioni generate seguiranno la struttura descritta nel documento http://goo.gl/jpRhJp

E' possibile specificare diverse configurazioni (dal menù
configurazioni -> varie -> Ri.Ba.). Per ognuna, in caso di 'salvo buon fine',
è necessario specificare almeno il sezionale ed il conto da
utilizzare al momento dell'accettazione della distinta da parte della banca.
Tale conto deve essere di tipo 'crediti' (ad esempio "Ri.Ba. all'incasso",
eventualmente da creare).

La configurazione relativa alla fase di accredito, verrà usata nel momento in
cui la banca accredita l'importo della distinta.
E' possibile utilizzare un sezionale creato appositamente, ad esempio "accredito RiBa",
ed un conto chiamato ad esempio "banche c/RIBA all'incasso", che non deve essere di tipo 'banca'.

La configurazione relativa all'insoluto verrà utilizzata in caso di mancato pagamento da parte del cliente.
Il conto può chiamarsi ad esempio "crediti insoluti".

Nel caso si vogliano gestire anche le spese per ogni scadenza con ricevuta bancaria,
si deve configurare un prodotto di tipo servizio e legarlo in
Configurazione -> Contabilità -> Ri.Ba. Configurazione spese d'incasso -> Servizio spese d'incasso.

Utilizzo

Per utilizzare il meccanismo delle Ri.Ba. è necessario configurare un termine
di pagamento di tipo 'Ri.Ba.'.

Per emettere una distinta bisogna andare su Ri.Ba. -> emetti Ri.Ba. e
selezionare i pagamenti per i quali emettere la distinta.
Se per il cliente è stato abilitato il raggruppo, i pagamenti dello stesso
cliente e con la stessa data di scadenza andranno a costituire un solo elemento
della distinta.

I possibili stati della distinta sono: bozza, accettata, accreditata, pagata,
insoluta, annullata.
Ad ogni passaggio di stato sarà possibile generare le relative registrazioni
contabili, le quali verranno riepilogate nel tab 'contabilità'.
Questo tab è presente sia sulla distinta che sulle sue righe.


Installation
------------

Configuration
-------------

Usage
-----

=====

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/122/10.0

Known issues / Roadmap
----------------------

Bug Tracker
-----------

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/l10n-italy/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
-------

### Contributors

* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Andrea Cometa <a.cometa@apuliasoftware.it>
* Andrea Gallina <a.gallina@apuliasoftware.it>
* Davide Corio <info@davidecorio.com>
* Giacomo Grasso <giacomo.grasso@agilebg.com>
* Gabriele Baldessari <gabriele.baldessari@gmail.com>
* Alex Comba <alex.comba@agilebg.com>

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







