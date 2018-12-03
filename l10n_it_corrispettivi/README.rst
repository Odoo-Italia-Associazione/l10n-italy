[![Build Status](https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=10.0)](https://travis-ci.org/zeroincombenze/l10n-italy)
[![license lgpl](https://img.shields.io/badge/licence-LGPL--3-7379c3.svg)](https://www.gnu.org/licenses/lgpl.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=10.0)](https://coveralls.io/github/zeroincombenze/l10n-italy?branch=10.0)
[![codecov](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg)](https://github.com/OCA/l10n-italy/tree/10.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/man/FI)
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

**zeroincombenze®** is a trademark of [SHS-AV s.r.l.](http://www.shs-av.com/)
which distributes and promotes **Odoo** ready-to-use on own cloud infrastructure.
[Zeroincombenze® distribution of Odoo](http://wiki.zeroincombenze.org/en/Odoo)
is mainly designed for Italian law and markeplace.
Users can download from [Zeroincombenze® distribution](https://github.com/zeroincombenze/OCB) and deploy on local server.

[//]: # (end copyright)





[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
