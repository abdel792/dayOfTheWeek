# Tag der Woche #

*	 Autoren: Abdel, Noelia.
*	 [stabile Version herunterladen][1]
*	 [Entwicklerversion herunterladen][2]

Diese Erweiterung erlaubt Ihnen die Ermittlung des Wochentags für ein
angegebenes Datum.

Im Menü Extras von NVDA wird hierfür ein neuer Eintrag "Wochentag"
hinzugefügt. Dieser Eintrag öffnet ein Dialogfeld, das aus drei
Steuerelementen besteht

*	 Ein Datumsfeld um das Datum einzugeben oder auszuwählen.
*	 ein OK-Schalter, der ein Meldungsfenster mit dem Wochentag zum
   betreffenden Datum anzeigt.
*	 einen Schalter "abbrechen", der den dialog schließt

## Anmerkungen ##
*	 Sie können den Dialog auch durch Drücken der Taste ESC schließen.
*	 Über den NVDA-Einstellungsdialog "Eingaben" können Sie dem Dialog eine
   Tastenkombination zuweisen.

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
