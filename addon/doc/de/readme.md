# Tag der Woche #

*	 Autoren: Abdel, Noelia.
*	 [stabile Version herunterladen][1]
*	 [Entwicklerversion herunterladen][2]

Diese Erweiterung erlaubt Ihnen die Ermittlung des Wochentags für ein
angegebenes Datum.

Es fügt ein Untermenü im NVDA-Einstellungsmenü mit dem Namen "Tag der Woche"
hinzu, das 2 Einträge enthält:


*	Das erste mit dem Namen "Suche nach einem Tag" öffnet einen Dialog, der aus 3 Steuerelementen besteht:
	-	Eine Listbox, um das Datum auszuwählen oder einzugeben; 
	-	Ein "Ok-Schalter", um eine Meldung anzuzeigen, die deinen Tag enthält; 
	-	Ein "Abbrechen-Schalter", um den Dialog zu schließen.
*	Das zweite mit dem Namen "Tag der Woche Einstellungen" öffnet die Parameter der Erweiterung. Hier kann angegeben werden, ob Sie Beschriftungen für Datumsfelder angesagt bekommen möchten oder nicht. Der Dialog besteht aus den folgenden Elementen:
	-	Zugänglichkeit des Auswahlschalters für das Datum aktivieren;
	-	Wenn Sie auf der Ebene der Ansagen von Beschriftungen sind, dann haben Sie 3 Möglichkeiten: 
		1.	Lang (Standardauswahl;
		2.	Kurz (für kurze Ansagen); 
		3.	Aus (um die Ansagen der Beschriftungen zu deaktivieren);
	-	Aktiviere die  Anzeige des aktuellen Wertes im Datumsfeld nur bei senkrechter Bewegung; 
	-	Ein "OK-Schalter", um die Konfiguration zu speichern; 
	-	Ein "Abbrechen-Schalter", um den Dialog abzubrechen und zu schließen.


## Anmerkungen ##

*	 Sie können den Dialog auch durch Drücken der Taste ESC schließen.
*	 Über den NVDA-Einstellungsdialog "Eingaben" können Sie
   Tastenkombinationen zuweisen, um diese Dialoge zu öffnen.

## Änderungen in V4.0 ##

*	 Die Erweiterung ist nun in der Lage, alle regionalen Datumsformate zu
   erkennen, die ausgewählt werden können;
*	 Abwärtskompatibilität der Erweiterung mit den NVDA-Versionen vor 2016.4,
   die das Modul gui.guiHelper enthielten wurde hinzugefügt.

## Änderungen in V3.1 ##

*	 Zurück zum vorherigen Format für den Wochentag, weil es erlaubt, eine
   größere Anzahl von Sprachen zu erkennen;
*	 Die Zugänglichkeit der Datumsauswahl wurde verbessert, indem die 3 Felder
   "Tag", "Monat" und "Jahr" mit ihren jeweiligen Werten erkannt werden;
*	 Eine Modalität für die Integration der georgischen Sprache zur Erkennung
   der Wochentage wurde hinzugefügt;
*	 Es wurde ein Konfigurationsdialogfeld hinzugefügt, um die Zugänglichkeit
   der Datumsauswahl zu aktivieren oder zu deaktivieren;
*	 Das Erweiterungsuntermenü wurde von "Extras" nach "Einstellungen"
   verschoben;
*	 Die Erweiterungskategorie wurde in "Tag der Woche" geändert.

## Änderungen bis 2.0 ##

*	 Nun wird das gui.guiHelper-Modul verwendet,um die korrekte Darstellung
   des Dialogfelds zu gewährleisten, welches nach dem Datum fragt.
*	 Die Erweiterung wurde unter der GPL lizensiert.
*	 Die Wochentage sind übersetzt worden, damit das Add-on ordnungsgemäß in
   den verschiedenen Sprachen funktioniert;
*	 Nun wird das Format %w für Daten verwendet, um Kodierungsfehler zu
   vermeiden. Zuvor wurde %a verwendet.

## Änderungen in Version 1.0 ##

*	 anfängliche Version

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=dw

[2]: http://addons.nvda-project.org/files/get.php?file=dw-dev
