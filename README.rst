
================================
|Zeroincombenze| l10n-italy 10.0
================================

|Maturity| |Build Status| |Coverage Status| |Codecov Status| |license gpl| |Tech Doc| |Help| |Try Me|

.. contents::


Overview / Panoramica
=====================

|en| Italian Localization

|it| Localizzazione Italiana

La localizzazione italiana comprende moduli per la gestione delle principali
incombenze fiscali che le imprese italiane devono gestire.

Sono coperte le aree:

* Stampa registri IVA
* Stampa libro giornale
* Registrazione fatture fornitori con RA
* FatturaPA
* Fattura Elettronica B2B (in fase di sviluppo)
* Gestione DdT
* Data di registrazione fatture fornitori
* Gestione Ricevute Bancarie
* Split payment
* Documenti con Reverse Charge

Avaiable Addons / Moduli disponibili
------------------------------------

+--------------------------------------+------------+------------+----------------------------------------------------+
| Name / Nome                          | Version    | OCA Ver.   | Description / Descrizione                          |
+--------------------------------------+------------+------------+----------------------------------------------------+
| account_central_journal              | |no_check| | |halt|     | Account Central Journal                            |
+--------------------------------------+------------+------------+----------------------------------------------------+
| account_fiscal_year_closing          | |halt|     | |no_check| | Fiscal Year Closing                                |
+--------------------------------------+------------+------------+----------------------------------------------------+
| account_invoice_entry_date           | 10.0.0.1.0 | |halt|     | Account Invoice entry Date                         |
+--------------------------------------+------------+------------+----------------------------------------------------+
| account_invoice_report_ddt_group     | 10.0.0.3.1 | |same|     | Account invoice report grouped by DDT              |
+--------------------------------------+------------+------------+----------------------------------------------------+
| account_invoice_sequential_dates     | |halt|     | |halt|     | Check invoice date consistency                     |
+--------------------------------------+------------+------------+----------------------------------------------------+
| account_vat_period_end_statement     | 10.0.1.4.2 | |same|     | Period End VAT Statement                           |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_eu_trial_balance                | |halt|     | |no_check| | 2013/34/EU - Trial Balance + Financial Statements  |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_CEE_balance_generic          | |halt|     | |halt|     | Italy - 4th EU Directive - Consolidation Chart of  |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_abicab                       | 10.0.1.0.0 | |same|     | Base Bank ABI/CAB codes                            |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_account                      | 10.0.1.0.1 | 10.0.1.2.3 | Italian Localization - Account                     |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_account_tax_kind             | |no_check| | 10.0.1.0.0 | Italian Localisation - Natura delle aliquote IVA   |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_ade                          | 10.0.0.1.1 | |no_check| | Codice e definizioni come da Agenzia delle Entrate |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_ateco                        | 10.0.1.0.0 | |same|     | Ateco codes                                        |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_base                         | 10.0.0.2.1 | |no_check| | Italian Localisation - Base                        |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_base_crm                     | |halt|     | |halt|     | Italian Localisation - CRM                         |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_base_location_geonames_impor | 10.0.1.0.0 | |same|     | Import base_location entries (provinces) from Geon |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_bill_of_entry                | |halt|     | |halt|     | Italian Localisation - Bill of Entry               |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_causali_pagamento            | |no_check| | 10.0.1.0.0 | Aggiunge la tabella delle causali di pagamento da  |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_central_journal              | 10.0.0.0.1 | |same|     | Italian Localization - Account central journal     |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_codici_carica                | |no_check| | 10.0.1.0.0 | Aggiunge la tabella dei codici carica da usare nei |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_corrispettivi                | 10.0.1.1.0 | 10.0.1.2.2 | Italian Localization - Corrispettivi               |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_corrispettivi_sale           | |no_check| | 10.0.1.0.1 | Modulo per integrare i corrispettivi in odoo con g |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_ddt                          | 10.0.1.5.1 | 10.0.1.7.1 | Documento di Trasporto                             |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_einvoice_base                | 10.0.2.1.1 | |no_check| | Infrastructure for Italian Electronic Invoice + Fa |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_einvoice_out                 | 10.0.1.0.0 | |no_check| | Electronic invoices emission                       |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_esigibilita_iva              | 10.0.1.0.0 | |same|     | Esigibilità IVA                                    |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_fatturapa                    | |no_check| | 10.0.2.2.2 | Electronic invoices                                |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_fatturapa_in                 | |no_check| | 10.0.1.2.1 | Electronic invoices reception                      |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_fatturapa_in_purchase        | |no_check| | 10.0.1.0.0 | Fattura Elettronica - Purchase integration         |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_fatturapa_out                | |no_check| | 10.0.1.2.3 | Electronic invoices emission                       |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_fatturapa_out_ddt            | |no_check| | 10.0.1.0.2 | Bridge module                                      |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_fatturapa_pec                | |no_check| | 10.0.1.2.0 | Send electronic invoices via PEC                   |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_fiscal                       | 10.0.0.2.0 | |no_check| | Italy - Fiscal localization by zeroincombenze(R)   |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_fiscal_document_type         | |halt|     | |same|     | Italian Localization - Tipi di documento fiscali p |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_fiscal_ipa                   | 10.0.1.1.0 | |no_check| | IPA Code and Destination Code in Partner Record    |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_fiscal_payment_term          | 10.0.1.0.0 | |same|     | Electronic & Fiscal invoices payment               |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_fiscalcode                   | 10.0.1.0.2 | 10.0.1.1.0 | Italian Localisation - Fiscal Code                 |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_fiscalcode_invoice           | 10.0.1.0.0 | |same|     | Italian Fiscal Code in invoice PDF                 |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_ipa                          | |no_check| | 10.0.2.0.0 | IPA Code (IndicePA)                                |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_location_nuts                | |no_check| | 10.0.1.0.0 | NUTS specific options for Italy                    |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_partially_deductible_vat     | |halt|     | |halt|     | Italy - Partially Deductible VAT                   |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_pec                          | 10.0.1.0.0 | |same|     | Pec Mail                                           |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_prima_nota_cassa             | |halt|     | |halt|     | Italian Localisation - Prima Nota Cassa            |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_rea                          | 10.0.1.0.1 | 10.0.1.1.0 | Manage fields for  Economic Administrative catalog |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_reverse_charge               | 10.0.1.1.1 | 10.0.1.1.3 | Reverse Charge for Italy                           |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_riba_commission              | |halt|     | |same|     | Ricevute bancarie & commissioni                    |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_ricevute_bancarie            | 10.0.1.1.0 | 10.0.1.2.0 | Ricevute Bancarie                                  |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_sdi_channel                  | |no_check| | 10.0.1.1.0 | Add channel to send-receice xml files to SdI.      |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_split_payment                | 10.0.1.0.2 | 10.0.1.1.0 | Split Payment                                      |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_vat_communication            | |halt|     | |no_check| | Comunicazione periodica IVA                        |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_vat_registries               | 10.0.1.2.2 | |same|     | Italian Localization - VAT Registries              |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_vat_registries_cash_basis    | 10.0.1.0.0 | |same|     | Italian Localization - VAT Registries - Cash Basis |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_vat_registries_split_payment | |no_check| | 10.0.1.0.0 | Bridge module to make VAT registries work with Spl |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_website_sale_corrispettivi   | |halt|     | 10.0.1.1.1 | Italian localization - Website Sale Corrispettivi  |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_website_sale_fiscalcode      | 10.0.1.0.1 | |same|     | Website Sale FiscalCode                            |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_withholding_tax              | 10.0.1.2.2 | 10.0.1.2.3 | Italian Withholding Tax                            |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_withholding_tax_causali      | |no_check| | 10.0.1.0.0 | Causali pagamento per ritenute d'acconto           |
+--------------------------------------+------------+------------+----------------------------------------------------+
| l10n_it_withholding_tax_payment      | 10.0.1.1.0 | |same|     | Italian Withholding Tax Payment                    |
+--------------------------------------+------------+------------+----------------------------------------------------+
| multibase_plus                       | 10.0.0.1.3 | |no_check| | Enhanced Odoo Features                             |
+--------------------------------------+------------+------------+----------------------------------------------------+


OCA comparation / Confronto con OCA
-----------------------------------

+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
| Description / Descrizione            | Odoo Italia      | OCA             | Notes / Note                                                                       |
+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
| Gestione evoluta anagrafiche         | |check|          | |no_check|      | `l10n_it_base <https://github.com/zeroincombenze/l10n-italy/tree/8.0/l10n_it_base> |
+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
| Piano dei conti evoluto              | |check|          | |no_check|      |                                                                                    |
+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
| Codici IVA completi                  | |check|          | |no_check|      |                                                                                    |
+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
| Validazione Codice Fiscale           | |check|          | |no_check|      |                                                                                    |
+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+



Getting started / Come iniziare
===============================

|Try Me|


Prerequisites / Prerequisiti
----------------------------


* python
* postgresql 9.2+

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
| /opt/odoo/10.0/l10n-italy/                                                 |
+----------------------------------------------------------------------------+

::

    cd $HOME
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    export PATH=$HOME/dev:$PATH
    odoo_install_repository l10n-italy -b 10.0 -O zero
    for pkg in os0 z0lib; do
        pip install $pkg -U
    done
    sudo manage_odoo requirements -b 10.0 -vsy -o /opt/odoo/10.0


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

    odoo_install_repository l10n-italy -b 10.0 -O zero -U
    # Adjust following statements as per your system
    sudo systemctl restart odoo


Support / Supporto
------------------


|Zeroincombenze| This module is maintained by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__ and free support is supplied through `Odoo Italia Associazione Forum <https://odoo-italia.org/index.php/kunena/recente>`__



Get involved / Ci mettiamo in gioco
===================================

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/zeroincombenze/l10n-italy/issues>`_.

In case of trouble, please check there if your issue has already been reported.

Proposals for enhancement
-------------------------


|en| If you have a proposal to change this module, you may want to send an email to <cc@shs-av.com> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.

|it| Se hai proposte per migliorare questo modulo, puoi inviare una mail a <cc@shs-av.com> per un iniziale contatto.

Credits / Titoli di coda
========================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


----------------


|en| **zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes ready-to-use **Odoo** on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://wiki.zeroincombenze.org/en/Odoo>`__
is mainly designed to cover Italian law and markeplace.

|it| **zeroincombenze®** è un marchio registrato di `SHS-AV s.r.l. <https://www.shs-av.com/>`__
che distribuisce e promuove **Odoo** pronto all'uso sullla propria infrastuttura.
La distribuzione `Zeroincombenze® è progettata per le esigenze del mercato italiano.


|chat_with_us|


|

Last Update / Ultimo aggiornamento: 2018-12-03

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=10.0
    :target: https://travis-ci.org/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=10.0
    :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=10.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0/graph/badge.svg
    :target: https://codecov.io/gh/OCA/l10n-italy/branch/10.0
    :alt: Codecov
.. |OCA project| image:: Unknown badge-OCA
    :target: https://github.com/OCA/l10n-italy/tree/10.0
    :alt: OCA
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/10.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/10.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg
    :target: https://erp10.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov Status| image:: https://codecov.io/gh/OCA/l10n-italy/branch/10.0/graph/badge.svg
    :target: https://codecov.io/gh/OCA/l10n-italy/branch/10.0
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
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/Desktoptelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/fatturapa.md
.. |chat_with_us| image:: https://www.shs-av.com/wp-content/chat_with_us.gif
   :target: https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b
