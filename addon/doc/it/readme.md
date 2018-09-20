# Giorno della settimana #

*	 Autori: Abdel, Noelia.
*	 download [versione stabile][1]
*	 download [versione in sviluppo][2]

Questo componente aggiuntivo permette di conoscere il giorno della settimana
a apartire da una data conosciuta.

Aggiunge un elemento nel menu strumenti di NVDA chiamato "Giorno della
settimana", contenente due elementi:


*	The first one named "Search a day", opens a dialog composed of 3 controls:
	*	A listbox to choose or type your date;
	*	An "OK" button to display a messageBox containing your day;
	*	A "Cancel" button to close the dialog.
*	The second one named "dayOfTheWeek add-on settings" opens the parameters of the add-on to specify whether you want to report labels for date fields or not, it is composed of the following elements:
	*	Enable accessibility of the date selector;
	*	Level of the announces of labels, you will then have 3 choices:
		*	Long (it's the default choice);
		*	Short (for short announcements);
		*	Off (to disable labels announcements).
	*	Enable announcement of the current date field value only, when moving vertically;
	*	An "OK" button to save your configuration;
	*	A "Cancel" button to cancel and close the dialog.

## Note ##

*	 You can close these dialogs just by pressing Escape;
*	 You can assign a shortcut to open these dialogs in "Input gestures" menu
   and, more precisely, in the "Day of the week" category;
*	 If you use NVDA 2018.2 or higher, you'll find only one item in the tool
   menu for searching your day, the add-on settings will be in the NVDA
   settings panel.

## Changes for 6.0 ##

*	 added the addon settings to the NVDA settings panel for NVDA 2018.2 and
   higher;
*	 Moved the item for searching a day to the tools menu;
*	 Added the backward compatibility of the add-on with the NVDA versions
   that preceded 2018.2, which included the settings panel.

## Modifiche per 5.0 ##

*	 Added the compatibility of the add-on with wxPython 4.0 and Python3;
*	 Fixed a bug with add-on paths that contain non-ASCII characters.

## Modifiche per 4.0 ##

*	 L'add-on è ora in grado di riconoscere tutti i formati regionali di data
   che l'utente può scegliere; 
*	 Added the backward compatibility of the add-on with the NVDA versions
   that preceded 2016.4, which included the gui.guiHelper module.

## Modifiche per 3.1 ##

*	 Back to the previous format for the day of the week because it allows to
   recognize a greater number of languages;
*	 Improved the accessibility of the date selector with recognition of the 3
   fields 'Day', 'Month' and 'Year', and their respective values;
*	 Added a technique for the integration of the Georgian language for the
   recognition of the days of the week;
*	 Aggiunta una finestra di configurazione per attivare o disattivare
   l'accessibilità del selettore date.
*	 Spostato il sottomenu del componente aggiuntivo da strumenti a
   preferenze.
*	 Modificata la categoria dell'addon in "giorno della settimana".

## Modifiche per 2.0 ##

*	 Used the gui.guiHelper module to ensure the correct appearance of the
   dialog asking for a date;
*	 Aggiunta la licenza GPL al componente.
*	 Sono stati tradotti i giorni della settimana, così il componente
   aggiuntivo funzionerà in più lingue.
*	 Modificato il formato del giorno per evitare errori di codifica.

## Modifiche per 1.0 ##

*	 Versione iniziale.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
