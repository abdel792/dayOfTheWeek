# A hét napja #

*	 Fejlesztők: Abdel, Noelia.
*	 Letöltés [Stabil verzió][1]
*	 Letöltés [Fejlesztői verzió][2]

Ezzel a kiegészítővel meghatározhatja egy kiválasztott dátumhoz tartozó
napját a hétnek.

Hozzáadja az NVDA Eszközök menüjéhez A hét napja almenüt, ami 3 vezérlőből
álló párbeszédpanelt nyit meg:

*	 Egy listamező, ahová beírhatja, vagy kiválaszthatja a keresett dátumot.
*	 Egy Ok gomb, aminek a lenyomására megjelenik a keresett nap egy
   üzenetpanelen.
*	 Egy Mégse gomb, ami bezárja az ablakot.

## Megjegyzés ##
*	 A párbeszédpanelt az ESC gomb lenyomásával is bezárhatja.
*	 A Beviteli parancsok almenüben billentyűparancsot rendelhet a
   párbeszédpanel megnyitásához, az opció az Eszközök kategóriában
   található.

## Changes for 2.0 ##

*	 Used the gui.guiHelper module to ensure the correct appearance of the
   dialog asking for a date;
*	 Added the GPL license to the addon;
*	 Days of the week have been translated, so that the add-on works properly
   in the different languages;
*	 Used the %w format for the dates rather than %a to avoid encoding errors.

## Az 1.0 verzió változásai: ##

*	 Első kiadás

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
