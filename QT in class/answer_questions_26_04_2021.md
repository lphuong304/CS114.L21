**Lớp: CS114.L21**

Nhóm:
1. Nguyễn Ngọc Lan Phương - *19520227*
2. Nguyễn Quốc Huy - *19521623*
3. Hoàng Anh Tú - *19522450*


**Trả lời câu hỏi: Các bài toán giải quyết bằng Machine Learning trong cuộc sống**
1. Mô hình hồi quy tuyến tính:
***Ứng dụng tính giá tiền của một chuyển đi xe ôm công nghệ***
* Cách thu thập dữ liệu: Dựa trên giá tiền từ xe ôm truyền thống
* Xử lý dữ liệu: Làm tròn xuống đối với số tiền ứng với km để tăng tính cạnh tranh, được đưa vào một file CSV gồm cột km và giá tiền
* Dữ liệu train: Số km và giá tiền ứng với số km của các chuyến đi trước đó
* Đầu vào: số km
* Đầu ra: Giá tiền
2. Mô hình hồi quy tuyến tính:
***Ứng dụng tìm hiểu mối hệ giữa liều lượng thuốc và huyết áp của bệnh nhân***
* Dữ liệu train:

:point_right:Số thực x1: miligram thuốc dùng trong ngày

:point_right:Số thực x2: chỉ số huyết áp đầu ngày

:point_right:Số thực: sự thay đổi của huyết áp

* Đầu vào:
số thực x1:miligram thuốc dùng trong ngày
số thực x2: chỉ số huyết áp đầu ngày
* Đầu ra: sự thay đổi của huyết áp
* Cách thu thập data: thu thập dữ liệu thủ công từ các nguồn tại phường, dữ liệu hành chính từ chương trình quản lý bệnh nhân điện tử (i.PM), và xem xét hồ sơ bệnh án nội trú (tiêu chuẩn vàng) cho liều lượng thuốc của bệnh nhân và chỉ số huyết áp đầu ngày*
* Xử lý dữ liệu: Chuẩn bị tệp dưới format của một bảng (csv), tạo thành 3 cột dữ liệu (cột liều lượng thuốc - đơn vị mg/ngày, là một con số thực, cột huyết áp - đơn vị mmHg, và cột kết quả - là sự thay đổi của huyết áp)
3. Mô hình hồi quy logistic:
***Ứng dụng dự báo khả năng trả nợ của khách hàng***
* Dữ liệu train:

:point_right:số thực x1: thu nhập bình quân hằng năm

:point_right:số thực x2: tổng tài sản hiện có

:point_right:số thực y: nằm trong khoảng [0, 1] thể hiện phần trăm nợ có thể trả

* Đầu vào: x1, x2
* Đầu ra: y
* Thu thập data: Liên kết vào xin cấp phép từ các ngân hàng.
* Xử lý data: 
  * Tạo file dữ liệu dưới dạng .csv với 3 cột : Thu nhập, Tổng tài sản, y(kết quả dự đoán).
  * Đưa file.csv vào chương trình với cấu trúc DataFrame. 
  *(DataFrames tương tự như SQL tables hoặc bảng tính mà bạn làm việc trong Excel hoặc Calc, Pandas DataFrame là một cấu trúc chứa dữ liệu hai chiều và các nhãn tương ứng của nó).
  * Xóa hết các hàng có chứa giá trị Null/NaN.
