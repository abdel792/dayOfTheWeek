# Day of the week #

* Authors: Abdel, Noelia.
* download [stable version][1]
* download [development version][2]

This add-on allows you to find a day of the week corresponding to a chosen date.

It adds a submenu in the NVDA Tools menu named "Day of the week", containing 2 items:

* The first one named "Search a day", opens a dialog composed of 3 controls:

    * A listbox to choose or type your date;
    * An "OK" button to display a messageBox containing your day;
    * A "Cancel" button to close the dialog.

* The second one named "dayOfTheWeek add-on settings" opens the parameters of the add-on to specify whether you want to report labels for date fields or not, it is composed of the following elements:

    * Enable accessibility of the date selector;
    * Level of the announces of labels, you will then have 3 choices:

        * Long (it's the default choice);
        * Short (for short announcements);
        * Off (to disable labels announcements).

    * Enable announcement of the current date field value only, when moving vertically;
    * An "OK" button to save your configuration;
    * A "Cancel" button to cancel and close the dialog.

## Notes ##

* You can close these dialogs just by pressing Escape;
* You can assign a shortcut to open these dialogs in "Input gestures" menu and, more precisely, in the "Day of the week" category;
* If you use NVDA 2018.2 or higher, you'll find only one item in the tool menu for searching your day, the add-on settings will be in the NVDA settings panel.

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3 and beyond.

## Changes for 20231015.0.0 ##

* Fixed a bug detected when navigating with up arrow from the date picker in the latest versions of NVDA.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support annotations introduced in Python 3.

## Changes for 20230607.0.0 ##

* Added the following workflows:
 * auto-update-translations - to automatically update translations from NVDA's translation system.
 * release-on-tag..yaml: to build and publish the addon as soon as a new tag is pushed;
 * manual-release.yaml: to build and release new versions of the add-on manually.
* Updated translations.

## Changes for version 20230508.0.0 and beyond ##

* • Changed version number, minimum NVDA version and download link according to store conventions/requirements.

## Changes for 19.02 ##

* Changed version numbering using YY.MM (The year in 2 digits, followed by a dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared since nvda 2019.1.

## Changes for 6.0 ##

* added the addon settings to the NVDA settings panel for NVDA 2018.2 and higher;
* Moved the item  for  searching a day to the tools menu;
* Added the backward compatibility of the add-on with the NVDA versions that preceded 2018.2, which included the settings panel.

## Changes for 5.0 ##

* Added the compatibility of the add-on with wxPython 4.0 and Python3;
* Fixed a bug with add-on paths that contain non-ASCII characters.

## Changes for 4.0 ##

* The add-on is now able to recognize all the regional date formats that the user can choose;
* Added the backward compatibility of the add-on with the NVDA versions that preceded 2016.4, which included the gui.guiHelper module.

## Changes for 3.1 ##

* Back to the previous format for the day of the week because it allows to recognize a greater number of languages;
* Improved the accessibility of the date selector with recognition of the 3 fields 'Day', 'Month' and 'Year', and their respective values;
* Added a technique for the integration of the Georgian language for the recognition of the days of the week;
* Added a configuration dialog box to enable or disable the accessibility of the date selector;
* Moved the add-on submenu from "Tools" to "Preferences";
* Changed the add-on category to "Day of the week".

## Changes for 2.0 ##

* Used the gui.guiHelper module to ensure the correct appearance of the dialog asking for a date;
* Added the GPL license to the addon;
* Days of the week have been translated, so that the add-on works properly in the different languages;
* Changed the day format to avoid encoding errors.

## Changes for 1.0 ##

* Initial version.

[1]: https://www.nvaccess.org/addonStore/legacy?file=dayOfTheWeek

[2]: https://www.nvaccess.org/addonStore/legacy?file=dayOfTheWeek
