# Day of the week #

*	 Tác giả: Abdel, Noelia.
*	 tải về [phiên bản chính thức][1]
*	 tải về [phiên bản thử nghiệm][2]

Add-on này cho phép bạn tìm kiếm ngày trong tuần căn cứ theo này đã chọn.

Add-on này thêm một trình đơn con trong trình đơn tùy chọn của NVDA với tên
"Day of the week", có hai mục con:


*	Mục đầu tiên tên "Tìm kiếm ngày", mở một hộp thoại với ba điều khiển:
	*	Một danh sách để chọn hoặc nhập ngày;
	*	Nút "Đồng ý" để hiển thị hộp thông điệp với ngày của bạn;
	*	Nút "Hủy" để đóng hộp thoại.
*	Mục thứ hai tên "dayOfTheWeek Cài đặt add-on" mở các giá trị của add-on để thiết lập việc có thông báo nhãn cho các trường ngày hay không, có các thành phần sau:
	*	Bật khả năng truy cập của bộ chọn ngày;
	*	Cấp độ thông báo của nhãn, bạn sẽ có ba lựa chọn:
		*	Dài (là lựa chọn mặc định);
		*	Ngắn (để thông báo ngắn gọn);
		*	Tắt (để tắt thông báo nhãn).
	*	Bật chỉ thông báo giá trị của trường ngày hiện tại khi di chuyển theo cột dọc;
	*	Nút "Đồng ý" để lưu cấu hình;
	*	Nút "Hủy" để hủy và đóng hộp thoại.


## Lưu ý ##

*	 Bạn có thể đóng các hộp thoại này bằng cách bấm Escape.
*	 Bạn có thể gán thao tác để mở các hộp thoại này từ trình đơn "Quản lý các
   thao tác" hoặc trong phân loại "Day of the week".

## Các thay đổi cho phiên bản 5.0 ##

*	 Thêm tương thích của add-on với wxPython 4.0 và Python3;
*	 Sửa lỗi với đường dẫn add-on có kí tự không phải mã ASCII.

## Các thay đổi cho phiên bản 4.0 ##

*	 Add-on giờ đây đã nhận dạng được tất cả các định dạng ngày theo khu vực
   mà người dùng có thể chọn;
*	 Thêm tương thích ngược của add-on với các phiên bản NVDA trước 2016.4,
   bao gồm module gui.guiHelper.

## Các thay đổi cho phiên bản 3.1 ##

*	 Trở về định dạng trước của day of the week vì nó cho phép nhận dạng số
   lượng ngôn ngữ lớn hơn;
*	 Cải thiện khả năng truy cập của bộ chọn ngày với việc nhận dạng ba trường
   'Ngày', 'Tháng' và 'Năm', và giá trị tương ứng của nó;
*	 Đã thêm công nghệ để tích hợp Tiếng Gruzia vào nhận dạng ngày trong tuần;
*	 Thêm hộp thoại cấu hình để  bật hoặc tắt khả năng truy cập của bộ chọn
   ngày;
*	 Chuyển trình đơn của add-on từ "Công cụ" sang "Tùy chọn";
*	 Đổi phân loại của add-on thành "Day of the week".

## Các thay đổi cho phiên bản 2.0 ##

*	 Dùng module gui.guiHelper để đảm bảo hiển thị chính xác của hộp thoại hỏi
   ngày;
*	 Thêm giấy phép GPL vào addon;
*	 Đã phiên dịch ngày trong tuần, vậy nên add-on làm việc chính xác ở các
   ngôn ngữ khác nhau;
*	 Thay đổi định dạng ngày để tránh lỗi mã hóa.

## Các thay đổi cho phiên bản 1.0 ##

*	 Phiên bản đầu tiên.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
