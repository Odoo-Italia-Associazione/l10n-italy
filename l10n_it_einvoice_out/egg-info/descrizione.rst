Fattura Elettronica + FatturaPA
===============================

Questo modulo permette di generare il file xml della fatturaPA versione 1.2
da trasmettere al sistema di interscambio SdI.

::

    Destinatari:

Il modulo è destinato a tutte le aziende che dal 2019 dovranno emettere fattura elettronica


::

    Normativa:

Le leggi inerenti la fattura elettronica sono numerose. Potete consultare la `normativa fattura elettronica <https://www.fatturapa.gov.it/export/fatturazione/it/normativa/norme.htm>`__


|warning| Lo schema di definizione dei file xml, pubblicato
con urn:www.agenziaentrate.gov.it:specificheTecniche è base per tutti i file
xml dell'Agenzia delle Entrate; come conseguenza nasce un conflitto tra
moduli diversi che riferiscono allo schema dell'Agenzia delle Entrate,
segnalato dall'errore:

|exclamation| **name CryptoBinary used for multiple values in typeBinding**

Tutti i moduli della localizzazione italiana che generano file xml dipendenti
dallo schema dell'Agenzia delle Entrate **devono** dichiare il modulo
`l10n_it_ade <../l10n_it_ade>`__ come dipendenza.

Per maggiori informazioni visitare il sito www.odoo-italia.org o contattare
l'ultimo autore: Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>.

|halt| Non utilizzare ancora questo modulo in produzione: alpha release soggetta
ad ulteriori modifiche