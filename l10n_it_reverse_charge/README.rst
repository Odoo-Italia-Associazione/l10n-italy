[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=10.0)](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy)
[![license lgpl](https://img.shields.io/badge/licence-LGPL--3-7379c3.svg)](https://www.gnu.org/licenses/lgpl.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=10.0)](https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=10.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/10.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/10.0)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](https://erp10.zeroincombenze.it)




[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

|en|

================================
Reverse Charge Supplier Invoices
================================

Module to handle reverse charge VAT on supplier invoices.

|it|

Fatture fornitori con Reverse Charge

Il modulo permette di automatizzare le registrazioni contabili derivate
dalle fatture fornitori intra UE ed extra UE mediante il reverse charge
IVA. Inoltre è automatizzata la procedura di annullamento e riapertura
della fattura fornitore.

E' anche possibile utilizzare la modalità "con autofattura fornitore
aggiuntiva". Questo tipicamente è usato per i fornitori extra UE, con lo
scopo di mostrare, nel registro IVA acquisti, una fattura intestata alla
propria azienda, che verrà poi totalmente riconciliata con l'autofattura
attiva, sempre intestata alla propria azienda

**NOTA**: al momento è gestito solo il metodo **Autofattura** e non
quello **Integrazione IVA**.

Funzionalità, Certificati & Differenze da OCA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  ================================   ======   ====   ==========================================
  Funzione                           Status   OCA    Note
  ================================   ======   ====   ==========================================
  Fattura Reverse Charge Italia       |ok|    |ok|   Fatture da soggetti italiani
  Fattura Reverse Charge IntraUE      |ok|    |ok|   Fatture da fornitori UE
  RC con autofattura (ExtraUE)        |ok|    |ok|   Fatture da fornitori extra-UE
  Cancellazione fattura               |ok|    |ok|   Cancella anche le registrazioni collegate
  Fattura con RC + IVA [RCIVA]_.      |ok|    |No|   Separazione IVA RC da IVA ordinaria
  Proponi RC in fattura da cod.IVA    |ok|    |No|   Riconosce codici IVA Reverse Charge
  ================================   ======   ====   ==========================================


.. [RCIVA] Nel caso di fatture con IVA sia in Reverse Charge che ordinaria,
           in autofattura e ciroconto è riportata solo l'IVA in Reverse Charge.



Installation
------------

These instruction are just an example to remember what you have to do:
::

    $ ODOO\_DIR=/opt/odoo/10.0/l10n-italy # here your Odoo dir
    $ BACKUP\_DIR=/opt/odoo/backup # here your backup dir
    # Check for modules
    $ cd /tmp
    $ git clone https://github.com/zeroincombenze/l10n-italy.git l10n-italy
    $ mv $ODOO\_DIR/l10n-italy/l10n\_it\_reverse\_charge/ $BACKUP\_DIR/
    $ mv /tmp/l10n-italy/l10n\_it\_reverse\_charge/ $ODOO\_DIR/


Configuration
-------------

|it|

Creare l'imposta **22% intra UE** Vendita:

|image10|

Creare l'imposta **22% intra UE** Acquisti:

|image11|

    | alt
    | 22% intra UE Acqisti

    | width
    | 600 px

    Creare l'imposta **22% extra UE** Vendita:

|image12|

Creare l'imposta **22% extra UE** Acquisti:

|image13|

    | alt
    | 22% extra UE Acqisti

    | width
    | 600 px

    Creare il tipo reverse charge **Intra UE (autofattura)**:

|image14|

    | alt
    | reverse charge con Autofattura

    | width
    | 600 px

    Il sezionale autofattura deve essere di tipo 'vendita'

Creare il tipo reverse charge **Extra-EU (autofattura)** :

|image15|

    | alt
    | reverse charge con Autofattura

    | width
    | 600 px

    Il 'Sezionale autofattura passiva' deve essere di tipo 'acquisto'

Il 'Conto transitorio autofattura' va configurato come segue:

|image16|

    | alt
    | conto transitorio Autofattura

    | width
    | 600 px

    Il 'Sezionale pagamento autofattura' deve essere configurato con il
    'Conto transitorio autofattura':

|image17|

    | alt
    | Sezionale pagamento autofattura

    | width
    | 600 px

    Nella posizione fiscale, impostare il tipo reverse charge

|image18|

    | alt
    | Impostazione posizioni fiscali Intra CEE

    | width
    | 600 px

    |image19|

    | alt
    | Impostazione posizioni fiscali Extra CEE

    | width
    | 600 px


Usage
-----

=====

For furthermore information, please visit
http://wiki.zeroincombenze.org/it/Odoo/10.0/man/FI


Known issues / Roadmap
----------------------

Bug Tracker
-----------

Bugs are tracked on `GitHub
Issues <https://github.com/OCA/l10n-italy/issues>`__. In case of
trouble, please check there if your issue has already been reported. If
you spotted it first, help us smash it by providing detailed and
welcomed feedback.


Credits
-------

### Contributors

-  Davide Corio
-  Alex Comba alex.comba@agilebg.com
-  Lorenzo Battistini lorenzo.battistini@agilebg.com
-  Antonio Maria Vigliotti antoniomaria.vigliotti@gmail.com

### Funders

This module has been financially supported by

-  Agile BG https://www.agilebg.com/
-  SHS-AV s.r.l. https://www.zeroincombenze.it/

### Maintainer

|Odoo Italia Associazione|

| Odoo Italia is a nonprofit organization whose develops Italian
Localization for
| Odoo.

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
.. |image10| image:: /l10n_it_reverse_charge/static/description/tax_22_v_i_ue.png
.. |image11| image:: /l10n_it_reverse_charge/static/description/tax_22_a_i_ue.png
.. |image12| image:: /l10n_it_reverse_charge/static/description/tax_22_v_e_ue.png
.. |image13| image:: /l10n_it_reverse_charge/static/description/tax_22_a_e_ue.png
.. |image14| image:: /l10n_it_reverse_charge/static/description/rc_selfinvoice.png
.. |image15| image:: /l10n_it_reverse_charge/static/description/rc_selfinvoice_extra.png
.. |image16| image:: /l10n_it_reverse_charge/static/description/temp_account_auto_inv.png
.. |image17| image:: /l10n_it_reverse_charge/static/description/sezionale_riconciliazione.png
.. |image18| image:: /l10n_it_reverse_charge/static/description/fiscal_pos_intra.png
.. |image19| image:: /l10n_it_reverse_charge/static/description/fiscal_pos_extra.png
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :target: https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b
.. |ok| raw:: html

   <i class="fa fa-check-square" style="font-size:24px;color:green"></i>
.. |No| raw:: html

   <i class="fa fa-minus-circle" style="font-size:24px;color:red"></i>
.. |hand right| raw:: html

   <i class="fa fa-hand-o-right" style="font-size:12px"></i>

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







