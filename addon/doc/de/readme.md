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

## Changes for 2.0 ##

*	 Used the gui.guiHelper module to ensure the correct appearance of the
   dialog asking for a date;
*	 Added the GPL license to the addon;
*	 Days of the week have been translated, so that the add-on works properly
   in the different languages;
*	 Used the %w format for the dates rather than %a to avoid encoding errors.

## Änderungen in Version 1.0 ##

*	 anfängliche Version

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=dw

[2]: http://addons.nvda-project.org/files/get.php?file=dw-dev
