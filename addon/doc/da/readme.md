# Day of the week (Ugedag) #

* Forfattere: Abdel, Noelia.
* download [stabil version][1]
* download [udviklingsversion][2]

Med dette tilføjelsesprogram kan du finde den ugedag, som svarer til en
valgt dato.

It adds a submenu in the NVDA Tools menu named "Day of the week", containing
2 items:

* The first one named "Search a day", opens a dialog composed of 3 controls:

    * A listbox to choose or type your date;
    * An "OK" button to display a messageBox containing your day;
    * En Annuller-knap, som lukker dialogen.

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

## Noter ##

* You can close these dialogs just by pressing Escape.
* You can assign a shortcut to open these dialogs in "Input gestures" menu
  and, more precisely, in the "Day of the week" category.;
* Hvis du bruger NVDA 2018.2 eller nyere, finder du kun et punkt i
  værktøjsmenuen for at søge efter dage, og tilføjelsesindstillingerne er i
  NVDA-indstillingspanelet.

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2014.3
  until 2019.1.

## Changes for 19.02 ##

* Changed version numbering using YY.MM (The year in 2 digits, followed by a
  dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Ændringer i 6.0 ##

* tilføjede tilføjelsesindstillingerne til NVDA indstillingspanelet for NVDA
  2018.2 og nyere;
* Flyttet punktet til at søge en dag til værktøjsmenuen;
* Tilføjet bagudkompatibilitet for tilføjelsesprogrammet med NVDA versioner,
  der går forud for 2018.2, som omfatteder indstillingspanelet.

## Ændringer i 5.0 ##

* Tilføjet kompatibilitet af tilføjelsesprogrammet med wxPython 4.0 og
  Python3;
* Rettede en fejl med stier tilhørende tilføjelsespakken der indholder
  non-ASCII-tegn.

## Ændringer i4.0  ##

* Tilføjelsesprogrammet er nu i stand til at genkende alle de regionale
  datoformater, som brugeren kan vælge;
* Tilføjet bagudkompatibilitet for tilføjelsesprogrammet med NVDA versioner,
  der gik forud for 2016.4, som omfattede gui.guiHelper modul.

## Ændringer i 3.1 ##

* Tilbage til det tidligere format for Ugedag, fordi det giver mulighed for
  at genkende et større antal sprog;
* Forbedret tilgængelighed af dato selector med anerkendelsen af de 3 felter
  'Dag', 'Måned' og 'År', og deres respektive værdier;
* Tilføjet en teknik til integrering af det georgiske sprog for anerkendelse
  af dagene i ugen;
* Tilføjet en konfigurationsdialog for at aktivere eller deaktivere
  tilgængeligheden af datovælgeren;
* Flyttede tilføjelsespakkens undermenu fra "Værktøjer" til "Indstillinger";
* Ændret tilføjelsespakkens kategori til "Ugedag".

## Ændringer i 2.0 ##

* Brugt modulet gui.guiHelper for at sikre den korrekte udseende i
  dialogboksen der beder om en dato;
* Tilføjet GPL-licensen til tilføjelsen;
* Ugedag er blevet oversat, således at tilføjelsen virker korrekt på de
  forskellige sprog;
* Ændret dagsformat for at undgå kodningsfejl.

## Ændringer i 1.0 ##

* Første version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
