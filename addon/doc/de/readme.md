# Wochentag #

*	 Autoren: Abdel, Noelia.
*	 [Stabile Version herunterladen][1]
*	 [Entwicklerversion herunterladen][2]

Diese Erweiterung erlaubt Ihnen die Ermittlung des Wochentags für ein
angegebenes Datum.

Es fügt ein Untermenü im NVDA-Einstellungsmenü mit dem Namen "Wochentag"
hinzu, das 2 Einträge enthält:


*	Das erste mit dem Namen "Suche nach einem Tag" öffnet einen Dialog, der aus 3 Steuerelementen besteht:
	-	Eine Listbox, um das Datum auszuwählen oder einzugeben; 
	-	Ein "OK"-Schalter, um eine Meldung anzuzeigen, die den ausgewählten Tag enthält; 
	-	Ein "Abbrechen"-Schalter, um den Dialog zu schließen.
*	Das Zweite mit dem Namen "Tag der Woche Einstellungen" öffnet die Parameter der Erweiterung. Hier kann angegeben werden, ob Sie Beschriftungen für Datumsfelder angesagt bekommen möchten oder nicht. Der Dialog besteht aus den folgenden Elementen:
	-	Zugänglichkeit des Auswahlschalters für das Datum aktivieren;
	-	Wenn Sie auf der Ebene der Ansagen von Beschriftungen sind, dann haben Sie 3 Möglichkeiten: 
		1.	Lang (Standardauswahl)
		2.	Kurz (für kurze Ansagen)
		3.	Aus (um die Ansagen der Beschriftungen zu deaktivieren)
	-	Aktivieren der Anzeige des aktuellen Wertes im Datumsfeld nur bei senkrechter Bewegung.
	-	Ein "OK"-Schalter, um die Konfiguration zu speichern.
	-	Ein "Abbrechen"-Schalter, um den Dialog abzubrechen und zu schließen.

## Anmerkungen ##

*	 Sie können diese Dialoge einfach durch Drücken der Escape-Taste
   schließen.
*	 Im Menü "Eingabegesten" und genauer gesagt in der Kategorie "Wochentag"
   können Sie diesen Dialogen eine Verknüpfung zuweisen.
*	 Wenn Sie NVDA 2018.2 oder höher verwenden, finden Sie im Extras-Menü nur
   einen Eintrag für die Suche nach Ihrem Tag, die zusätzlichen
   Einstellungen befinden sich im NVDA-Einstellungsfenster.

## Änderungen in 6.0 ##

*	 Die Einstellungen der Erweiterung zum NVDA-Einstellungsfenster für NVDA
   2018.2 und höher hinzugefügt.
*	 Das Element für die Suche nach einem Tag wurde in das Extras-Menü
   verschoben.
*	 Die Abwärtskompatibilität der Erweiterung mit den NVDA-Versionen vor
   2018.2, einschließlich des Einstellungsbereichs, wurde hinzugefügt.

## Änderungen in 5.0 ##

*	 Die Kompatibilität der Erweiterung mit wxPython 4.0 und Python3 wurde
   hinzugefügt.
*	 Ein Fehler wurde behoben, bei dem manche Pfade der Erweiterung
   Nicht-ASCII-Zeichen enthielten.

## Änderungen in 4.0 ##

*	 Die Erweiterung ist nun in der Lage, alle regionalen Datumsformate zu
   erkennen.
*	 Abwärtskompatibilität der Erweiterung mit den NVDA-Versionen vor 2016.4,
   die das Modul gui.guiHelper enthielten wurde hinzugefügt.

## Änderungen in 3.1 ##

*	 Zurück zum vorherigen Format für den Wochentag, weil es eine größere
   Anzahl von Sprachen erkennt.
*	 Die Zugänglichkeit der Datumsauswahl wurde verbessert, indem die 3 Felder
   "Tag", "Monat" und "Jahr" mit ihren jeweiligen Werten erkannt werden.
*	 Eine Modalität für die Integration der georgischen Sprache zur Erkennung
   der Wochentage wurde hinzugefügt.
*	 Es wurde ein Konfigurationsdialogfeld hinzugefügt, um die Zugänglichkeit
   der Datumsauswahl zu aktivieren oder zu deaktivieren.
*	 Das Erweiterungsuntermenü wurde von "Extras" nach "Einstellungen"
   verschoben.
*	 Die Erweiterungskategorie wurde in "Wochentag" geändert.

## Änderungen in 2.0 ##

*	 Nun wird das "gui.guiHelper-Modul" verwendet, um die korrekte Darstellung
   des Dialogfelds zu gewährleisten, welches nach dem Datum fragt.
*	 Die Erweiterung wurde unter der GPL lizenziert.
*	 Die Wochentage sind übersetzt worden, damit das Add-on ordnungsgemäß in
   den verschiedenen Sprachen funktioniert;
*	 Nun wird das Format "%w" für Daten verwendet, um Kodierungsfehler zu
   vermeiden. Zuvor wurde "%a" verwendet.

## Änderungen in 1.0 ##

*	 Erstveröffentlichung

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
