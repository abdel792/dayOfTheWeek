# Wochentag #

* Autoren: Abdel, Noelia.
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]

Diese Erweiterung erlaubt Ihnen die Ermittlung des Wochentags für ein
angegebenes Datum.

Es fügt ein Untermenü im NVDA-Extras-Menü mit dem Namen "Wochentag" hinzu,
das 2 Einträge enthält:

* Der erste mit dem Namen "Tag suchen" öffnet einen Dialog bestehend aus 3
  Elementen:

    * Eine Liste, um das Datum einzugeben oder auszuwählen;
    * Ein OK-Schalter, der ein Meldungsfenster mit dem Wochentag zum
      betreffenden Datum anzeigt;
    * Einen Schalter "abbrechen", der den dialog schließt.

* Der zweite Eintrag mit dem Namen "Wochentag-Einstellungen" öffnet die
  Parameter der Erweiterung, um festzulegen, ob Beschriftungen für
  Datumsfelder gemelden werden sollen oder nicht. Der Dialog besteht aus
  folgenden Elementen:

    * Es wurde ein Konfigurationsdialogfeld hinzugefügt, um die
      Zugänglichkeit der Datumsauswahl zu aktivieren oder zu deaktivieren;
    * Ebene der Ankündigungen von Beschriftungen, bestehend aus 3
      Auswahlmöglichkeiten:

        * Lang (ist standardmäßig ausgewählt);
        * Kurz (für kurze Ankündigungen);
        * Aus (deaktiviert die Ankündigungen von Beschriftungen).

    * Aktiviert die Ankündigung des aktuellen Wertes für das Datumsfeld nur
      bei vertikaler Bewegung;
    * Ein OK-Schalter zum Speichern der Konfiguration;
    * Einen Schalter "abbrechen", der den dialog schließt.

## Anmerkungen ##

* Sie können diese Dialoge einfach durch Drücken der Escape-Taste schließen.
* Im Dialog "Eingaben" und genauer in der Kategorie "Wochentag" können Sie
  diesen Dialogen eine Tastenkombinationzuweisen;
* Wenn Sie NVDA 2018.2 oder höher verwenden, finden Sie im Extras-Menü nur
  einen Eintrag für die Suche nach Ihrem Tag, die zusätzlichen Einstellungen
  befinden sich im NVDA-Einstellungsfenster.

## Kompatibilität ##

* Diese Erweiterung ist kompatibel mit den NVDA-Versionen von 2014.3 bis
  2019.3.

## Änderungen in 19.02 ##

* Die Versionsnummerierung wurde in JJ.MM geändert (das Jahr in 2 Ziffern,
  gefolgt von einem Punkt, gefolgt von dem Monat in 2 Ziffern);
* Die Kompatibilität mit dem neuen Versionierungsformat der Erweiterung
  wurde gesichert, erschienen seit nvda 2019.1.

## Änderungen in 6.0 ##

* Die Einstellungen der Erweiterung zum NVDA-Einstellungsfenster für NVDA
  2018.2 und höher hinzugefügt;
* Das Element für die Suche nach einem Tag wurde in das Extras-Menü
  verschoben;
* Die Abwärtskompatibilität der Erweiterung mit den NVDA-Versionen vor
  2018.2, einschließlich des Einstellungsbereichs, wurde hinzugefügt.

## Änderungen in 5.0 ##

* Die Kompatibilität der Erweiterung mit wxPython 4.0 und Python3 wurde
  hinzugefügt;
* Ein Fehler wurde behoben, bei dem manche Pfade der Erweiterung
  Nicht-ASCII-Zeichen enthielten.

## Änderungen in 4.0 ##

* Die Erweiterung ist nun in der Lage, alle regionalen Datumsformate zu
  erkennen;
* Abwärtskompatibilität der Erweiterung mit den NVDA-Versionen vor 2016.4,
  die das Modul gui.guiHelper enthielten wurde hinzugefügt.

## Änderungen in 3.1 ##

* Zurück zum vorherigen Format für den Wochentag, weil es eine größere
  Anzahl von Sprachen erkennt;
* Die Zugänglichkeit der Datumsauswahl wurde verbessert, indem die 3 Felder
  "Tag", "Monat" und "Jahr" mit ihren jeweiligen Werten erkannt werden;
* Eine Modalität für die Integration der georgischen Sprache zur Erkennung
  der Wochentage wurde hinzugefügt;
* Es wurde ein Konfigurationsdialogfeld hinzugefügt, um die Zugänglichkeit
  der Datumsauswahl zu aktivieren oder zu deaktivieren;
* Das Erweiterungsuntermenü wurde von "Extras" nach "Einstellungen"
  verschoben;
* Die Erweiterungskategorie wurde in "Wochentag" geändert.

## Änderungen in 2.0 ##

* Nun wird das "gui.guiHelper-Modul" verwendet, um die korrekte Darstellung
  des Dialogfelds zu gewährleisten, welches nach dem Datum fragt;
* Die Erweiterung wurde unter der GPL lizenziert;
* Die Wochentage sind übersetzt worden, damit das Add-on ordnungsgemäß in
  den verschiedenen Sprachen funktioniert;
* Das Tagesformat wurde geändert, um Kodierungsfehler zu vermeiden.

## Änderungen in 1.0 ##

* Erstveröffentlichung.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
