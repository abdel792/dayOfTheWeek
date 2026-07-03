# Thứ trong tuần #

* Nhà phát triển: Abdel, Noelia.

Add-on này cho phép bạn tìm thứ trong tuần tương ứng với một ngày đã chọn.

Nó thêm một menu con vào menu Công cụ của NVDA có tên là "Thứ trong tuần", bao gồm 2 mục:

* Mục thứ nhất có tên "Tìm một ngày", mở ra một hộp thoại gồm 3 bảng điều khiển:

    * Một hộp danh sách để chọn hoặc nhập ngày của bạn;
    * Một nút "OK" để hiển thị hộp thông báo chứa thứ của ngày đó;
    * Một nút "Hủy" để đóng hộp thoại.

* Mục thứ hai có tên "Cài đặt add-on dayOfTheWeek", mở các tham số của add-on để chỉ định bạn có muốn thông báo các nhãn của trường ngày hay không, bao gồm các thành phần sau:

    * Bật tính năng dễ tiếp cận cho trình chọn ngày;
    * Mức độ thông báo của các nhãn, bạn sẽ có 3 lựa chọn:

        * Dài (đây là lựa chọn mặc định);
        * Ngắn (cho các thông báo ngắn gọn);
        * Tắt (để tắt thông báo nhãn).

    * Chỉ bật thông báo giá trị trường ngày hiện tại khi di chuyển theo chiều dọc;
    * Một nút "OK" để lưu cấu hình của bạn;
    * Một nút "Hủy" để hủy và đóng hộp thoại.

## Lưu ý ##

* Bạn có thể đóng các hộp thoại này chỉ bằng cách nhấn phím Escape;
* Bạn có thể gán một phím tắt để mở các hộp thoại này trong menu "Phím tắt nhập liệu" và chính xác hơn là trong danh mục "Thứ trong tuần";
* Nếu bạn đang sử dụng NVDA 2018.2 trở lên, bạn sẽ chỉ tìm thấy một mục trong menu công cụ để tìm ngày của mình, các cài đặt của add-on sẽ nằm trong bảng cài đặt của NVDA.

## Tính tương thích ##

* Add-on này tương thích với các phiên bản NVDA từ 2019.3 trở lên.

## Thay đổi cho 20240326.0.0

* Cập nhật tính tương thích cho nvda-2024.1.;
* Xóa liên kết tải xuống khỏi tệp readme, liên kết tải xuống cho các bản cập nhật trong tương lai giờ đây sẽ chỉ có sẵn từ cửa hàng add-on.

## Thay đổi cho 20231229.0.0 ##

* Thêm một triển khai tương thích ngược để hỗ trợ chế độ lời nói theo yêu cầu, chế độ này sẽ sớm có sẵn với nvda-2024.1.

## Thay đổi cho 20231015.0.0 ##

* Sửa một lỗi được phát hiện khi điều hướng bằng mũi tên lên từ trình chọn ngày trong các phiên bản NVDA mới nhất.

## Thay đổi cho 20230728.0.0 ##

* Áp dụng các quy tắc flake8 và mypy vào mã nguồn;
* Thay đổi phiên bản NVDA tối thiểu được hỗ trợ thành 2019.3 để hỗ trợ các chú thích được giới thiệu trong Python 3.

## Thay đổi cho 20230607.0.0 ##

* Thêm các quy trình làm việc (workflows) sau:
 * auto-update-translations - để tự động cập nhật các bản dịch từ hệ thống dịch của NVDA.
 * release-on-tag..yaml: để xây dựng và xuất bản add-on ngay khi một tag mới được push;
 * manual-release.yaml: để xây dựng và phát hành các phiên bản mới của add-on một cách thủ công.
* Cập nhật các bản dịch.

## Thay đổi cho phiên bản 20230508.0.0 và trở lên ##

* • Thay đổi số phiên bản, phiên bản NVDA tối thiểu và liên kết tải xuống theo các quy ước/yêu cầu của cửa hàng.

## Thay đổi cho 19.02 ##

* Thay đổi cách đánh số phiên bản bằng cách sử dụng YY.MM (Năm có 2 chữ số, tiếp theo là dấu chấm, tiếp theo là tháng có 2 chữ số);
* Thêm tính tương thích với định dạng phiên bản add-on mới, xuất hiện từ nvda 2019.1.

## Thay đổi cho 6.0 ##

* Thêm các cài đặt của add-on vào bảng cài đặt NVDA cho NVDA 2018.2 trở lên;
* Di chuyển mục tìm một ngày vào menu công cụ;
* Thêm tính năng tương thích ngược của add-on với các phiên bản NVDA trước 2018.2 có bao gồm bảng cài đặt.

## Thay đổi cho 5.0 ##

* Thêm tính tương thích của add-on với wxPython 4.0 và Python3;
* Sửa một lỗi với các đường dẫn add-on chứa các ký tự không phải ASCII.

## Thay đổi cho 4.0 ##

* Add-on giờ đây có thể nhận dạng tất cả các định dạng ngày theo vùng mà người dùng có thể chọn;
* Thêm tính năng tương thích backward của add-on với các phiên bản NVDA trước 2016.4 có bao gồm mô-đun gui.guiHelper.

## Thay đổi cho 3.1 ##

* Quay lại định dạng trước đó cho thứ trong tuần vì nó cho phép nhận dạng số lượng ngôn ngữ lớn hơn;
* Cải thiện tính dễ tiếp cận của trình chọn ngày với việc nhận dạng 3 trường 'Ngày', 'Tháng' và 'Năm' cùng các giá trị tương ứng của chúng;
* Thêm một kỹ thuật tích hợp tiếng Gruzia để nhận dạng các thứ trong tuần;
* Thêm một hộp thoại cấu hình để bật hoặc tắt tính năng dễ tiếp cận của trình chọn ngày;
* Di chuyển menu con của add-on từ "Công cụ" sang "Tùy chọn";
* Thay đổi danh mục của add-on thành "Thứ trong tuần".

## Thay đổi cho 2.0 ##

* Sử dụng mô-đun gui.guiHelper để đảm bảo giao diện chính xác của hộp thoại yêu cầu ngày tháng;
* Thêm giấy phép GPL vào add-on;
* Các thứ trong tuần đã được dịch để add-on hoạt động chính xác bằng các ngôn ngữ khác nhau;
* Thay đổi định dạng ngày để tránh lỗi mã hóa.

## Thay đổi cho 1.0 ##

* Phiên bản đầu tiên.
