# Ngày của tuần

- Tác giả: Abdel, Noelia.

Add-on này cho phép bạn tìm kiếm ngày trong tuần căn cứ theo này đã chọn.

Nó thêm một trình đơn con trong trình đơn tùy chọn của NVDA với tên "Day of
the week", có hai mục con:

- Mục đầu tiên tên gọi "Tìm một ngày", mở một hộp thoại được thiết kế với ba
  điều khiển:

  - Một hộp danh sách để chọn hoặc nhập ngày của bạn;
  - Nút "OK" để hiển thị hộp thông điệp chứa ngày của bạn;
  - Nút "Cancel" để đóng hộp thoại.

- Mục thứ hai tên gọi "cài đặt add-on ngày trong tuần" mở các tham số của
  add-on để quy định có thông báo nhãn cho trường ngày hay không, bao gồm
  các thành phần sau:

  - Bật khả năng truy cập cho bộ chọn ngày;

  - Cấp độ thông báo nhãn, bạn sẽ có ba lựa chọn:

    - Dài (là lựa chọn mặc định);
    - Ngắn (cho thông báo ngắn gọn);
    - Tắt (vô hiệu hóa thông báo).

  - Chỉ bật thông báo giá trị của trường ngày hiện tại, khi di chuyển theo
    hàng dọc;

  - Nút "OK" để lưu cấu hình của bạn;

  - Nút "Cancel" để hủy và đóng hộp thoại.

## Lưu ý

- Bạn có thể đóng các hộp thoại này bằng cách bấm Escape;
- Bạn có thể gán thao tác để mở các hộp thoại này từ trình đơn "Quản lý các
  thao tác" hoặc trong phân loại "Ngày của tuần";
- Nếu dùng NVDA 2018.2 trở lên, bạn sẽ chỉ tìm thấy một mục trong trình đơn
  công cụ cho việc tìm kiếm ngày của bạn, phần cài đặt add-on sẽ ở trong bản
  tùy chỉnh của NVDA.

## Tương thích

- This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20240326.0.0

- Updated compatibility for nvda-2024.1.;
- Deleted download link from readme, the download link for future updates
  will now only be available from the add-on store.

## Changes for 20231229.0.0

- Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Changes for 20231015.0.0

- Fixed a bug detected when navigating with up arrow from the date picker in
  the latest versions of NVDA.

## Changes for 20230728.0.0

- Applied the flake8 and mypy rules to the code;
- Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Changes for 20230508.0.0 and beyond

- Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.
- auto-update-translations - to automatically update translations from NVDA's translation system.
- release-on-tag..yaml: to build and publish the addon as soon as a new tag is pushed;
- manual-release.yaml: to build and release new versions of the add-on manually.
- Updated translations.

## Các thay đổi cho phiên bản 19.02

- Thay đổi cách đặt số phiên bản bằng YY.MM (hai chữ số năm, một dấu chấm,
  hai chữ số tháng);

## Các thay đổi cho phiên bản 6.0

- đã thêm cài đặt addon vào bản tùy chỉnh NVDA cho NVDA 2018.2 trở lên;
- Đã chuyển tùy chọn tìm kiếm ngày vào trình đơn công cụ;

## Các thay đổi cho phiên bản 5.0

- Thêm tương thích của add-on với wxPython 4.0 và Python3;
- Sửa lỗi với đường dẫn add-on có kí tự không phải mã ASCII.
- Added the backward compatibility of the add-on with the NVDA versions that preceded 2018.2, which included the settings panel.

## Các thay đổi cho phiên bản 4.0

- Add-on giờ đây đã nhận dạng được tất cả các định dạng ngày theo khu vực mà
  người dùng có thể chọn;
- Thêm tương thích ngược của add-on với các phiên bản NVDA trước 2016.4, bao
  gồm module gui.guiHelper.

## Các thay đổi cho phiên bản 3.1

- Trở về định dạng trước của day of the week vì nó cho phép nhận dạng số
  lượng ngôn ngữ lớn hơn;
- Cải thiện khả năng truy cập của bộ chọn ngày với việc nhận dạng ba trường
  'Ngày', 'Tháng' và 'Năm', và giá trị tương ứng của nó;

## Các thay đổi cho phiên bản 2.0

- Dùng module gui.guiHelper để đảm bảo hiển thị chính xác của hộp thoại hỏi
  ngày;
- Thêm giấy phép GPL vào addon;
- Đã phiên dịch ngày trong tuần, vậy nên add-on làm việc chính xác ở các
  ngôn ngữ khác nhau;
- Thay đổi định dạng ngày để tránh lỗi mã hóa.
- Moved the add-on submenu from "Tools" to "Preferences";
- Changed the add-on category to "Day of the week".

## Các thay đổi cho phiên bản 1.0

- Phiên bản đầu tiên.
- Added the GPL license to the addon;
- Days of the week have been translated, so that the add-on works properly in the different languages;
- Changed the day format to avoid encoding errors.

## Changes for 1.0

- Initial version.
