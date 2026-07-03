# Wochentag #

* Entwickler: Abdel, Noelia.

Diese Erweiterung ermöglicht es Ihnen, den Wochentag zu einem ausgewählten Datum zu finden.

Sie fügt ein Untermenü im NVDA-Menü "Werkzeuge" namens "Wochentag" hinzu, das 2 Einträge enthält:

* Der erste namens "Einen Tag suchen" öffnet einen Dialog, der aus 3 Steuerelementen besteht:

    * Ein Listenfeld zur Auswahl oder Eingabe Ihres Datums;
    * Eine "OK"-Schaltfläche zur Anzeige eines Meldungsfensters, das Ihren Tag enthält;
    * Eine "Abbrechen"-Schaltfläche zum Schliessen des Dialogs.

* Der zweite namens "Einstellungen der Wochentag-Erweiterung" öffnet die Parameter der Erweiterung, um festzulegen, ob Sie Beschriftungen für Datumsfelder angesagt bekommen möchten oder nicht. Er besteht aus folgenden Elementen:

    * Barrierefreiheit für die Datumsauswahl aktivieren;
    * Stufe der Ansagen von Beschriftungen, Sie haben dann 3 Auswahlmöglichkeiten:

        * Lang (dies ist die Standardeinstellung);
        * Kurz (für kurze Ansagen);
        * Aus (um Beschriftungsansagen zu deaktivieren).

    * Nur die Ansage des aktuellen Datumsfeldwerts beim vertikalen Bewegen aktivieren;
    * Eine "OK"-Schaltfläche zum Speichern Ihrer Konfiguration;
    * Eine "Abbrechen"-Schaltfläche zum Abbrechen und Schliessen des Dialogs.

## Hinweise ##

* Sie können diese Dialoge einfach durch Drücken der Eingabetaste (Escape) schliessen;
* Sie können eine Tastenkombination zum Öffnen dieser Dialoge im Menü "Eingaben" und genauer gesagt in der Kategorie "Wochentag" zuweisen;
* Wenn Sie NVDA 2018.2 oder höher verwenden, finden Sie nur einen Eintrag im Werkzeugmenü zur Suche Ihres Tages. Die Einstellungen der Erweiterung befinden sich dann im NVDA-Einstellungsmenü.

## Kompatibilität ##

* Diese Erweiterung ist mit den NVDA-Versionen von 2019.3 und höher kompatibel.

## Änderungen für 20240326.0.0

* Kompatibilität für nvda-2024.1. aktualisiert;
* Download-Link aus der Readme gelöscht, der Download-Link für zukünftige Updates wird nun nur noch über den Erweiterungs-Store verfügbar sein.

## Änderungen für 20231229.0.0 ##

* Eine abwärtskompatible Implementierung zur Unterstützung des Sprachmodus "auf Abruf" hinzugefügt, der bald mit nvda-2024.1. verfügbar sein wird.

## Änderungen für 20231015.0.0 ##

* Ein Fehler wurde behoben, der beim Navigieren mit der Pfeiltaste nach oben in der Datumsauswahl in den neuesten NVDA-Versionen auftrat.

## Änderungen für 20230728.0.0 ##

* Die flake8- und mypy-Regeln auf den Code angewendet;
* Die minimal unterstützte NVDA-Version auf 2019.3 geändert, um die in Python 3 eingeführten Annotationen zu unterstützen.

## Änderungen für 20230607.0.0 ##

* Die folgenden Arbeitsabläufe hinzugefügt:
 * auto-update-translations - zur automatischen Aktualisierung von Übersetzungen aus dem NVDA-Übersetzungssystem.
 * release-on-tag..yaml: zum Erstellen und Veröffentlichen der Erweiterung, sobald ein neuer Tag gepusht wird;
 * manual-release.yaml: zum manuellen Erstellen und Veröffentlichen neuer Versionen der Erweiterung.
* Übersetzungen aktualisiert.

## Änderungen für Version 20230508.0.0 und höher ##

* • Versionsnummer, minimale NVDA-Version und Download-Link entsprechend den Konventionen/Anforderungen des Stores geändert.

## Änderungen für 19.02 ##

* Versionsnummerierung auf JJ.MM geändert (Das Jahr in 2 Ziffern, gefolgt von einem Punkt, gefolgt vom Monat in 2 Ziffern);
* Kompatibilität mit dem neuen Versionsformat für Erweiterungen hinzugefügt, das seit nvda 2019.1. existiert.

## Änderungen für 6.0 ##

* Die Einstellungen der Erweiterung zum NVDA-Einstellungsmenü für NVDA 2018.2 und höher hinzugefügt;
* Den Eintrag zur Suche eines Tages in das Werkzeugmenü verschoben;
* Die Abwärtskompatibilität der Erweiterung mit den NVDA-Versionen vor 2018.2 hinzugefügt, die das Einstellungsmenü enthielten.

## Änderungen für 5.0 ##

* Kompatibilität der Erweiterung mit wxPython 4.0 und Python3 hinzugefügt;
* Ein Fehler mit Erweiterungspfaden behoben, die Nicht-ASCII-Zeichen enthalten.

## Änderungen für 4.0 ##

* Die Erweiterung ist nun in der Lage, alle regionalen Datumsformate zu erkennen, die der Benutzer auswählen kann;
* Die Abwärtskompatibilität der Erweiterung mit den NVDA-Versionen vor 2016.4 hinzugefügt, die das Modul gui.guiHelper enthielten.

## Änderungen für 3.1 ##

* Zurück zum vorherigen Format für den Wochentag, da es die Erkennung einer größeren Anzahl von Sprachen ermöglicht;
* Die Barrierefreiheit der Datumsauswahl mit Erkennung der 3 Felder 'Tag', 'Monat' und 'Jahr' und deren jeweiligen Werten verbessert;
* Eine Technik für die Integration der georgischen Sprache zur Erkennung der Wochentage hinzugefügt;
* Ein Konfigurationsdialogfeld zum Aktivieren oder Deaktivieren der Barrierefreiheit der Datumsauswahl hinzugefügt;
* Das Untermenü der Erweiterung von "Werkzeuge" nach "Einstellungen" verschoben;
* Die Kategorie der Erweiterung in "Wochentag" geändert.

## Änderungen für 2.0 ##

* Das Modul gui.guiHelper verwendet, um das korrekte Erscheinungsbild des Dialogs zu gewährleisten, der nach einem Datum fragt;
* Die GPL-Lizenz zur Erweiterung hinzugefügt;
* Die Wochentage wurden übersetzt, damit die Erweiterung in den verschiedenen Sprachen ordnungsgemäss funktioniert;
* Das Tagesformat geändert, um Kodierungsfehler zu vermeiden.

## Änderungen für 1.0 ##

* Erste Version.
