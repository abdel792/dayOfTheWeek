# Day of the week #

* مطورو الإضافة: Abdel, Noelia.
* تحميل [الإصدار النهائي][1]
* تحميل [الإصدار التجريبي][2]

تتيح لك هذه الإضافةُ البرمجيةُ معرفةَ اليومِ المتعلقِ بتاريخٍ معين.

It adds a submenu in the NVDA Tools menu named "Day of the week", containing
2 items:

* The first one named "Search a day", opens a dialog composed of 3 controls:

    * A listbox to choose or type your date;
    * An "OK" button to display a messageBox containing your day;
    * وزر "إلغاء" لإغلاق المحاورة.

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

## ملاحظات ##

* You can close these dialogs just by pressing Escape;
* You can assign a shortcut to open these dialogs in "Input gestures" menu
  and, more precisely, in the "Day of the week" category;
* If you use NVDA 2018.2 or higher, you'll find only one item in the tool
  menu for searching your day, the add-on settings will be in the NVDA
  settings panel.

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Changes for 20230508.0.0 and beyond ##

* � Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.

## Changes for 19.02 ##

* Changed version numbering using YY.MM (The year in 2 digits, followed by a
  dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Changes for 6.0 ##

* added the addon settings to the NVDA settings panel for NVDA 2018.2 and
  higher;
* Moved the item for searching a day to the tools menu;
* Added the backward compatibility of the add-on with the NVDA versions that
  preceded 2018.2, which included the settings panel.

## Changes for 5.0 ##

* Added the compatibility of the add-on with wxPython 4.0 and Python3;
* Fixed a bug with add-on paths that contain non-ASCII characters.

## مستجدات الإصدار 4.0 ##

* يُمكِن للإضافة الآن أن تتعرفَ على جميع التنسيقات المتعلقة بالتاريخ التي قد
  يختارُها المستخدم;
* إضافةُ التوافق الخَلفي للإضافة البرمجية مع إصدارات NVDA التي سبقَت 2016.4
  التي شملت وحدة gui.guiHelper.

## مستجدات الإصدار 3.1 ##

* العودةُ إلى التنسيق السابق للتاريخ لأنهُ يُتيح إستخدام عدَدٍ أكبر من
  اللُغات;
* تحسينُ استعمال محدِّدِ التاريخ مع قارء الشاشة و ذلك بمنح إمكانية التعرف
  بشكلٍ جيد على كلٍ من الحقول : "يوم", "شهر" و "سنة" و مُحتوياتِها;
* إضافةُ تِقنِيَّةٍ لِدمجِ اللغة الجيورجية حتى تتعرفَ بشكلٍ جيد على أيام
  الأسبوع;
* إضافةُ صندوق إعدادات لتشغيل أو تعطيل إمكانيةِ استعمال مُحَدِّد التاريخ
  لمستعملي قارء الشاشة;
* نقلُ قائمةِ الإضافةِ البمجيةِ من "أدوات" إلى "تفضيلات";
* تغييرُ الفِءَةِ التي تنتمي إلَيها الإضافةُ البرمجيةُ إلى : "يوم الإسبوع".

## مستجدات الإصدار 2.0 ##

* إضافةُ إستعمال وحدةِ : "gui.guiHelper" و ذلك لضمان المظهر الصحيح لصناديق
  الإختيارات التي تقترحُها الإضافةُ البرمجية;
* إضافةُ ترخيص GPL للإضافةِ البرمجية;
* لقد عُرِضت أيام الأسبوع لِلترجمة و ذلك لِتُقرأَ بشكلٍ جيدْ مع اللغات
  المستعملة;
* تغييرُ تنسيقِ التاريخ و ذلك لتجنب الأخطاء المتعلقة بالترميز.

## مستجدات الإصدار 1.0 ##

* إصدار أولي

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dayOfTheWeek

[2]: https://www.nvaccess.org/addonStore/legacy?file=dayOfTheWeek
