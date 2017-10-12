# Day of the week #
*	 Authors: Abdel, Noelia.
*	 download [stable version][1]
*	 download [development version][2]

This add-on allows you to find a day of the week corresponding to a chosen date.

It adds a submenu in the NVDA Preferences menu named "Day of the week", containing 2 items:


*	The first one named "Search a day", opens a dialog composed of 3 controls:
	*	A listbox to choose or type your date;
	*	An "OK" button to display a messageBox containing your day;
	*	A "Cancel" button to close the dialog.
*	The second one named "dayOfTheWeek add-on settings" opens the parameters of the add-on to specify whether you want to report labels for date fields or not, it is composed of the following elements:
	*	Enable accessibility of the date selector;
	*	Level of the announces of labels, you will then have 3 choices:
		*	Long (it's the default choice);
		*	Short (for short announcements);
		*	Off (to disable labels announcements).
	*	Enable announcement of the current date field value only, when moving vertically;
	*	An "OK" button to save your configuration;
	*	A "Cancel" button to cancel and close the dialog.


## Notes ##

*	 You can close these dialogs just by pressing Escape.
*	 You can assign a shortcut to open these dialogs in "Input gestures" menu and, more precisely, in the "Day of the week" category.

## Changes for 4.0 ##

*	 The add-on is now able to recognize all the regional date formats that the user can choose.

## Changes for 3.1 ##

*	 Back to the old format for the day of the week because it allows to recognize a greater number of languages;
*	 Improved the accessibility of the date selector with recognition of the 3 fields 'Day', 'Month' and 'Year', and their respective values;
*	 Added a technique for the integration of the Georgian language for the recognition of the days of the week;
*	 Added a configuration dialog box to enable or disable the accessibility of the date selector;
*	 Moved the add-on submenu from "Tools" to "Preferences";
*	 Changed the add-on category to "Day of the week".

## Changes for 2.0 ##

*	 Used the gui.guiHelper module to ensure the correct appearance of the dialog asking for a date;
*	 Added the GPL license to the addon;
*	 Days of the week have been translated, so that the add-on works properly in the different languages;
*	 Used the %w format for the dates rather than %a to avoid encoding errors.

## Changes for 1.0 ##

*	 Initial version.

[1]: https://github.com/abdel792/dayOfTheWeek/releases/download/v4.0/dayOfTheWeek-4.0.nvda-addon

[2]: https://github.com/abdel792/dayOfTheWeek/releases/download/v4.0-dev/dayOfTheWeek-4.0-dev.nvda-addon
