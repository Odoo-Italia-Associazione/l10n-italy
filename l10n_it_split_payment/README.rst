[![Build Status](https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=10.0)](https://travis-ci.org/zeroincombenze/l10n-italy)
[![license lgpl](https://img.shields.io/badge/licence-LGPL--3-7379c3.svg)](https://www.gnu.org/licenses/lgpl.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=10.0)](https://coveralls.io/github/zeroincombenze/l10n-italy?branch=10.0)
[![codecov](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg)](https://github.com/OCA/l10n-italy/tree/10.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](https://erp10.zeroincombenze.it)



[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

|br|

=====================================
|icon| Split Payment in Sale Invoices
=====================================

Module to generate Split Payment accounting entries on sale invoices.
=====================================================================

|br|

|it| Fatture clienti in split-payment (scissione pagamenti)

Il modulo permette di emettere fatture e note credito
a clienti in regime di split-payment.

::

    Destinatari:

Il modulo serve alle aziende che devono emettere fatture nei confronti di 
Enti pubblici (PA), aziende partecipate in appalto con PA o
nei confronti aziende quotate in borsa.


::

    Normativa:

La normativa di legge è `(Articolo 17 ter) <http://def.finanze.it/DocTribFrontend/getAttoNormativoDetail.do?ACTION=getArticolo&id={75A4827C-3766-4ECC-9C45-00C8D6CDC552}&codiceOrdinamento=200001700000300&articolo=Articolo%2017%20ter>`__
e successive modificazioni


::

    Funzionalità & Differenze da OCA:

Funzione                                          Status   OCA    Note
Fattura con split payment                          |ok|    |ok|   Richiede modifica report di stampa
Nota Credito con split payment                     |ok|    |ok|   Richiede modifica report di stampa
Cancellazione fattura/NC                           |ok|    |ok|   Prima occore cancellare la riconciliazione

|br|

::

    Note di implementazione:

L'IVA viene calcolata e inserita in fattura ma il credito risultante
dal totale da pagare è detratto dell'IVA.

Nella stampa della fattura si può riportare il totale comprensivo di IVA
*amount_total*, l'IVA *amount_tax* (nella versione OCA questo campo è a zero), l'importo
dell'IVA in split payment *amount_sp* con il segno negativo (nella versione OCA
il segno è positivo) e il netto a pagare *amount_net_pay*

La registrazione contabile contiene le righe di storno
dell'IVA (riconciliata con il credito cliente) e la riga
di IVA in regime di split payment in modo da evidenziare questi dati nella
liquidazione dell'IVA.


Esempio di registrazione fattura con split payment:

::

    =========================   =====   =====   ============================================
    Conto                       Dare    Avere   Note
    =========================   =====   =====   ============================================
    Crediti vs. clienti           122           Modulo OCA registra 100
    Conto di ricavo                       100
    IVA                                    22   Può essere il conto IVA a debito
    IVA in scissione               22           Conto per evidenziare l'IVA in split payment
    Crediti vs. clienti                    22   Riga riconciliata (no esiste in OCA)
    =========================   =====   =====   ============================================


|br|

|en| Installation

These instruction are just an example to remember what you have to do:
::

    $ ODOO\_DIR=/opt/odoo/10.0/l10n-italy # here your Odoo dir
    $ BACKUP\_DIR=/opt/odoo/backup # here your backup dir
    # Check for modules
    $ cd /tmp
    $ git clone https://github.com/zeroincombenze/l10n-italy.git l10n-italy
    $ mv $ODOO\_DIR/l10n-italy/l10n\_it\_split\_payment/ $BACKUP\_DIR/
    $ mv /tmp/l10n-italy/l10n\_it\_split\_payment/ $ODOO\_DIR/


|br|

|it| Configuration/Configurazione

|menu| Contabilità > Configurazione > Contabilità > Posizioni fiscali: Inserire posizione fiscale split payment

|image10|

|menu| Contabilità > Configurazione > Contabilità > Codici IVA: Inserire un codice IVA split payment

|image11|

|menu| Contabilità > Configurazione > Contabilità > Codici IVA: Inserire un codice IVA storno split payment

|image12|

|menu| Contabilità > Configurazione > Configurazione: Impostare dati split payment

|image13|


|br|

|it| Usage/Utilizzo

In crezione fattura o nota di accredito, impostare la posizione fiscale di split payment.
Si consiglia di impostare la posizione fiscale in anagrafica clienti.

|image14|

|br|

Per ulteriori informazioni vedere
`Guida utente Odoo <http://wiki.zeroincombenze.org/it/Odoo/10.0/man/FI/>`__


|br|

|it| Known issues / Roadmap

|warning| Questo modulo rimpiazza il modulo OCA. Leggete attentamente il
paragrafo relativo alle funzionalità e differenze.

|warning| Questo modulo richiede `l10n_it_ade <l10n_it_ade/>`__ che non esiste
nella repository OCA e contiene le stesse definizioni del modulo OCA
*l10n_it_fiscal_document_type* che è quidni incompatbile.


|br|

|en| Bug Tracker

Have a bug? Please visit https://odoo-italia.org/index.php/kunena/home


|br|

|en| Credits

Installation
------------

Configuration
-------------

Usage
-----

Known issues / Roadmap
----------------------

Bug Tracker
-----------

Credits
-------

### Contributors

* Davide Corio <davide.corio@abstract.it>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Alessio Gerace <alessio.gerace@agilebg.com>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

### Funders

This module has been financially supported by

* `Agile BG <https://www.agilebg.com/>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__

### Maintainer

|Odoo Italia Associazione|

Odoo Italia is a nonprofit organization whose develops Italian
Localization for Odoo.

To contribute to this module, please visit https://odoo-italia.org/.


**Odoo** is a trademark of `Odoo S.A. <https://www.odoo.com/>`__
(formerly OpenERP, formerly TinyERP)

**OCA**, or the `Odoo Community Association <http://odoo-community.org/>`__,
is a nonprofit organization whose mission is to support
the collaborative development of Odoo features and promote its widespread use.

**zeroincombenze®** is a trademark of `SHS-AV s.r.l. <http://www.shs-av.com/>`__
which distributes and promotes **Odoo** ready-to-use on own cloud infrastructure.
`Zeroincombenze® distribution <http://wiki.zeroincombenze.org/en/Odoo>`__
is mainly designed for Italian law and markeplace.
Users can download from `Zeroincombenze® distribution <https://github.com/zeroincombenze/OCB>`__
and deploy on local server.


.. |icon| image:: /l10n_it_split_payment/static/description/icon.png
.. |image10| image:: /l10n_it_split_payment/static/description/fiscal_position.png
.. |image11| image:: /l10n_it_split_payment/static/description/SP.png
.. |image12| image:: /l10n_it_split_payment/static/description/SP2.png
.. |image13| image:: /l10n_it_split_payment/static/description/config.png
.. |image14| image:: /l10n_it_split_payment/static/description/invoice.png
   :target: https://travis-ci.org/zeroincombenze/l10n-italy

    <a href="https://www.gnu.org/licenses/lgpl.html"><img src="https://img.shields.io/badge/licence-LGPL--3-7379c3.svg"/></a>

   :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=10.0
.. |codecov| raw:: html

    <a href="https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0"><img src="https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0/graph/badge.svg"/></a>

.. |OCA project| raw:: html

    <a href="https://github.com/OCA/l10n-italy/tree/10.0"><img src="http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg"/></a>

.. |Tech Doc| raw:: html

    <a href="http://wiki.zeroincombenze.org/en/Odoo/10.0/dev"><img src="http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg"/></a>

.. |Help| raw:: html

    <a href="http://wiki.zeroincombenze.org/en/Odoo/10.0/man/FI"><img src="http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg"/></a>


    <a href="http://erp10.zeroincombenze.it"><img src="http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg"/></a>

.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :target: https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b
.. |ok| image:: https://www.gnu.org/licenses/lgpl.html"><img src="https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
.. |ok| raw:: html

   <i class="fa fa-check-square" style="font-size:24px;color:green"></i>
.. |No| raw:: html

   <i class="fa fa-minus-circle" style="font-size:24px;color:red"></i>

.. |menu| raw:: html

   <i class="fa fa-ellipsis-v" style="font-size:18px"></i>

.. |hand right| raw:: html

   <i class="fa fa-hand-o-right" style="font-size:12px"></i>

.. |warning| raw:: html

    <i class="fa fa-warning" style="font-size:24px;color:orange"></i>

.. |br| raw:: html

    <br/>

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
