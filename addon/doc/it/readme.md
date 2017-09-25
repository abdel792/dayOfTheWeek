# Giorno della settimana #

*	 Autori: Abdel, Noelia.
*	 download [versione stabile][1]
*	 download [versione in sviluppo][2]

Questo componente aggiuntivo permette di conoscere il giorno della settimana
a apartire da una data conosciuta.

Aggiunge un elemento nel menu strumenti di NVDA chiamato "Giorno della
settimana", che farà apparire  una finestra di dialogo composta da 3
controlli: 

*	 Una casella ad elenco per selezionare o digitare la data desiderata.
*	 Un pulsante "OK" per visualizzare un messaggio contenente il giorno. 
*	 Un pulsante annulla per chiudere la finestra.

## Note ##
*	 è possibile chiudere questa finestra semplicemente premendo esc.
*	 è possibile assegnare un tasto rapido per aprire la finestra di dialogo
   dal menu tasti e gesti di immissione, situato nelle preferenze di NVDA.

## Changes for 2.0 ##

*	 Used the gui.guiHelper module to ensure the correct appearance of the
   dialog asking for a date;
*	 Added the GPL license to the addon;
*	 Days of the week have been translated, so that the add-on works properly
   in the different languages;
*	 Used the %w format for the dates rather than %a to avoid encoding errors.

## Modifiche per 1.0 ##

*	 Versione iniziale.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
