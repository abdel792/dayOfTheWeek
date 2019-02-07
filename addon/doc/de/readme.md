# Wochentag #

* Autoren: Abdel, Noelia.
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]

Diese Erweiterung erlaubt Ihnen die Ermittlung des Wochentags für ein
angegebenes Datum.

It adds a submenu in the NVDA Tools menu named "Day of the week", containing
2 items:

* The first one named "Search a day", opens a dialog composed of 3 controls:

    * A listbox to choose or type your date;
    * An "OK" button to display a messageBox containing your day;
    * einen Schalter "abbrechen", der den dialog schließt

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

## Anmerkungen ##

* You can close these dialogs just by pressing Escape.
* You can assign a shortcut to open these dialogs in "Input gestures" menu
  and, more precisely, in the "Day of the week" category.;
* Wenn Sie NVDA 2018.2 oder höher verwenden, finden Sie im Extras-Menü nur
  einen Eintrag für die Suche nach Ihrem Tag, die zusätzlichen Einstellungen
  befinden sich im NVDA-Einstellungsfenster.

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2014.3
  until 2019.1.

## Changes for 19.02 ##

* Changed version numbering using YY.MM (The year in 2 digits, followed by a
  dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Änderungen in 6.0 ##

* Die Einstellungen der Erweiterung zum NVDA-Einstellungsfenster für NVDA
  2018.2 und höher hinzugefügt.
* Das Element für die Suche nach einem Tag wurde in das Extras-Menü
  verschoben.
* Die Abwärtskompatibilität der Erweiterung mit den NVDA-Versionen vor
  2018.2, einschließlich des Einstellungsbereichs, wurde hinzugefügt.

## Änderungen in 5.0 ##

* Die Kompatibilität der Erweiterung mit wxPython 4.0 und Python3 wurde
  hinzugefügt.
* Ein Fehler wurde behoben, bei dem manche Pfade der Erweiterung
  Nicht-ASCII-Zeichen enthielten.

## Änderungen in 4.0 ##

* Die Erweiterung ist nun in der Lage, alle regionalen Datumsformate zu
  erkennen.
* Abwärtskompatibilität der Erweiterung mit den NVDA-Versionen vor 2016.4,
  die das Modul gui.guiHelper enthielten wurde hinzugefügt.

## Änderungen in 3.1 ##

* Zurück zum vorherigen Format für den Wochentag, weil es eine größere
  Anzahl von Sprachen erkennt.
* Die Zugänglichkeit der Datumsauswahl wurde verbessert, indem die 3 Felder
  "Tag", "Monat" und "Jahr" mit ihren jeweiligen Werten erkannt werden.
* Eine Modalität für die Integration der georgischen Sprache zur Erkennung
  der Wochentage wurde hinzugefügt.
* Es wurde ein Konfigurationsdialogfeld hinzugefügt, um die Zugänglichkeit
  der Datumsauswahl zu aktivieren oder zu deaktivieren.
* Das Erweiterungsuntermenü wurde von "Extras" nach "Einstellungen"
  verschoben.
* Die Erweiterungskategorie wurde in "Wochentag" geändert.

## Änderungen in 2.0 ##

* Nun wird das "gui.guiHelper-Modul" verwendet, um die korrekte Darstellung
  des Dialogfelds zu gewährleisten, welches nach dem Datum fragt.
* Die Erweiterung wurde unter der GPL lizenziert.
* Die Wochentage sind übersetzt worden, damit das Add-on ordnungsgemäß in
  den verschiedenen Sprachen funktioniert;
* Nun wird das Format "%w" für Daten verwendet, um Kodierungsfehler zu
  vermeiden. Zuvor wurde "%a" verwendet.

## Änderungen in 1.0 ##

* Erstveröffentlichung

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
