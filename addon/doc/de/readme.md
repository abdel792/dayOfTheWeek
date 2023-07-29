# Wochentag #

* Autoren: Abdel, Noelia.
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]

Mit diesem Add-on können Sie einen Wochentag finden, der einem ausgewählten
Datum entspricht.

Es wird im NVDA-Menü unter "Werkzeuge" einen Eintrag mit dem Namen
"Wochentag" hinzugefügt, welches zwei Elemente enthält:

* Der erste mit der Suche nach dem Tag öffnet einen Dialog, der aus drei
  Steuerelementen besteht:

    * Ein Listenfeld zur Auswahl oder Eingabe des Datums;
    * Ein Dialogfeld mit dem Tag und der Schaltfläche "OK" anzeigt;
    * Eine Schaltfläche "Abbrechen", um das Dialogfeld zu schließen.

* Das zweite mit den Einstellungen für Wochentag öffnet die Parameter der
  Erweiterung, um anzugeben, ob Sie Beschriftungen für Datumsfelder
  mitgeteilt möchten oder nicht, es besteht aus den folgenden Elementen:

    * Es wurde ein Konfigurationsdialogfeld hinzugefügt, um die
      Zugänglichkeit der Datumsauswahl zu aktivieren oder zu deaktivieren;
    * Ebene der Ankündigungen von Beschriftungen, bestehend aus drei
      Auswahlmöglichkeiten:

        * Lang (dies ist die Standardeinstellung);
        * Kurz (für kurze Mitteilungen);
        * Aus (deaktiviert die Ankündigungen von Beschriftungen).

    * Aktiviert die Ankündigung des aktuellen Wertes für das Datumsfeld nur
      bei vertikaler Bewegung;
    * Ein Schalter "OK" zum Speichern der Konfiguration;
    * Einen Schalter "Abbrechen", zum Schließen des Dialogfelds.

## Anmerkungen ##

* Diese Dialogfelder können Sie einfach mit der Escape-Taste schließen;
* Sie können Tastenkombinationenzum für diese Dialogfelder im Menü für die
  Tastenbefehle öffnen und in der Kategorie "Wochentag" zuweisen;
* Wenn Sie NVDA 2018.2 oder neuer verwenden, finden Sie im Menü "Werkzeuge"
  nur einen Eintrag für die Suche nach dem Tag. Die Einstellungen für die
  Erweiterung befinden sich in den NVDA-Einstellungen.

## Kompatibilität ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Änderungen in 20230508.0.0 und neuer ##

* Die Versionsnummer, die minimale NVDA-Version und der Download-Link wurden
  entsprechend den Konventionen/Anforderungen für den Store für
  NVDA-Erweiterungen geändert.

## Änderungen in 19.02 ##

* Versionsnummerierung mit JJ.MM geändert (das Jahr in zwei Stellen, gefolgt
  von einem Punkt, gefolgt vom Monat in zwei Stellen);
* Die Kompatibilität mit dem neuen Versionierungsformat der Erweiterung
  wurde gesichert, erschienen seit nvda 2019.1.

## Änderungen in 6.0 ##

* Einstellungen der Erweiterung zum NVDA-Einstellungsfenster für NVDA 2018.2
  und neuer wurde hinzugefügt;
* Das Element für die Suche nach einem Tag wurde in das Menü "Werkzeuge"
  verschoben;
* Abwärtskompatibilität der Erweiterung mit den NVDA-Versionen vor 2018.2
  wurde hinzugefügt, die das Einstellungsfeld enthielten.

## Änderungen in 5.0 ##

* Kompatibilität des Add-Ons mit wxPython 4.0 und Python 3 wurde
  hinzugefügt;
* Ein Fehler mit Pfaden zur Erweiterung, die Nicht-ASCII-Zeichen enthalten,
  wurde behoben.

## Änderungen in 4.0 ##

* Die Erweiterung erkennt nun alle regionalen Datumsformate, die der
  Benutzer auswählen kann;
* Abwärtskompatibilität der Erweiterung mit den NVDA-Versionen vor 2016.4
  wurde hinzugefügt, die das Modul "gui.guiHelper" enthielten.

## Änderungen in 3.1 ##

* Zurück zum vorherigen Format für den Wochentag, da es die Erkennung einer
  größeren Anzahl von Sprachen ermöglicht;
* Verbesserte Zugänglichkeit der Datumsauswahl durch Erkennung der drei
  Felder "Tag", "Monat" und "Jahr" und deren Werte;
* Eine Technik zur Integration der georgischen Sprache zur Erkennung der
  Wochentage wurde hinzugefügt;
* Ein Konfigurationsdialogfeld wurde hinzugefügt, um die Zugänglichkeit der
  Datumsauswahl zu aktivieren oder zu deaktivieren;
* Das Untermenü der Erweiterung wurde von "Werkzeuge" nach "Einstellungen"
  verschoben;
* Die Erweiterungskategorie wurde in "Wochentag" geändert.

## Änderungen in 2.0 ##

* Verwendet das Modul "gui.guiHelper", um die korrekte Darstellung des
  Dialogfelds, der nach einem Datum fragt, sicherzustellen;
* GPL-Lizenz zur Erweiterung hinzugefügt;
* Die Wochentage sind übersetzt worden, damit die Erweiterung ordnungsgemäß
  in den verschiedenen Sprachen funktioniert;
* Das Tagesformat wurde geändert, um Kodierungsfehler zu vermeiden.

## Änderungen in 1.0 ##

* Erstveröffentlichung.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dayOfTheWeek

[2]: https://www.nvaccess.org/addonStore/legacy?file=dayOfTheWeek
