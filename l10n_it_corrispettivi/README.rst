[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=10.0)](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy)
[![license lgpl](https://img.shields.io/badge/licence-LGPL--3-7379c3.svg)](https://www.gnu.org/licenses/lgpl.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=10.0)](https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=10.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/10.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/10.0)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](https://erp10.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

.. image:: https://img.shields.io/badge/license-LGPL--3-blue.png
   :target: https://www.gnu.org/licenses/lgpl
   :alt: License: LGPL-3

====================================
Italian Localization - Corrispettivi
====================================

Questo modulo permette di generare le ricevute specificando le varie aliquote per riga
(le righe della ricevuta hanno gli stessi automatismi di quelle della fattura) e quindi registrare le ricevute una per una.
Un esempio tipico di questo caso d’uso è la vendita tramite sito di e-commerce.

Chi invece emette scontrini (e non ha un POS integrato con Odoo) dovrà registrare in contabilità, a fine giornata, gli incassi totali.

Installation
------------

Configuration
-------------

Creare almeno un sezionale di tipo vendita su cui saranno registrati i corrispettivi,
deve avere il flag corrispettivi abilitato.

Se necessario, creare una posizione fiscale per i corrispettivi, deve avere il flag corrispettivi abilitato.
Questa posizione fiscale verrà assegnata a tutti i nuovi partner aventi il flag *Usa corrispettivi* abilitato.

Utilizzando un utente del gruppo Contabilità & Finanza > Contabilità, sul partner associato al public user:

* Modificare, se necessario, i conti di debito e di credito da utilizzare per i corrispettivi;
* Abilitare il flag *Usa corrispettivi*

Nota: di default, il public user è disabilitato (flag active disabilitato).

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

Images

* Odoo Community Association: `Icon <https://odoo-community.org/logo.png>`_.

### Contributors

* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Simone Rubino <simone.rubino@agilebg.com>

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







