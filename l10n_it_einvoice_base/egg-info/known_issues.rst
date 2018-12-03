|en| Please, do not mix the following module with OCA Italy modules.

This module may be conflict with some OCA modules with error:

|exclamation| name CryptoBinary used for multiple values in typeBinding


|it| Si consiglia di non mescolare i seguenti moduli con i moduli di OCA Italia.

Lo schema di definizione xml, pubblicato con
urn:www.agenziaentrate.gov.it:specificheTecniche è base per tutti i file
in formato xml da inviare all'Agenzia delle Entrate; come conseguenza
nasce un conflitto tra moduli diversi che utilizzano uno schema che riferisce 
all'urn dell'Agenzia delle Entrate, di cui sopra, segnalato dall'errore:

|exclamation| name CryptoBinary used for multiple values in typeBinding

* This module replaces l10n_it_fatturapa of OCA distribution.
* Do not use l10n_it_base module of OCA distribution
* Do not use l10n_it_split_payment module of OCA distribution
* Do not use l10n_it_reverse_charge of OCA distribution
* Do not install l10n_it_codici_carica module of OCA distribution
* Do not install l10n_it_fiscal_document_type module of OCA distribution
* Do not install l10n_it_fiscalcode_invoice module of OCA distribution
* Do not install l10n_it_ipa module of OCA distribution
* Do not install l10n_it_esigibilita_iva of OCA distribution