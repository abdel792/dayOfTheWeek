# Giorno della settimana #

* Autori: Abdel, Noelia.
* Scarica la [versione stabile][1]
* Scarica la [versione in sviluppo][2]

Questo componente aggiuntivo permette di conoscere il giorno della settimana
a apartire da una data conosciuta.

It adds a submenu in the NVDA Tools menu named "Day of the week", containing
2 items:

* The first one named "Search a day", opens a dialog composed of 3 controls:

    * A listbox to choose or type your date;
    * An "OK" button to display a messageBox containing your day;
    * Un pulsante annulla per chiudere la finestra.

* The second one named "dayOfTheWeek add-on settings" opens the parameters
  of the add-on to specify whether you want to report labels for date fields
  or not, it is composed of the following elements:

    * Enable accessibility of the date selector;
    * Level of the announces of labels, you will then have 3 choices:

        * Long (it's the default choice);
        * Short (for short announcements);
        * Off (to disable labels announcements).

    * Enable announcement of the current date field value only, when moving
      vertically;
    * An "OK" button to save your configuration;
    * A "Cancel" button to cancel and close the dialog.

## Note ##

* You can close these dialogs just by pressing Escape;
* You can assign a shortcut to open these dialogs in "Input gestures" menu
  and, more precisely, in the "Day of the week" category;
* Se si utilizza NVDA 2018.2 o superiore, troverete solo una voce nel menu '
  strumenti per la ricerca del giorno, le impostazioni del componente
  aggiuntivo verranno visualizzate nelle impostazioni di NVDA. 

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2014.3
  until 2019.1.

## Changes for 19.02 ##

* Changed version numbering using YY.MM (The year in 2 digits, followed by a
  dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Modifiche per 5.0 ##

* Integrate le impostazioni del componente  al pannello delle impostazioni
  di NVDA 2018.2 e superiori; 
* Spostata la voce per la ricerca del giorno nel menu strumenti; 
* Mantenuta la compatibilità per versioni precedenti a NVDA 2018.2, che
  include il pannello delle impostazioni.

## Modifiche per 5.0 ##

* Aggiunta compatibilità per wxPython 4 e Python 3.
* Risolto un bug con i percorsi che contengono caratteri non ASCII. 

## Modifiche per 4.0 ##

* L'add-on è ora in grado di riconoscere tutti i formati regionali di data
  che l'utente può scegliere; 
* Mantenuta la compatibilità per versioni precedenti a NVDA 2016.4, CHE
  USANO IL MODULO gui-HELPER. 

## Modifiche per 3.1 ##

* Riutilizzo del formato precedente per il giorno della settimana, CHE
  permette di riconoscere un numero maggiore di lingue; 
* Migliorata l'accessibilità del selettore di data con il riconoscimento di
  3 campi, Giorno, 'Mese, Anno,, e i loro rispettivi valori; 
* Aggiunta una tecnica di integrazione per il riconoscimento dei giorni
  della settimana nella lingua georgiana; 
* Aggiunta una finestra di configurazione per attivare o disattivare
  l'accessibilità del selettore date.
* Spostato il sottomenu del componente aggiuntivo da strumenti a preferenze.
* Modificata la categoria dell'addon in "giorno della settimana".

## Modifiche per 2.0 ##

* Introdotto il modulo gui.guiHelper per garantire il corretto aspetto della
  finestra di dialogo;
* Aggiunta la licenza GPL al componente.
* Sono stati tradotti i giorni della settimana, così il componente
  aggiuntivo funzionerà in più lingue.
* Modificato il formato del giorno per evitare errori di codifica.

## Modifiche per 1.0 ##

* Versione iniziale.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
