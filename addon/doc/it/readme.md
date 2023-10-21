# Giorno della settimana #

* Autori: Abdel, Noelia.
* scarica la [versione stabile][1]
* scarica la [versione in sviluppo][2]

Questo componente aggiuntivo permette di conoscere il giorno della settimana
corrispondente a una data conosciuta.

Aggiunge un elemento nel menu strumenti di NVDA chiamato "Giorno della
settimana", contenente due elementi:

* Il primo, chiamato "Cerca un giorno", apre una finestra di dialogo
  composta da tre controlli:

    * Una casella elenco per selezionare o digitare la data desiderata;
    * Un pulsante "OK" per visualizzare un messaggio contenente il giorno
      della settimana;
    * Un pulsante annulla per chiudere la finestra.

* Il secondo, chiamato "impostazioni del componente aggiuntivo Giorno della
  Settimana", apre i parametri del componente, per specificare se si
  vogliono vocalizzare le etichette dei campi data o no; è composto dai
  seguenti elementi:

    * attiva l'accessibilità del selettore date;
    * Prolissità della vocalizzazione delle etichette; si avranno tre
      scelte:

        * Lunga (è la scelta predefinita);
        * Breve (per messaggi brevi);
        * Disattivato (per disabilitare la vocalizzazione delle etichette).

    * Attiva la vocalizzazione del solo valore del campo data corrente,
      quando ci si sposta verticalmente;
    * Un pulsante "OK" per salvare la configurazione;
    * Un pulsante annulla per annullare e chiudere la finestra.

## Note ##

* è possibile chiudere queste finestre semplicemente premendo esc;
* È possibile assegnare una combinazione di tasti per aprire queste finestre
  di dialogo nel menu "gesti e tasti di immissione" e, più precisamente,
  nella categoria  "Giorno della settimana";
* Se si utilizza NVDA 2018.2 o superiore, troverete solo una voce nel menu
  strumenti per la ricerca del giorno; le impostazioni del componente
  aggiuntivo verranno visualizzate nelle impostazioni di NVDA.

## Compatibilità ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20231015.0.0 ##

* Fixed a bug detected when navigating with up arrow from the date picker in
  the latest versions of NVDA.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Changes for 20230508.0.0 and beyond ##

* � Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.

## Novità nella versione 19.02 ##

* Cambiata la modalità di numerazione delle versioni; ora si utilizzano due
  cifre per l'anno, seguite da un punto, seguito da due cifre per il mese
  (aa.mm);
* Aggiunta la compatibilità con il nuovo formato per il numero di versione
  degli add-on, presente a partire da NVDA 2019.1.

## Novità nella versione 6.0 ##

* Integrate le impostazioni del componente  nella finestra impostazioni di
  NVDA 2018.2 e superiori;
* Spostata la voce per la ricerca del giorno nel menu strumenti;
* Mantenuta la compatibilità per versioni precedenti a NVDA 2018.2, che
  include la finestra impostazioni.

## Novità nella versione 5.0 ##

* Aggiunta compatibilità per wxPython 4 e Python 3;
* Risolto un bug con i percorsi che contengono caratteri non ASCII.

## Novità nella versione 4.0 ##

* L'add-on è ora in grado di riconoscere tutti i formati locali di data che
  l'utente può scegliere;
* Mantenuta la compatibilità per versioni precedenti a NVDA 2016.4, CHE
  include IL MODULO gui-HELPER.

## Novità nella versione 3.1 ##

* Riutilizzo del formato precedente per il giorno della settimana, CHE
  permette di riconoscere un numero maggiore di lingue;
* Migliorata l'accessibilità del selettore di data con il riconoscimento dei
  3 campi 'Giorno', 'Mese', 'Anno', e dei loro rispettivi valori;
* Aggiunta una tecnica di integrazione per il riconoscimento dei giorni
  della settimana nella lingua georgiana;
* Aggiunta una finestra di configurazione per attivare o disattivare
  l'accessibilità del selettore date;
* Spostato il sottomenu del componente aggiuntivo da strumenti a preferenze;
* Modificata la categoria dell'addon in "giorno della settimana".

## Novità nella versione 2.0 ##

* Introdotto il modulo gui.guiHelper per garantire il corretto aspetto della
  finestra di dialogo di richiesta di una data;
* Aggiunta la licenza GPL al componente;
* Sono stati tradotti i giorni della settimana, perciò il componente
  aggiuntivo funzionerà in più lingue.
* Modificato il formato del giorno per evitare errori di codifica.

## Novità nella versione 1.0 ##

* Versione iniziale.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dayOfTheWeek

[2]: https://www.nvaccess.org/addonStore/legacy?file=dayOfTheWeek
