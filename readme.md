# Day of the week #
*	 Authors: Abdel, Noelia.
*	 download [stable version][1]
*	 download [development version][2]

This add-on allows you to find a day of the week corresponding to a chosen date.

It adds an item in the NVDA Tools menu named "Day of the week", to open a dialog composed of 3 controls:

*	 A listbox to choose or type your date.
*	 An "OK" button to display a messageBox containing your day.
*	 A "Cancel" button to close the dialog.

## Notes ##
*	 You can close this dialog just by pressing Escape.
*	 You can assign a shortcut to open the dialog in "Input gestures" menu and, more precisely, in the "Tools" category.

## Changes for 3.0 ##

*	 Back to the %A format for the day of the week because it allows to recognize a greater number of languages;
*	 Improved the accessibility of the date selection with recognition of the 3 fields 'Day', 'Month' and 'Year'.

## Changes for 2.0 ##

*	 Used the gui.guiHelper module to ensure the correct appearance of the dialog asking for a date;
*	 Added the GPL license to the addon;
*	 Days of the week have been translated, so that the add-on works properly in the different languages.;
*	 Used the %w format for the dates rather than %a to avoid encoding errors.

## Changes for 1.0 ##

*	 Initial version.

[1]: https://github.com/abdel792/dayOfTheWeek/releases/download/v3.0-dev/dayOfTheWeek-3.0-dev.nvda-addon

[2]: https://github.com/abdel792/dayOfTheWeek/releases/download/v3.0-dev/dayOfTheWeek-3.0-dev.nvda-addon
