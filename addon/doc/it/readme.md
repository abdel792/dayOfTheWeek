# Giorno della settimana #

*	 Autori: Abdel, Noelia.
*	 Scarica la [versione stabile][1]
*	 Scarica la [versione in sviluppo][2]

Questo componente aggiuntivo permette di conoscere il giorno della settimana
a apartire da una data conosciuta.

Aggiunge un elemento nel menu strumenti di NVDA chiamato "Giorno della
settimana", contenente due elementi:


*	Il primo "Scopri il giorno della settimana", apre una finestra di dialogo con tre controlli:
	*	Una casella per selezionare o digitare la data;
	*	Un pulsante "OK" per visualizzare il messaggio con il nome del giorno;
	*	Un pulsante "Annulla" per chiudere la finestra.
*	Il secondo chiamato "dayOfTheWeek add-on settings" apre i parametri del componente aggiuntivo per specificare se si desidera visualizzare  le etichette per i campi data, se è composto dai seguenti elementi:
	*	Attiva l'accessibilità del selettore data;
	*	Livello di annuncio delle etichette, ci sono  3 livelli disponibili:
		*	Lungo (di default);
		*	Corto(per un annuncio breve);
		*	Disattivo (disattiva la lettura delle etichette).
	*	Leggi solo il controllo del valore data selezionato, quando ci si sposta verticalmente;
	*	Un pulsante "OK" per salvare la configurazione;
	*	Un pulsante "Annulla" per annullare e chiudere la finestra.

## Note ##

*	 è possibile chiudere queste finestre semplicemente premendo esc.
*	 È possibile assegnare una combinazione di tasti per aprire queste
   finestre di dialogo nel menu "gesti e tasti di immissione" e, più
   precisamente, nella categoria  "Giorno della settimana".
*	 Se si utilizza NVDA 2018.2 o superiore, troverete solo una voce nel menu
   ' strumenti per la ricerca del giorno, le impostazioni del componente
   aggiuntivo verranno visualizzate nelle impostazioni di NVDA. 

## Modifiche per 5.0 ##

*	 Integrate le impostazioni del componente  al pannello delle impostazioni
   di NVDA 2018.2 e superiori; 
*	 Spostata la voce per la ricerca del giorno nel menu strumenti; 
*	 Mantenuta la compatibilità per versioni precedenti a NVDA 2018.2, che
   include il pannello delle impostazioni.

## Modifiche per 5.0 ##

*	 Aggiunta compatibilità per wxPython 4 e Python 3.
*	 Risolto un bug con i percorsi che contengono caratteri non ASCII. 

## Modifiche per 4.0 ##

*	 L'add-on è ora in grado di riconoscere tutti i formati regionali di data
   che l'utente può scegliere; 
*	 Mantenuta la compatibilità per versioni precedenti a NVDA 2016.4, CHE
   USANO IL MODULO gui-HELPER. 

## Modifiche per 3.1 ##

*	 Riutilizzo del formato precedente per il giorno della settimana, CHE
   permette di riconoscere un numero maggiore di lingue; 
*	 Migliorata l'accessibilità del selettore di data con il riconoscimento di
   3 campi, Giorno, 'Mese, Anno,, e i loro rispettivi valori; 
*	 Aggiunta una tecnica di integrazione per il riconoscimento dei giorni
   della settimana nella lingua georgiana; 
*	 Aggiunta una finestra di configurazione per attivare o disattivare
   l'accessibilità del selettore date.
*	 Spostato il sottomenu del componente aggiuntivo da strumenti a
   preferenze.
*	 Modificata la categoria dell'addon in "giorno della settimana".

## Modifiche per 2.0 ##

*	 Introdotto il modulo gui.guiHelper per garantire il corretto aspetto
   della finestra di dialogo;
*	 Aggiunta la licenza GPL al componente.
*	 Sono stati tradotti i giorni della settimana, così il componente
   aggiuntivo funzionerà in più lingue.
*	 Modificato il formato del giorno per evitare errori di codifica.

## Modifiche per 1.0 ##

*	 Versione iniziale.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
