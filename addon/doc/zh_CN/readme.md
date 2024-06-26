# 某天星期几 #

* 作者: Abdel, Noelia.

此插件允许您查找与所选日期对应的星期是星期几。

此插件在NVDA工具菜单中添加了一个名为“星期几”的子菜单，其中包含2个项目：

* 第一个名为“搜索一天”，打开一个由3个控件组成的对话框：

    * 用于选择或输入日期的列表框;
    * “确定”按钮，显示包含您一天的消息框;
    * “取消”按钮关闭对话框。

* 第二个名为 "dayoftheweek 插件设置" 的设置项将打开插件的参数, 以指定是否要朗读日期字段的标签, 它由以下元素组成:

    * 启用日期选择器的无障碍功能;
    * 标签朗读级别, 你将有3个选择:

        * 很长（这是默认选择）;
        * 短（读短标签）
        * 关闭（禁用标签朗读）。

    * 当垂直移动时，仅朗读启用当前日期字段值的通知;
    * 一个“确定”按钮，用于保存配置;
    * “取消”按钮取消并关闭对话框。

## 注意 ##

* 你可以按“Esc”来关闭这些对话框;
* 您可以在“输入手势”菜单中分配一个快捷手势来打开这些对话框，更确切地说，在“星期几”类别中指定一个快捷手势;
* 如果您使用NVDA 2018.2或更高版本，您只会在工具菜单中找到一个用于搜索当天的项目，插件设置将位于NVDA设置面板中。

## 兼容性 ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20240326.0.0

* Updated compatibility for nvda-2024.1.;
* Deleted download link from readme, the download link for future updates
  will now only be available from the add-on store.

## Changes for 20231229.0.0 ##

* Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Changes for 20231015.0.0 ##

* Fixed a bug detected when navigating with up arrow from the date picker in
  the latest versions of NVDA.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Changes for 20230508.0.0 and beyond ##

* Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.

## 19.02版的更改 ##

* 现在使用YY.MM形式的版本号（年份为2位数，后跟一个点，后跟月份为2位数）;
* 兼容nvda 2019.1的插件新版本格式。

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
* 将插件类别更改为“星期几”。

## 版本2.0 ##

* 使用gui.guiHelper模块确保对话框的正确外观和要求日期;
* 在插件中添加了GPL许可证;
* 已翻译了星期几，以便加载项在不同语言中正常工作;
* 更改了日期格式以避免编码错误。

## 版本1.0 ##

* 发布初始版本。

[[!tag dev stable]]
