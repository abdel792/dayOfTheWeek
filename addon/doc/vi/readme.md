# Ngày của tuần #

* Tác giả: Abdel, Noelia.
* tải về [phiên bản chính thức][1]
* tải về [phiên bản thử nghiệm][2]

Add-on này cho phép bạn tìm kiếm ngày trong tuần căn cứ theo này đã chọn.

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

## Lưu ý ##

* You can close these dialogs just by pressing Escape.
* You can assign a shortcut to open these dialogs in "Input gestures" menu
  and, more precisely, in the "Day of the week" category.;
* Nếu dùng NVDA 2018.2 trở lên, bạn sẽ chỉ tìm thấy một mục trong trình đơn
  công cụ cho việc tìm kiếm ngày của bạn, phần cài đặt add-on sẽ ở trong bản
  tùy chỉnh của NVDA.

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2014.3
  until 2019.1.

## Changes for 19.02 ##

* Changed version numbering using YY.MM (The year in 2 digits, followed by a
  dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Các thay đổi cho phiên bản 6.0 ##

* đã thêm cài đặt addon vào bản tùy chỉnh NVDA cho NVDA 2018.2 trở lên;
* Đã chuyển tùy chọn tìm kiếm ngày vào trình đơn công cụ;
* Đã thêm tương thích ngược của add-on với các phiên bản NVDA trước 2018.2,
  bao gồm bản các thiết lập.

## Các thay đổi cho phiên bản 5.0 ##

* Thêm tương thích của add-on với wxPython 4.0 và Python3;
* Sửa lỗi với đường dẫn add-on có kí tự không phải mã ASCII.

## Các thay đổi cho phiên bản 4.0 ##

* Add-on giờ đây đã nhận dạng được tất cả các định dạng ngày theo khu vực mà
  người dùng có thể chọn;
* Thêm tương thích ngược của add-on với các phiên bản NVDA trước 2016.4, bao
  gồm module gui.guiHelper.

## Các thay đổi cho phiên bản 3.1 ##

* Trở về định dạng trước của day of the week vì nó cho phép nhận dạng số
  lượng ngôn ngữ lớn hơn;
* Cải thiện khả năng truy cập của bộ chọn ngày với việc nhận dạng ba trường
  'Ngày', 'Tháng' và 'Năm', và giá trị tương ứng của nó;
* Đã thêm công nghệ để tích hợp Tiếng Gruzia vào nhận dạng ngày trong tuần;
* Thêm hộp thoại cấu hình để  bật hoặc tắt khả năng truy cập của bộ chọn
  ngày;
* Chuyển trình đơn của add-on từ "Công cụ" sang "Tùy chọn";
* Đổi phân loại của add-on thành "Day of the week".

## Các thay đổi cho phiên bản 2.0 ##

* Dùng module gui.guiHelper để đảm bảo hiển thị chính xác của hộp thoại hỏi
  ngày;
* Thêm giấy phép GPL vào addon;
* Đã phiên dịch ngày trong tuần, vậy nên add-on làm việc chính xác ở các
  ngôn ngữ khác nhau;
* Thay đổi định dạng ngày để tránh lỗi mã hóa.

## Các thay đổi cho phiên bản 1.0 ##

* Phiên bản đầu tiên.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
