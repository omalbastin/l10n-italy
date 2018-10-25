Fattura Elettronica + FatturaPA
===============================

Questo modulo gestisce l'infrastruttura per generare il file xml della Fattura 
Elettronica e della FatturaPA, versione 1.2, da trasmettere al sistema di interscambio SdI.

|warning| Lo schema di definizione dei file xml, pubblicato
con urn:www.agenziaentrate.gov.it:specificheTecniche è base per tutti i file
xml dell'Agenzia delle Entrate; come conseguenza nasce un conflitto tra
moduli diversi che riferiscono allo schema dell'Agenzia delle Entrate,
segnalato dall'errore:

|exclamation| name CryptoBinary used for multiple values in typeBinding

Tutti i moduli della localizzazione italiana che generano file xml dipendenti
dallo schema dell'Agenzia delle Entrate **devono** dichiare il modulo
`{{GIT_URL_ROOT}}/tree/{{branch}}/l10n_it_ade>`__ come dipendenza.

Per maggiori informazioni visitare il sito www.odoo-italia.org o contattare
l'ultimo autore: Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>.

Questo modulo sostituisce il il modulo l10n_it_fatturapa della distribuzione OCA.

|halt| Non installare questo modulo: è ancora in fase di sviluppo.