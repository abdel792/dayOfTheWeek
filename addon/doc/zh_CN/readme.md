# 某天星期几 #

* 作者: Abdel, Noelia.
* 下载 [稳定版][1]
* 下载 [开发板][2]

此插件允许您查找与所选日期对应的星期是星期几。

It adds a submenu in the NVDA Tools menu named "Day of the week", containing
2 items:

* The first one named "Search a day", opens a dialog composed of 3 controls:

    * A listbox to choose or type your date;
    * An "OK" button to display a messageBox containing your day;
    * A "Cancel" button to close the dialog.

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

## 注意 ##

* You can close these dialogs just by pressing Escape.
* You can assign a shortcut to open these dialogs in "Input gestures" menu
  and, more precisely, in the "Day of the week" category.;
* 如果您使用NVDA 2018.2或更高版本，您只会在工具菜单中找到一个用于搜索当天的项目，插件设置将位于NVDA设置面板中。

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2014.3
  until 2019.1.

## Changes for 19.02 ##

* Changed version numbering using YY.MM (The year in 2 digits, followed by a
  dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## 版本6.0 ##

* 将插件设置添加到NVDA 2018.2及更高版本的NVDA通用设置面板中;
* 将用于搜索一天的项目移动到工具菜单;
* 添加了插件与2018.2之前的NVDA版本的向后兼容性支持，其中包括设置面板。

## 版本5.0 ##

* 添加了插件与wxPython 4.0和Python3的支持;
* 修复了包含非ASCII字符的附加路径的错误。

## 版本4.0 ##

* 该插件现在能够识别用户可以选择的所有区域日期格式;
* 添加了插件与2016.4之前的NVDA版本的向后兼容性，其中包括gui.guiHelper模块。

## 版本3.1 ##

* 恢复到星期几的先前格式，因为它允许识别更多语言;
* 改进了日期选择器的可访问性，识别了3个字段'Day'，'Month'和'Year'，以及它们各自的值;
* 增加了一种整合格鲁吉亚语的技术，以表彰一周的日子;
* 添加了配置对话框以启用或禁用日期选择器的辅助功能;
* 将附加子菜单从“工具”移动到“首选项”;
* 将附加组件类别更改为“星期几”。

## 版本2.0 ##

* 使用gui.guiHelper模块确保对话框的正确外观和要求日期;
* 在插件中添加了GPL许可证;
* 已翻译了星期几，以便加载项在不同语言中正常工作;
* 更改了日期格式以避免编码错误。

## 版本1.0 ##

* 发布初始版本。

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
