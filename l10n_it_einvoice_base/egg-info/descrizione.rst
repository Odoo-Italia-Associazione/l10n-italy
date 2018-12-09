Fattura Elettronica + FatturaPA
-------------------------------

Questo modulo gestisce l'infrastruttura per generare il file xml della Fattura 
Elettronica e della FatturaPA, versione 1.2, da trasmettere al sistema di interscambio SdI.

In anagrafica clienti i dati per la fattura elettronica sono inseribili nella scheda "Agenzia delle Entrate".
Selezionare "Soggetto a fattura elettronica" se il cliente è soggetto alla fatturazione elettronica.
Se soggetto alla fatturazione elettronica occorre compilare il "Codice destinatario" o la "PEC".
Ai fini della fattura elettronica è obbligatoria la partita IVA.
Per fatturare un privato inserire il valore "0000000" nel codice destinatario e i codice fiscale.

Per la PA impostare "Pubblica Amministrazione" e compilare il "Codice ufficio".

Configurare le imposte riguardo a "Natura non imponibile", "Riferimento legisltativo" ed "Esigibilità IVA"

Configurare i dati della fattura elettronica nella configurazione della contabilità, dove necessario

::

    Destinatari:

Il modulo è destinato a tutte le aziende che dal 2019 dovranno emettere fattura elettronica


::

    Normativa:

Le leggi inerenti la fattura elettronica sono numerose. Potete consultare la `normativa fattura elettronica <https://www.fatturapa.gov.it/export/fatturazione/it/normativa/norme.htm>`__