# Giorno della settimana #

* Sviluppatori: Abdel, Noelia.

Questo componente aggiuntivo consente di trovare il giorno della settimana corrispondente a una data scelta.

Aggiunge un sottomenu nel menu Strumenti di NVDA chiamato "Giorno della settimana", contenente 2 voci:

* La prima, denominata "Cerca un giorno", apre una finestra di dialogo composta da 3 controlli:

    * Una casella di riepilogo per scegliere o digitare la data;
    * Un pulsante "OK" per visualizzare una casella di messaggio contenente il giorno;
    * Un pulsante "Annulla" per chiudere la finestra di dialogo.

* La seconda, denominata "Impostazioni del componente aggiuntivo dayOfTheWeek", apre i parametri del componente aggiuntivo per specificare se si desidera o meno annunciare le etichette dei campi data, ed è composta dai seguenti elementi:

    * Attiva l'accessibilità del selettore di data;
    * Livello di annuncio delle etichette, avrai quindi 3 opzioni:

        * Lungo (è l'opzione predefinita);
        * Breve (per annunci brevi);
        * Disattivato (per disattivare gli annunci delle etichette).

    * Attiva l'annuncio del solo valore del campo data corrente, quando ci si sposta verticalmente;
    * Un pulsante "OK" per salvare la configurazione;
    * Un pulsante "Annulla" per annullare e chiudere la finestra di dialogo.

## Note ##

* È possibile chiudere queste finestre di dialogo semplicemente premendo Escape;
* È possibile assegnare una scorciatoia per aprire queste finestre di dialogo nel menu "Gesti di immissione" e, più precisamente, nella categoria "Giorno della settimana";
* Se usi NVDA 2018.2 o superiore, troverai solo una voce nel menu degli strumenti per cercare il giorno, e le impostazioni del componente aggiuntivo saranno nel pannello delle impostazioni di NVDA.

## Compatibilità ##

* Questo componente aggiuntivo è compatibile con le versioni di NVDA a partire dalla 2019.3 e successive.

## Modifiche per 20240326.0.0

* Aggiornata la compatibilità per nvda-2024.1.;
* Rimosso il collegamento per il download dal file readme, il collegamento per il download per i futuri aggiornamenti sarà ora disponibile solo nell'add-on store.

## Modifiche per 20231229.0.0 ##

* Aggiunta un'implementazione retrocompatibile per supportare la modalità di sintesi vocale su richiesta, che sarà presto disponibile con nvda-2024.1.

## Modifiche per 20231015.0.0 ##

* Corretto un errore rilevato durante la navigazione con la freccia su dal selettore di data nelle ultime versioni di NVDA.

## Modifiche per 20230728.0.0 ##

* Applicate le regole di flake8 e mypy al codice;
* Modificata la versione minima supportata di NVDA alla 2019.3 per supportare le annotazioni introdotte in Python 3.

## Modifiche per 20230607.0.0 ##

* Aggiunti i seguenti flussi di lavoro:
 * auto-update-translations - per aggiornare automaticamente le traduzioni dal sistema di traduzione di NVDA.
 * release-on-tag..yaml: per creare e pubblicare il componente aggiuntivo non appena viene inviato un nuovo tag;
 * manual-release.yaml: per creare e rilasciare manualmente nuove versioni del componente aggiuntivo.
* Traduzioni aggiornate.

## Modifiche per la versione 20230508.0.0 e successive ##

* • Modificato il numero di versione, la versione minima di NVDA e il collegamento per il download in conformità con le convenzioni/requisiti dello store.

## Modifiche per 19.02 ##

* Modificata la numerazione delle versioni utilizzando AA.MM (L'anno in 2 cifre, seguito da un punto, seguito dal mese in 2 cifre);
* Aggiunta la compatibilità con il nuovo formato di versione dei componenti aggiuntivi, apparso a partire da nvda 2019.1.

## Modifiche per 6.0 ##

* Aggiunte le impostazioni del componente aggiuntivo al pannello delle impostazioni di NVDA per NVDA 2018.2 e versioni successive;
* Spostata la voce per cercare un giorno nel menu strumenti;
* Aggiunta la retrocompatibilità del componente aggiuntivo con les versioni di NVDA precedenti alla 2018.2, che includevano il pannello delle impostazioni.

## Modifiche per 5.0 ##

* Aggiunta la compatibilità del componente aggiuntivo con wxPython 4.0 e Python3;
* Corretto un errore con i percorsi del componente aggiuntivo che contengono caratteri non ASCII.

## Modifiche per 4.0 ##

* Il componente aggiuntivo è ora in grado di riconoscere tutti i formati di data regionali che l'utente può scegliere;
* Aggiunta la retrocompatibilità del componente aggiuntivo con le versioni di NVDA precedenti alla 2016.4, che includevano il modulo gui.guiHelper.

## Modifiche per 3.1 ##

* Ritorno al formato precedente per il giorno della settimana perché consente di riconoscere un numero maggiore di lingue;
* Migliorata l'accessibilità del selettore di data con il riconoscimento dei 3 campi 'Giorno', 'Mese' e 'Anno' e dei rispettivi valori;
* Aggiunta una tecnica per l'integrazione della lingua georgiana per il riconoscimento dei giorni della settimana;
* Aggiunta una finestra di dialogo di configurazione per abilitare o disabilitare l'accessibilità del selettore di data;
* Spostato il sottomenu del componente aggiuntivo da "Strumenti" a "Preferenze";
* Modificata la categoria del componente aggiuntivo in "Giorno della settimana".

## Modifiche per 2.0 ##

* Utilizzato il modulo gui.guiHelper per garantire il corretto aspetto della finestra di dialogo che richiede una data;
* Aggiunta la licenza GPL al componente aggiuntivo;
* I giorni della settimana sono stati tradotti, in modo che il componente aggiuntivo funzioni correttamente nelle diverse lingue;
* Modificato il formato del giorno per evitare errori di codifica.

## Modifiche per 1.0 ##

* Versione iniziale.
