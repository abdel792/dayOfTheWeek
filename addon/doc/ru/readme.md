# Day of the week #

* Авторы: Abdel, Noelia.
* Загрузить [стабильную версию][1]
* Загрузить [разрабатываемую версию][2]

Это дополнение позволяет определить день недели, соответствующий указанной
дате.

It adds a submenu in the NVDA Tools menu named "Day of the week", containing
2 items:

* The first one named "Search a day", opens a dialog composed of 3 controls:

    * A listbox to choose or type your date;
    * An "OK" button to display a messageBox containing your day;
    * Кнопка "Cancel", чтобы закрыть этот диалог.

* The second one named "dayOfTheWeek add-on settings" opens the parameters
  of the add-on to specify whether you want to report labels for date fields
  or not, it is composed of the following elements:

    * Enable accessibility of the date selector;
    * Level of the announces of labels, you will then have 3 choices:

        * Long (it's the default choice);
        * Short (for short announcements);
        * Off (to disable labels announcements).

    * Enable announcement of the current date field value only, when moving
      vertically;
    * An "OK" button to save your configuration;
    * A "Cancel" button to cancel and close the dialog.

## Примечания ##

* Вы также можете закрыть эти диалоги, просто нажав клавишу Escape.
* Вы можете назначить горячие клавиши для открытия этих диалогов в разделе
  "Жесты ввода", перейдя в раздел "День недели".
* If you use NVDA 2018.2 or higher, you'll find only one item in the tool
  menu for searching your day, the add-on settings will be in the NVDA
  settings panel.

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2014.3
  until 2019.1.

## Изменения в версии 19.02 ##

* Changed version numbering using YY.MM (The year in 2 digits, followed by a
  dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Изменения в версии 6.0 ##

* added the addon settings to the NVDA settings panel for NVDA 2018.2 and
  higher;
* Moved the item for searching a day to the tools menu;
* Added the backward compatibility of the add-on with the NVDA versions that
  preceded 2018.2, which included the settings panel.

## Изменения в версии 5.0 ##

* Добавлена совместимость дополнения с wxPython 4.0 и Python3;
* Исправлена ошибка с путями дополнения, которые содержат не-ASCII символы.

## Изменения в версии 4.0 ##

* The add-on is now able to recognize all the regional date formats that the
  user can choose;
* Added the backward compatibility of the add-on with the NVDA versions that
  preceded 2016.4, which included the gui.guiHelper module.

## Изменения в версии 3.1 ##

* Back to the previous format for the day of the week because it allows to
  recognize a greater number of languages;
* Improved the accessibility of the date selector with recognition of the 3
  fields 'Day', 'Month' and 'Year', and their respective values;
* Added a technique for the integration of the Georgian language for the
  recognition of the days of the week;
* Added a configuration dialog box to enable or disable the accessibility of
  the date selector;
* Moved the add-on submenu from "Tools" to "Preferences";
* Changed the add-on category to "Day of the week".

## Изменения в версии 2.0 ##

* Used the gui.guiHelper module to ensure the correct appearance of the
  dialog asking for a date;
* Для дополнения Добавлено лицензия GPL;
* Дни недели были переведены, так что дополнение работает правильно в разных
  языках;
* Изменился формат дня, чтобы избежать ошибок кодировки.

## Изменения в версии 1.0 ##

* Первая версия.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
