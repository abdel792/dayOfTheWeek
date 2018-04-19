# День недели #

*	 Авторы: Abdel, Noelia.
*	 Загрузить [стабильную версию][1]
*	 Загрузить [разрабатываемую версию][2]

Это дополнение позволяет определить день недели, соответствующий указанной
дате.

Он добавляет подменю в меню параметров NVDA "день недели", содержащий 2
пункта:


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


## Примечания ##

*	 Вы также можете закрыть эти диалоги, нажав клавишу Escape.
*	 Вы можете назначить горячие клавиши для открытия этих диалогов в разделе
   "Жесты ввода", перейдя в раздел "День недели".

## Изменения в версии 5.0 ##

*	 Добавлена совместимость дополнения с wxPython 4.0 и Python3;
*	 Исправлена ошибка с путями дополнения, которые содержат не-ASCII символы.

## Изменения в версии 4.0 ##

*	 The add-on is now able to recognize all the regional date formats that
   the user can choose;
*	 Added the backward compatibility of the add-on with the NVDA versions
   that preceded 2016.4, which included the gui.guiHelper module.

## Изменения в версии 3.1 ##

*	 Back to the previous format for the day of the week because it allows to
   recognize a greater number of languages;
*	 Improved the accessibility of the date selector with recognition of the 3
   fields 'Day', 'Month' and 'Year', and their respective values;
*	 Added a technique for the integration of the Georgian language for the
   recognition of the days of the week;
*	 Added a configuration dialog box to enable or disable the accessibility
   of the date selector;
*	 Moved the add-on submenu from "Tools" to "Preferences";
*	 Changed the add-on category to "Day of the week".

## Изменения в версии 2.0 ##

*	 Used the gui.guiHelper module to ensure the correct appearance of the
   dialog asking for a date;
*	 Для дополнения Добавлено лицензия GPL;
*	 Дни недели были переведены, так что дополнение работает правильно в
   разных языках;
*	 Изменился формат дня, чтобы избежать ошибок кодировки.

## Изменения в версии 1.0 ##

*	 Первая версия.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
