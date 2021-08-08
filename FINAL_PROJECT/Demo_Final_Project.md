<h1 align="center"><b>Trường Đại Học Công Nghệ Thông Tin - ĐHQH TPHCM</b></h1>
<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: 5;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>
<h1 align="center"><b>Đồ án cuối kỳ môn Máy học - CS112.L21</b></h1>
<h2 align="center"><b>BÀI TOÁN NHẬN DIỆN SẢN PHẨM THƯƠNG MẠI ÁP DỤNG VÀO MÔ HÌNH SIÊU THỊ KHÔNG THU NGÂN TRONG BỐI CẢNH THANH TOÁN ĐIỆN TỬ PHÁT TRIỂN MẠNH </b></h2>

* Bộ môn: Máy học - CS112.L21
* Giảng viên:
  * Lê Đình Duy - *duydl@uit.edu.vn*
  * Phạm Nguyễn Trường An - *truonganpn@uit.edu.vn*
* Thành viên nhóm:
<p align="center">

| STT    | MSSV          | Họ và Tên              | Github                                              | Email                   |
| :------: |:-------------:|:----------------------:|:-------------------------------------------------:|:-----------------------:|
| 1      | 19520227      | Nguyễn Ngọc Lan Phương |[lphuong304](https://github.com/lphuong304)          |19520227@gm.uit.edu.vn   |
| 2      | 19521623      | Nguyễn Quốc Huy        |[nguyen-huy-1623](https://github.com/nguyen-huy-1623)|19521263@gm.uit.edu.vn   |
| 3      | 19522450      | Hoàng Anh Tú           |[19522450](https://github.com/19522450)              |19522450@gm.uit.edu.vn   |

</p>

# **BẢNG MỤC LỤC**

<!-- Content -->

# Tổng Quan Về Đồ Án
## Mô tả bài toán
* **Ngữ cảnh ứng dụng**: Trong thời đại công nghệ phát triển vượt trội,nhu cầu mua sắm của con người ngày càng cao, song song với sự phát triển mạnh mẽ của thương mại điện tử thì hình thức mua sắm truyền thống vẫn là sự lựa chọn hàng đầu của con người. Dựa trên điều đó, chúng em nảy ra ý tưởng vận dụng Machine Learning hay cụ thể hơn là Deep Learning vào MÔ HÌNH SIÊU THỊ KHÔNG THU NGÂN thông qua bài toán nhận diện sản phẩm thương mại.

* **Tại sao lại là MÔ HÌNH SIÊU THỊ KHÔNG THU NGÂN? Lợi ích so với mô hình truyền thống?**

    Sản phẩm đồ án của chúng em sẽ mang đến những lợi ích như sau:
    + Giúp đẩy nhanh quy trình thanh toán tại các cửa hàng, hạn chế việc chờ đợi xếp hàng.
    + Ngành công nghiệp bán lẻ ngày càng được đẩy mạnh, thì việc tự động quá khâu thanh toán giúp cắt giảm chi phí nhân lực, giảm các trường hợp dịch vụ không được đánh giá cao do thái độ nhân viên.
    + Tối ưu hóa trải nghiệm người dùng ở quá trình thanh toán.
    + Đáng tin cậy hơn so với hình thức thanh toán thủ công
    + Theo trang Digimarc<!-- https://www.digimarc.com/about/news-events/press-releases/2015/07/21/digimarc-survey-88-percent-of-u.s.-adults-want-their-retail-checkout-experience-to-be-faster -->, 45% khách hàng phàn nàn rằng đôi khi sử dụng mã vạch không tiện lợi
    + 
* **INPUT**: Video thời lượng tối đa 1 phút các sản phẩm thương mại, góc quay từ trên xuống, mặt hàng đặt nằm ngửa, quay trực diện sản phẩm, ánh sáng tốt (xét điều kiện ánh sáng siêu thị), mỗi mặt hàng có nhiều mặt (trước, sau), video không nhiễu, chất lượng video tối thiểu là 480p trở lên.
* **OUTPUT**: Tên sản phẩm thương mại + Số lượng + Gía tiền sản phẩm => Tổng tiền (Hình thức một hóa đơn)

## Mô tả dữ liệu
Dữ liệu được tụi em tự thu thập
* **Tại sao cần tự thu thập dữ liệu:**
  * Dữ liệu có sẵn không phù hợp với yêu cầu của bài toán: số lượng ảnh, góc chụp, sự đa dạng của sản phẩm. Điển hình là VOC có 20 classes và COCO có 80 classes
  * Việc tự thu thập giúp chúng em kiểm soát góc chụp, góc sản phẩm, số lượng ảnh một cách tốt nhất
* **Việc thu thập dữ liệu:**
  * Địa điểm: Từ nhiều nguồn như là siêu thị bigC, bách hóa xanh, các của hàng tiện lợi và cả tiệm tập hóa. Nhưng vì ảnh hưởng lớn của dịch, nên phần lớn dữ liệu được thu thập ở tiệm tập hóa và các của hàng tiện lợi.
  * Cách thu thập: Sử dụng điện thoại cá nhân để chụp lại hình ảnh sản phẩm ở nhiều góc độ
* **Khó khăn của việc thu thập dữ liệu:**
  * Số lượng hình ảnh lớn, yêu cầu về đa dạng sản phẩm nên việc thu thập tốn rất nhiều thời gian (khoảng 2 tuần)
  * Siêu thị và bách hóa xanh không cho chụp hình sản phẩm của họ, nên chúng em sẽ phải mua sản phẩm về nhà để chụp
  * Vì việc chụp ảnh diễn ra cùng lúc nên nhiều khi chúng em chụp lại sản phẩm mà đã có thành viên chụp rồi, hoặc mua nhầm sản phẩm đã được chụp

# Các nghiên cứu của tiền nhân

## Bài nghiên cứu về phát hiện sản phẩm trên kệ của Joseph Nelson
https://blog.roboflow.com/retail-store-item-detection-using-yolov5/

* Theo bài báo, họ sử dụng bộ dữ liệu SKU110k image dataset, bao gồm 2940 ảnh trong tập test và 8232 ảnh trong tập train và  587 ảnh trong tập validation
* Phương pháp sử dụng là YOLOv5
* Với kết quả đem lại là mAP là 0.7 với IoU là 0.5

## Bài báo nghiêm cứu về nhận diện sản phẩm của Yuchen Wei , Son Tran , Shuxiang Xu Byeong Kang and Matthew Springer 
https://www.hindawi.com/journals/cin/2020/8875910/

* **Theo bài báo**
Họ sử dụng nhiều bộ dữ liệu cùng với đó là công nghệ khác nhau trên từng bộ dữ liệu đem lại những hiệu quả khác nhau. Bộ dữ liệu từ nhiều nguồn họ sử dụng bao gồm GroZi-120, GroZi-3.2k, Freiburg Grocery Dataset, Cigarette Dataset, Grocery Store Dataset, GP181 Dataset, D2S Dataset và RPC Dataset. Với từng bộ dữ liệu, họ có sử dụng những phương thức tiếp cận khác nhau, như với CNN, GroZi-3.2k cho mAP 73.93%, GP-20 cho mAP 65.55% và GP181 cho mAP 85.79%
* **Tổng kết của bài báo nghiêm cứu**
  * Thách thức:
    * Phân loại bài toán với quy mô lớn
    * Hạn chế về dữ liệu
    * Biến thể nội thủy tinh
    * Tính linh hoạt
  * Các kỹ thuật đã sử dụng trong nghiên cứu:
    * Generating data with deep neural networks
    * Graph neural networks with deep learning
    * Cross-domain recognition with transfer learning
    * Joint feature learning from text information on packaging
    * Incremental learning with the CNN
    * The regression-based object detection methods for retail product recognition
* **Nhận xét từ các bài báo**: Bài báo có đề cập đến việc YOLO9000 đã cung cấp một phương pháp có thể phát hiện 9000 lớp đối tượng, nhưng không khả thi trong trường hợp phát hiện sản phẩm vì chi phí chú thích cao. Nhưng vì chúng em làm khoảng 200 lớp, và đã có ý định dùng "cơm" để gắn nhãn sản phẩm, nên đã sử dụng YOLOv4.
