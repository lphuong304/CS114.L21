

<h3 align="center" font-size= 14px;><b>Trường Đại Học Công Nghệ Thông Tin - ĐHQH TPHCM</b></h3>
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

| STT  |   MSSV   |       Họ và Tên        |                        Github                         |         Email          |
| :--: | :------: | :--------------------: | :---------------------------------------------------: | :--------------------: |
|  1   | 19520227 | Nguyễn Ngọc Lan Phương |      [lphuong304](https://github.com/lphuong304)      | 19520227@gm.uit.edu.vn |
|  2   | 19521623 |    Nguyễn Quốc Huy     | [nguyen-huy-1623](https://github.com/nguyen-huy-1623) | 19521263@gm.uit.edu.vn |
|  3   | 19522450 |      Hoàng Anh Tú      |        [19522450](https://github.com/19522450)        | 19522450@gm.uit.edu.vn |

</p>

# **BẢNG MỤC LỤC**

1. [Tổng Quan Về Đồ Án](#tongquan)
2. [Các Nghiên Cứu Về Bài Toán Của Tiền Nhân](#cacnghiencuu)
3. [Xây Dựng Bộ Dữ Liệu](#dulieu)
4. [Training Và Đánh Giá Model](#training)
5. [Hướng Phát Triển Ứng Dụng Và Cải Tiến](#ungdung)
6. [Phân Công Công Việc](#phancong)
7. [Nguồn Tham Khảo](#thamkhao)

<a name="tongquan"></a>
# **1. Tổng Quan Về Đồ Án**
# Mô tả bài toán

* **Ngữ cảnh ứng dụng**: 
  *   Trong thời đại công nghệ phát triển vượt trội,nhu cầu mua sắm của con người ngày càng cao, song song với sự phát triển mạnh mẽ thương mại điện tử thì hình thức mua sắm truyền thống vẫn là sự lựa chọn hàng đầu của con người. Dựa trên điều đó cộng với việc các hình thức thanh toán điện tử được áp dụng rộng rãi thay cho thanh toán bằng tiền mặt, chúng em nảy ra ý tưởng vận dụng kiến thức Machine Learning hay cụ thể hơn là Deep Learning để giải quyết một bài toán nhỏ trong ứng dụng Mô Hình Siêu Thị Không Thu Ngân - **Bài Toán Nhận Diện Sản Phẩm Thương Mại**

  * Tuy nhiên trước tiên, chúng ta cần hiểu rõ **Thế nào là Mô hình Siêu thị Không Thu Ngân?**, **Lợi ích của Mô hình Siêu Thị không Thu ngân so với Mô hình Mua sắm Truyền thống thông thường?** 
    * Mô hình Siêu thị không thu ngân là mô hình ứng dụng các công nghệ trí tuệ nhân tạo vào các cửa hàng siêu thị mô hình thông thường, tận dụng sức mạnh của AI để thay thế nhân lực cụ thể là ở các quầy thanh toán, checkout.
    * Sản phẩm đồ án của chúng em sẽ mang đến những lợi ích như sau:
      + Giúp đẩy nhanh quy trình thanh thoán tại các cửa hàng, hạn chế việc chờ đợi xếp hàng.
      + Ngành công nghiệp bán lẻ ngành càng được đẩy mạnh, thì việc tự động quá khâu thanh toán giúp cắt giảm chi phí nhân lực, giảm các trường hợp dịch vụ không được đánh giá cao do thái độ nhân viên.
      + Tối ưu hóa trải nghiệm người dùng ở quá trình thanh toán.
      + Đáng tin cậy hơn so với hình thức thanh toán thủ công.
      + Theo trang [HaNoi Times](http://hanoitimes.vn/vietnams-retailers-accelerate-shopping-experiences-to-meet-consumer-demand-317284.html),trong cuộc khảo vào năm 2021 ở những nước Châu Á Thái Bình Dương bao gồm cả Việt Nam, 50% người mua sắm được khảo sát đã tương tác với mô hình siêu thị self-checkouts và hơn 60% đồng ý rằng mô hình self-checkouts mang lại trải nghiệm khách hàng cải thiện hơn.
* **INPUT và OUTPUT Bài toán:**
  * INPUT: 
    * Video thời lượng tối đa 1 phút các sản phẩm thương mại
    * Các sản phẩm trong clip, nếu tính cùng một vật thể thì chỉ xuất hiện đúng 1 lần **(giả sử trong video test nếu sản phẩm đó xuất hiện lần 2 thì được tính là 2 sản phẩm khác nhau)**
    * Độ phân giải tối thiểu **480p**
    * Video được quay trực diện sản phẩm, cách sản phẩm từ **5 -15cm**
    * Tất cảc sản phẩm được đặt nằm ngang, hoặc đứng tuỳ thuộc hình dạng sản phẩm (ưu tiên đặt các sản phẩm nằm ngang)
    * Video không có noises, ánh sáng tốt **(ISO camera > 100)**
  * OUTPUT: 
    * Video đầu vào với các thông tin được hiển thị trên video cụ thể như sau:
      * Bbox bao quanh các sản phẩm được nhận diện đi kèm với tên sản phẩm+chỉ số biểu thị độ chính xác của sản phẩm nhận diện
      * Tên sản phẩm, tổng số lượng, tổng giá sản phẩm được nhận diện.
      * Bill thanh toán format file text, có tổng giá khách hàng phải thanh toán.
<a name="cacnghiencuu"></a>
# **2.Các Nghiên Cứu Về Bài Toán Của Tiền Nhân**
## [Bài nghiên cứu về *"Phát hiện sản phẩm trên kệ"* của Joseph Nelson](https://blog.roboflow.com/retail-store-item-detection-using-yolov5/)

* **Theo bài báo**

* Bộ dữ liệu sử dụng: **SKU110k** images dataset, bao gồm **2940 ảnh trong tập test**, **8232 ảnh trong tập train** và **587 ảnh trong tập validation**
* Model Training: YOLOv5
* Performance: **mAP là 0.7** với **IoU là 0.5**

## [Bài báo nghiêm cứu về *"Nhận diện sản phẩm"* của Yuchen Wei , Son Tran , Shuxiang Xu Byeong Kang and Matthew Springer](https://www.hindawi.com/journals/cin/2020/8875910/)

* **Theo bài báo**

Họ sử dụng nhiều bộ dữ liệu cùng với đó là công nghệ khác nhau trên từng bộ dữ liệu đem lại những hiệu quả khác nhau. Bộ dữ liệu từ nhiều nguồn, bao gồm **GroZi-120, GroZi-3.2k, Freiburg Grocery Dataset, Cigarette Dataset, Grocery Store Dataset, GP181 Dataset, D2S Dataset và RPC Dataset**. Với từng bộ dữ liệu, họ có sử dụng những phương thức tiếp cận khác nhau, như với **GroZi-3.2k cho mAP 73.93%, GP-20 cho mAP 65.55% và GP181 cho mAP 85.79%**
* **Tổng kết của bài báo nghiên cứu**
  * Thách thức:
    * Phân loại bài toán với quy mô lớn
    * Hạn chế về dữ liệu
    * Biến thể nội thủy tinh (các sản phẩm có thủy tinh có sự phản xạ từ môi trường xung quanh)
    * Tính linh hoạt
  * Các kỹ thuật đã sử dụng trong nghiên cứu:
    * Generating data with deep neural networks
    * Graph neural networks with deep learning
    * Cross-domain recognition with transfer learning
    * Joint feature learning from text information on packaging
    * Incremental learning with the CNN
    * The regression-based object detection methods for retail product recognition
* **Nhận xét từ các bài báo**: Bài báo có đề cập đến việc YOLO9000 đã cung cấp một phương pháp có thể phát hiện 9000 lớp đối tượng, nhưng không khả thi trong trường hợp phát hiện sản phẩm vì chi phí chú thích cao. 

<a name="dulieu"></a>
# **3.Xây Dựng Bộ Dữ Liệu**
## Mô tả dữ liệu
Dữ liệu được tụi em tự thu thập
* **Tại sao cần tự thu thập dữ liệu thủ công:**
  * Dữ liệu có sẵn không phù hợp với yêu cầu của bài toán: số lượng hình ảnh,background xung quanh sản phẩm, mẫu mã sản phẩm thương hiệu Việt Nam hầu như không có sẵn và rất ít,...
  * Việc tự thu thập giúp chúng em kiểm soát góc chụp, góc sản phẩm, số lượng ảnh một cách tốt nhất,... ngoài ra nhóm chúng em cũng đặt riêng các tiêu chí khi thu thập dữ liệu cho các thành viên.
* **Các tiêu chí khi thu thập dữ liệu:**
  * Vị trí của camera đặt cách sản phẩm từ **5 – 15cm** (tính từ bề mặt hướng vào của sản phẩm đến camera)
  * Background sản phẩm là **nền sáng**.
  * Đảm bảo độ sáng hình chụp **ISO > 100**.
  * Góc máy ảnh đặt từ trên xuống dưới trực diện sản phẩm và góc nghiêng
  * Các mặt hàng có nhiều hình dạng khác nhau nên để thuận lợi cho việc thu thập data và tăng khả năng nhận diện thì cách đặt cũng có tiêu chí riêng:
    * Hình trụ: Đặt thẳng đứng hoặc nằm ngang và phải thấy logo hoặc tên.
    * Hình hộp: Đặt nằm ngang, ưu tiên mặt có logo hoặc tên ở phía trên.
    * Dạng gói: Đặt nằm ngang, ưu tiên mặt có logo hoặc tên ở phía trên.  

* **Việc thu thập dữ liệu:**
  * Địa điểm: Từ nhiều nguồn như là siêu thị bigC, bách hóa xanh, các của hàng tiện lợi và cả tiệm tập hóa. Nhưng vì ảnh hưởng lớn của dịch, nên phần lớn dữ liệu được thu thập ở tiệm tập hóa và các của hàng tiện lợi.
  * Cách thu thập: Sử dụng điện thoại cá nhân để chụp lại hình ảnh sản phẩm ở nhiều góc độ
* **Khó khăn của việc thu thập dữ liệu:**
  * Số lượng hình ảnh lớn, yêu cầu về đa dạng sản phẩm nên việc thu thập tốn rất nhiều thời gian (khoảng 2 tuần)
  * Siêu thị và bách hóa xanh không cho chụp hình sản phẩm của họ 
  
    <span>&#8594;</span> **Giải pháp**: Mua sản phẩm về chụp nhưng sẽ cân nhắn lại các sản phẩm không còn như dự tính ban đầu.
* **Tổng quan về Bộ Dữ liệu:**
  *  Bộ dữ liệu dùng để training và testing model: gồm 18995 tấm ảnh, chụp 199 classes khác nhau, mỗi class có sự chênh lệnh không đồng đều về số lượng ảnh.
  * Bộ dữ liệu test mà model hoàn toàn chưa từng “tiếp xúc” bao giờ:
 gồm 10 – 15 videos được quay với điều kiện ràng buộc Input vừa mới đề cập.
  * Một tập dataset csv do nhóm tự đi thu thập trên mạng về, được cập nhật giá cụ thể và gần nhất, chủ yếu lấy từ Bách Hóa Xanh.
  * Hoàn toàn do nhóm tự chụp, tự quay
<p align="middle">
  <img src="https://user-images.githubusercontent.com/55471582/128621876-d4095ceb-7709-4da4-ad0b-55e558ed43c2.png" width="100" />
  <img src="https://user-images.githubusercontent.com/55471582/128621915-ea546a3b-349b-49fc-82df-879bc901d026.png" width="100" /> 
  <img src="https://user-images.githubusercontent.com/55471582/128621922-a6ad9631-36fc-4e0e-84fd-6a12ea3a4e72.png" width="100" />
  <img src="https://user-images.githubusercontent.com/55471582/128621963-eebc1685-daa8-455f-a02c-851be2a35eb7.png" width="100" />
</p>
<div style=width: 130px; align = center>Demo một số hình ảnh trong tập Dữ liệu</div>

<h3> Nhận xét: </h3>
<ol> 
  <li> Data nhóm hoàn toàn do thủ công tự chụp, thành viên trong nhóm đã thống nhất với nhau từ trước sẽ tạo nên một bộ dữ liệu “sạch” (clean data). </li>
  <ul> => Nhóm chúng em không có bước tiền xử lý dữ liệu. </ul>
  
  <li> Data nhóm có kích thước khá lớn (17.3GB), và do trong quá trình chuẩn bị dữ liệu, đường truyền mùa dịch không ổn định và quá trình train hay bị tràn, crash trên colab.</li>
  <ul> => Nhóm chúng em quyết định không có bước tăng cường dữ liệu, chấp nhận việc model có thể bị overfitting – sẽ demo sau, nhưng chúng em vẫn đảm bảo model sẽ detect tốt trong các video test được quay với điều kiệu đã ràng buộc từ trước. </ul>
</ol>


<h2> 3. Mô tả thông số bộ dữ liệu </h2>
<div align="middle"> <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/ThongSo01.png" /> </div>
<div align="middle"> <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/ThongSo02.png" /> </div>
<div align="middle"> <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/ThongSo03.png" /> </div>
<h3> Nhận xét thông số: </h3>
<ul>
  <li> Bộ dữ liệu có sự chênh lệch lớn về giữa các class, dự đoán mô hình training sẽ khó xử lý trên nhưng bởi lí do đã nêu trên, nhóm chúng em quyết định sẽ không tiền xử lý dữ liệu. => <strong>unbalanced data</strong> </li>
  
  <li> Nếu đem model training từ tập dữ liệu trên nhưng không có tiền xử lý dữ liệu thì độ chính xác khi áp dụng vào thực tế có thể sẽ thấp hơn => <strong>dự đoán model bị overfitting</strong> </li>
</ul>

<h3> Bộ dữ liệu cho mỗi model </h3>
<p> Hai tập dữ liệu dùng để train hai model đều có kích thước 17.3GB, tập dữ liệu sẽ bao gồm files ảnh chụp định dạng *.jpg các sản phẩm và files label (gán nhãn cho từng ảnh). </p>

<table border="1" style="width:100%;">
  <tr>
    <th> YOLO </th>
    <th> DETECRON2 </th>
  </tr>
  
  <tr>
    <td align="middle" style="width:50%;"> Định dạng files annotaions dưới dạng <strong>*.txt</strong> <br> (Tương ứng với một files ảnh sẽ có files labels trùng tên tương đương) </td>
    <td align="middle"> Định dạng files annotations dưới dạng <strong>*.json</strong>. </td>
  </tr>
  
  <tr>
    <td align="middle" colspan="2"> Bộ dữ liệu dùng để train model yolov4 được chia theo tỉ lệ <strong>80/20</strong> tương đương <strong>train/valid</strong>. </td>
  </tr>
</table>


<h3> Một số trường hợp khó xử lý: </h3>
<ul>
  <li> <strong>Khoảng các giữa các sản phẩm nhỏ hơn nhiều so với khoảng cách từ sản phẩm tới biên màn hình:</strong> </li>
  <div align="middle">
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/NhieuSp01.png" style="width:30%;"/>
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/NhieuSp02.png" style="width:30%;"/>
  </div>
  <ul> => Giải pháp: trong một khung hình chỉ nên xuất hiện một sản phẩm. </ul>

  <li> <strong>Các sản phẩm có đặc điểm cùng màu sắc, cùng hình dáng:</strong> </li>
  <div align="middle">
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/HopDo01.jpg" style="width:30%;"/>
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/HopDo02.jpg" style="width:30%;"/>
  </div>
  <div align="middle">
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/HopTron01.jpg" style="width:30%;"/>
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/HopTron02.jpg" style="width:30%;"/>
  </div>
  <div align="middle">
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/HopVang01.jpg" style="width:30%;"/>
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/HopVang02.jpg" style="width:30%;"/>
  </div>
  <div align="middle">
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/LonXanh01.jpg" style="width:30%;"/>
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/LonXanh02.jpg" style="width:30%;"/>
  </div>

  <li> <strong>Các sản phẩm có cùng hình dáng khác tông màu:</strong> </li>
  <div align="middle">
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/Tru01.jpg" style="width:30%;"/>
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/Tru02.jpg" style="width:30%;"/>
  </div>
  <div align="middle">
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/HopTron01.jpg" style="width:30%;"/>
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/HopTron02.jpg" style="width:30%;"/>
  </div>
                                                                                                                                   
  <li> <strong>Các sản phẩm có tông màu khác hình dạng:</strong> </li>
  <div align="middle">
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/Do01.jpg" style="width:30%;"/>
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/Do02.jpg" style="width:30%;"/>
  </div>
  <div align="middle">
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/Xanh01.jpg" style="width:30%;"/>
    <img src="https://raw.githubusercontent.com/19522450/CS114.L21/main/FINAL_PROJECT/image/Xanh02.jpg" style="width:30%;"/>
  </div>
</ul>


<a name="training"></a>
# **4. Training Và Đánh Giá Model**
## Giải thích về quá trình Training Model:

<p align ="middle">
  <img src = "https://user-images.githubusercontent.com/55471582/128622657-efe4d909-718a-4173-be7f-3efea3958b29.png" />
</p>
* Sau khi tìm hiểu, chúng em rút kế được cho mình kiến thức về quá trình training như sau:
Từ một tập dữ liệu Datasets hình ảnh đã được chuẩn bị từ trước
<div align="center">Từ một tập dữ liệu Datasets hình ảnh đã được chuẩn bị từ trước.</div>
<div align="center"><span>&#8595;</span></div>
<div align="center">Tiền xử lý dữ liệu Input trước khi đưa vào training, thực hiện Trích Xuất đặc Trưng ảnh.</div>
<div align="center"><span>&#8595;</span></div>
<div align="center">Tiến hành áp dụng các thuật toán cần thiết để máy học được những đặc trưng đó, nhằm phát hiện vật thể dựa trên Feature map.</div>

* Giải thích vì sao phải Trích xuất đặc trưng ảnh?
  * Do máy tính không thể tự nắm bắt được những thông tin cần thiết từ một bức hình để có thể học được những đặc điểm của vật thể có trong bức hình đó, ví dụ khi ta đưa hình một sản phẩm như "Pepsi lon xanh 330ml", máy không thể tự biết lấy những đặc điểm cần thiết như màu sắc lon coca, hình dạng lon,... để "học" và nhận biết những lon coca khác về sau. Nên chúng ta cần có bước này để máy có thể học được những đặc trưng đó.
## Hướng Tiếp cận quá trình lựa chọn Model để huấn luyện của nhóm**
 * So với Datasets của các Nghiên cứu từ trước mà giải quyết cùng bài toán, Datasets của chúng em không lớn để có thể xây dựng một mạng lưới hiểu quả cho việc triết xuất đặc trưng ảnh và giúp máy học các đặc trưng đó.
 * Kỹ năng lựa chọn ra các đặc trưng của chúng em trong chưa tốt. (Các kỹ thuật trích xuất đặc trưng ảnh thủ công như HOG, SURF,... có khá nhiều bất cập nhưng quan trọng nhất là do các đặc trưng được tạo ra không có khả năng huấn luyện vì quy luật tạo ra chúng là cố định)

  <span>&#8594;</span> **Giải pháp**: Áp dụng Kỹ thuật Transfer Learning (Tận dụng những kinh nghiệm kiến thức đã học được từ vấn đề này để giải quyết một vấn đề khác có liên quan), ở đây chúng em sẽ tận dụng nguồn tài nguyên dồi dào về các bài toán Objects Detection để áp dụng vào bài toán của nhóm em. 
  
  <span>&#8594;</span>Sử dụng mô hình **CNN(convolutional neutral network)** điển hình như Darknet, VGG – 16,.... Resnet,...để triết xuất đặc trưng thông qua các tầng layers.
  
  * *Đặc điểm của mô hình CNN hoàn toàn phù hợp với yêu cầu giải quyết bài toán của chúng em:* *
    * Kiến trúc phân tầng, học đặc trưng từ các cấp độ khác nhau, mức độ chi tiết đặc điểm của object cần detect trong hình ảnh cũng tăng lên thông qua các Feature Map (ví dụ như màu lon nước, đặc điểm logo,...) đến layer cuối cùng sẽ thu về được một lon nước hoàn chỉnh.
    * Đã được huấn luyện trên một datasets lớn từ trước, giải quyết được vấn đề datasets nhỏ của chúng em, tức là nó đã được học cách tự điều chỉnh những features mà nó cần trích xuất để phù hợp với tasks tương ứng.
<p align ="middle">
  <img src ="https://user-images.githubusercontent.com/55471582/128630197-d46602cf-36e7-4eff-b8e6-09ed55f03d53.png" />
 </p>
<div align= "center">Feature map - một khối output mà ta sẽ chia nó thành một lưới ô vuông và áp dụng tìm kiếm và phát hiện vật thể trên từng cell.</div>

Sau quá trình cân nhắc, nhóm quyết định sẽ sử dụng hai model được xem là một trong những  state-of-the art objects detector tốt nhất hiện nay để train và giải quyết bài toán là **Yolov4** và **Detectron2**

## Model Yolov4:
* Hiện nay, yolov4 vẫn được đánh giá là một trong những model để xây dựng state-of-the-art objects detector tốt nhất.
* Model Yolov4 sử dụng từ nhiều bộ dataset để train từ trước, đơn cử nhất là từ hai bộ dataset nổi tiếng là *ImageNet(ILSVRC 2012 val) gồm 1000 object classes với gần 1,5 triệu ảnh dùng để huấn luyện*  và *MS COCO (test-dev 2017) gồm 80 classes với 330000 ảnh dùng để huấn luyện*, có thêm các bước tăng cường dữ liệu như cutmix, blur,...
* Vì yolov4 là thuộc dạng **one-stage-detection** như SSD,... gồm các phần cơ bản bao gồm backbone, neck và dense prediction, **tuy nhiên ở đây chúng ta chỉ quan tâm chủ yến đến phần backbone**.
* Sử dụng kiến trúc backbone CPSDarknet53 (Kết hợp Darknet-53 và chiến lược CPSNet) để trích xuất đặc trưng. Sau khi các đặc trưng được trích xuất dưới dạng output là một feature map, nó sẽ được đưa vào các layers để dự đoán labels cũng như bbox của vật thể.
<p align ="middle">
  <img src ="https://user-images.githubusercontent.com/55471582/128632422-a454e567-b0e7-4b46-9ab7-7327b6221cdb.png" />
 </p>
<div align= "center">Kiến trúc của Model Yolov4.</div>

                    
* Để train lần đầu tiên, chúng em sử dụng file Pretrained Weights **yolov4.conv.137** để tiếp tục train cho model của mình.
* Giải thích vì sao sử dụng file pretrained weights yolov4.conv.137:
  * Sử dụng file Pretrained Weights giúp tiết kiệm thời gian train lại toàn bộ model từ đầu.
  * Datasets của chúng em nhỏ nhưng có đặc điẻm tương tự với bộ datasets dùng để train model yolov4 nên để giảm thiểu trường hợp bị overfitting, chúng em không lựa chọn sử dụng file yolov4.weights thông thường - chứa thông tin như weights,... của toàn bộ networks mà chỉ lựa chọn train từ layers nào.
* **Quá trình chuẩn bị dữ liệu cho và training cho Model yolov4:**  
* Quá trình chuẩn bị dữ liệu:
  1. Dữ liệu hình chụp thủ công 18995 files hình ảnh
  2. Sử dụng tool gán nhãn [labelImg](https://github.com/tzutalin/labelImg) để labels cho tập dữ liệu hình ảnh <span>&#8594;</span> Dữ liệu cơ bản thành:
     + **18995** files hình 
     + **18996** file text labels (bao gồm 1 file classes.txt chưa tên 199 classes thành từng dòng chứa tên class sắp thành từng dòng, được đánh số bắt đầu tử **0**) tương ứng với từng file hình là file text label trùng tên tương ứng
     + Mỗi file labels text sẽ chứa số thứ tự của nhãn được gán trong file classes.txt, 4 con số thập phân liên qua đến thông tin của bbox.
   3. Chia dữ liệu theo tỷ lệ **80/20** tương đương với hai tập dữ liệu **train/valid**.
<p align ="middle">
  <img src ="https://user-images.githubusercontent.com/55471582/128636488-b740a211-9fdf-4204-be57-2574e4a6a0d6.png" />
  <img src ="https://user-images.githubusercontent.com/55471582/128636472-cab1e11c-2d73-49ec-b6df-c07c625a9c82.png" />
 </p>
<div align= "center">Ảnh trong quá trình nhóm gán nhãn.</div>

* Quá trình training model:
  1. Upload bộ dữ liệu đã được nhóm chuẩn bị sẵn lên Drive
  2. Clone các source code cần thiết để train model - [AlexyAB/darknet](https://github.com/AlexeyAB/darknet)
  3. Set up lại các file cần thiết và tài nguyên để chuẩn bị cho việc training
      + Chuẩn bị files yolo.names chứa tên các classes sẽ được detect trong bộ datasets, file train.txt chứa các path files trong tập train, file valid.txt chứa các path files trong tập valid, file yolo.data chứa tên file set up cần thiết cho tập train
      + File Config để set up lại, cụ thể vì dataset của chúng em khá lớn, nên trong quá trình training, phải set up lại khá nhiều lần mới có thể train thuận lợi được.
      + Các thông số mà em tinh chỉnh có ý nghĩa ảnh hưởng tới quá trình trainning như sau:
          + **width, height(kích thước network)**: các bức ảnh chúng em đưa vào đề sẽ được yolov4 resize nó lại trước khi trainig, tuy nhiên vẫn giữ nguyên tỉ lệ bức ảnh.
          + **batch**: nếu hoàn thành đủ số lượng batch được set up trước thì tính là hoàn thành 1 iterations
          + **subvisions:** batch/subvision là số lượng ảnh được load vào cùng một lúc khi xử lý
          + **max_batches:** số lượng iterations cần phải hoàn thành để kết thúc trainning
          + **classes:** số lượng class có trong datasets (cố định trong suốt quá trình train)
          + **filters** (cố định trong suốt quá trình train)
          
<p align ="middle">
  <img src="https://raw.githubusercontent.com/lphuong304/CS114.L21/byPhun/FINAL_PROJECT/svg_report/edit_Config.svg" />
</p>

  3. Dowload file pretrain weights **(yolov4.conv.137)** cho lần training model đầu tiên.
  4. Chỉnh sửa source code trong file `detector.c` để model sẽ tự động tính mAP sau khi traninig được `1/10 iteration` và `lưu weights` sau khi train được `1000 ierations`  
  5. Training.
  6. Sử dụng file 
* Nhận xét về khó khăn và cách giải quyết trong quá trình Training Model Yolov4:       
  * Quá trình Training diễn ra rất chậm, **nguyên nhân:** số lượng data nhiều, tuy nhiên số lượng hình ảnh được xử lý cùng một lúc trong quá trình training model là `2` nên tốn thời gian rất lâu.
   
<span>&#8594;</span> **Giải pháp**: Như đã giải thích từ đầu, đây là một điều không thể tránh khỏi nhầm tránh lỗi `CUDA out of memory`.
  * Quá trình Training hay bị crashed đột ngột, dẫn đến phải train lại, **nguyên nhân:** file path dẫn đến tập tin có vấn đề, ví dụ đối với các file có tên như, tên file có dấu, tên file có dấu cách.
   
<span>&#8594;</span> **Giải pháp**: Tìm và xóa các file như trên, do số lượng file không nhiều nên chúng em list ra trong một file txt và dùng chức năng search để xóa bằng “cơm”.

<span>&#8594;</span> Model training khi train đến iteration từ 46000 trở đi không có dấu hiệu giảm nên chúng em quyết định dừng train và dùng các file weights đã train được đem đi test model

* **Đánh giá Model yolov4:**  
  * Model Yolov4 sẽ được đánh giá dựa trên hai thông số sai: **avg_loss** và **mAP**, nhưng ở đây. để tập trung vào phần so sánh với model Faster R - CNN ở phần sau, nhóm sẽ chỉ tập trung vào chỉ số **mAP** cũng như **AP, AP50, AP75** - các thước đo phỏ biết nhất hiện nay để đánh giá một model objects detection.
<p align ="middle">
  <img src="https://user-images.githubusercontent.com/55471582/128653722-47833fa5-b22c-4bd1-a4b6-42287367f4ed.png" />
</p>
<div align = "center">Đánh giá Model Yolov4 trong bài toán Object Detection sử dụng backbone CPSDarknet53</div>

  * Để biết vì sao chúng em sử dụng mAP để đánh giá model Yolov4, chúng em xin trình bài các khái niệm liên quan có ý nghĩa quan trọng như sau:
    * **IoU**: độ do overlap giữa các bbox, cụ thể là giữa *grounth truth bounding box - bao quanh chính xác bbox của vật thể - là bbox mà chúng em đã lable* với *bounding box mà mô hình dự đoán*.
    * **AP**: là chỉ số có quan hệ mật thiết với chỉ số *precision(phần trăm các bbox được dự đoán là đúng)* và *recall (tỉ lệ phần trăm các bbox được dự đoán đều chính xác)*
<p align ="middle">
  <img src="https://user-images.githubusercontent.com/55471582/128654429-26907296-9b3c-4c68-8600-cc44bf76f59c.png" />
</p>
<div align = "center">Minh họa cách tính các chỉ số như precision, recall, IoU</div>

<p align ="middle">
  <img src ="https://user-images.githubusercontent.com/55471582/128654434-7d2f0aa2-eb6f-4a43-8868-f0f3570b6181.png" />
</p>
<div align = "center">Sơ đồ trực quan cách tính AP dựa vào chỉ số precision và recall <br>AP là Average Precision - độ chính xác trung bình </br></div>

  * **AP50**: là độ chính xác với IoU = 0.5
  * **AP75**: là độ chính xác với IoU = 0.75
  * IoU có ý nghĩa quan trọng đối với chỉ số mAP và việc lựa chọn giá trị của IoU sẽ ảnh hưởng đến kết quả đánh giá của model. Trong các bài toán nhận diện vật thể, chúng ta tính toán chỉ số `precision` và `recall` với một ngưỡng IoU cho trước, ví dụ đơn giản nhất là nếu ta cho ngưỡng IoU bằng `0.4` và chỉ số IoU sau khi tính toán trên bbox được dự đoán là `0.5` thì ta tính rằng bbox được dự đoán đó là **đúng**, tuy nhiên nếu đặt ngưỡng IoU bằng `0.6` thì  với chỉ số IoU sau khi tính toán trên bbox được dự đoán là `0.5` thì bbox được dự đoán đó là **sai**.
  * Model yolov4 trực quan hóa các chỉ số đánh giá qua từng iterations trong quá trình train bằng một chart với trục `x` là các `iterations` trong quá trình training, trục `y` thể hiện các đánh giá tương ứng với `avg_loss` và `mAP` trong suốt quá trình train, trong đó `mAP` sẽ được model tính toán lại theo sau khi train được 1/10 iteration.
  * Khó khăn khi đánh giá model yolov4:
    * Mặc định ban đầu, do chính sách của colab notebook, các session khi train liên tục bị crashed giữa chừng, làm ảnh hưởng đến quá trình nắm bắt độ chính xác của model.
    * Nhóm đã có sai sót ban đầy do chủ quan nên đã set up theo mặc định là model sẽ cập mAP sau khi train hết 4 iterations một cách liên tục và vì bị crashed thường xuyên cho nên sẽ tốn thời gian gây khó khăn lớn trong trong quá trình tính được mAP.
   
    <span>&#8594;</span> **Giải pháp:** Sau khi train được 45000 ierations đầu tiên, nhóm fix lại source code file `detector.c` để model tính lại map sau khi train được `1/10` iterations, giúp model tính mAP nhanh hơn.
    
<p align ="middle">
  <img src="https://user-images.githubusercontent.com/55471582/128661000-1a745aa5-a218-4101-a228-65e2433abf26.png" />
</p>
<div align = "center">Yolov4 visualize độ chính xác thể hiện qua chart.png
</div>

* **Quá trình Detect Video trên tập video test:**  
* Video được detect phải có những thông tin chính xác với Ouput bao gồm: bbox xác định vật thể, class_name của vật thể, confidence-score, tổng số lượng sản phẩm xuất và tổng giá sản phẩm xuất hiện suốt video. 
  1. Đưa về bài toán **DeepSort** sử dụng file pretrained weights đã train trên với model Yolov4.
    * Mỗi object sẽ được gán một *track-id* riêng để phân biệt các sản phẩm.
    * Thuật toán phải them dõi đối tượng và gán có định một trạc-id suốt video.
    
    <span>&#8594;</span> Xác định yêu cầu: Nhận diện đúng các sản phẩm, số lượng vật thể sẽ được lưu vào và sẽ được cộng dồn khi phát hiện vật thể cùng khác cùng sản phẩm.
    
  2. Tham khảo source code từ repository [yolov4-deepsort](https://github.com/theAIGuysCode/yolov4-deepsort)
  3. Chỉnh sửa, thêm function:
      *   function và flag `--count` để đếm sản phẩm, lưu lại và cộng dồn vào trong suốt quá trình detect video, tính tổng giá: [line 271 - 290](https://github.com/lphuong304/CS114.L21/blob/f04739b149bccfda901220e77cc67d21a8751a9f/FINAL_PROJECT/deepsort_to_detect/object_tracker.py#L271)
      *   thêm function convert files giá excel sang format dict: [line 98 - 115](https://github.com/lphuong304/CS114.L21/blob/f04739b149bccfda901220e77cc67d21a8751a9f/FINAL_PROJECT/deepsort_to_detect/object_tracker.py#L98)
      *   xuất bill: [line 268 - 271](https://github.com/lphuong304/CS114.L21/blob/f04739b149bccfda901220e77cc67d21a8751a9f/FINAL_PROJECT/deepsort_to_detect/object_tracker.py#L268)
  5. Download file weights sau khi train để đem về máy local detect. Sử dụng files weights vừa mới tải về để save thành model sử dụng để detect video. Nếu sử dụng file weights mới, thì phải có bước này. Chạy file code save_model.py, gọi flag `--model` và lưu thành tên model muốn lưu - ví dụ command bên dưới lưu thành model tên `yolov4`
  ```python save_model.py --model yolov4``
  5. Ví dụ khi tiến hành detect video test3.mp4 để và lưu kết quả detect thành video demo8.avi nằm trong folder `./data/video`, ta chạy command line như sau:
  `python object_tracker.py --video ./data/video/test12.mp4 --output ./outputs/demo8.avi --model yolov4 --count`
  
* **Model detect trên các mẫu dữ liệu test:**
  * *Trường hợp mẫu dữ liệu mà model phần tích sai:*
  * *Trường hợp mẫu dữ liệu mà model phần tích đúng:*
* **Phân tích các Mẫu dữ liệu Video được detect:**
  * *Trường hợp mẫu dữ liệu mà model phần tích sai:*
    * Nguyên nhân:
      + Camera đặt cách xa sản phẩm hơn điều kiện ràng buộc quy định trước đó (trong khoảng từ 5 – 20cm)
      + Các sản phẩm như bơ thực vật Meizan, bơ Marrgarin có màu sắc và hình dạng kết cấu sản phẩm khá giống nhau nên dẫn đến model detect nhầm lẫn. Ngoài ra các sản phẩm như có kết cấu hình dạng giống nhau như sốt mayonnaise chai 260g
      + Do hình ảnh dữ liệu trong tập không cân bằng nhau nên model có xu hướng detect ra những class có số lượng hình ảnh nhiều hơn và nhận biết tốt hơn, dẫn đến sự nhầm lẫn như trên.
      
<span>&#8594;</span>Model bị **overfitting.**
   * *Trường hợp mẫu dữ liệu mà model phần tích đúng:*
     * Nguyên nhân:
      + Video có các tiêu chí điều kiện mà nhóm đã thống nhất sẽ chụp gom dữ liệu từ trước đó
      + Các sản phẩm trong clip là những sản phẩm có màu sắc khá nổi trội và hình dạng đặc trưng, không giống như những sản phẩm khác trong bộ dataset mà nhóm đã thu thập. 
      + Số lượng hình ảnh của các class sản phẩm trong clip nhiều (đều khoảng từ 100 – 150 tấm) nên model có nhiều dữ liệu để học và detect tốt hơn.

## Model Faster R- CNN:
* Trong bài toán này, chúng em sử dụng mô hình Faster R-CNN trên Detectron2 do Facebook Reseach xây dựng.
* Detectron2 được xây dựng bởi Facebook, một thư viện cung cấp mã nguồn mở để training model trên custom dataset của nhóm. Model zoo của Detectron2 rất phong phú, có thể sử dụng để pretrained và chúng em quyết định lựa chọn model Faster R-CNN để pretrained.
* Faster R-CNN là một mô hình với cấu trúc gần như tương tự với R-CNN và được cải thiện đáng kể về tốc độ training, sau khi trích xuất đặc trưng ảnh Faster R-CNN không sử dụng thuật toán để tìm ra khu vực có khả năng chứa các đối tượng mà thêm hẳn một mạng CNN để tìm ra nó. 
<p align ="middle">
  <img src="https://user-images.githubusercontent.com/55471582/128677840-c47ade54-484f-419a-8855-cb9c2c218f8f.png" />
</p>
<div align = "center">Kiến trúc của model Faster R - CNN
</div>

* Chúng em sử dụng file Pretrained Weights X-101-32x8d.pkl để tiếp tục train cho model của mình (cũng như với file pretrained – weights yolov4, do dataset của chúng em nhỏ nhưng khá tương đồng nhưn với datasets COCO dùng để train model data for objects detection nên sử dụng file Pretrained Weights giúp tiết kiệm thời gian train lại toàn bộ model từ đầu)

<p align ="middle">
  <img src="https://user-images.githubusercontent.com/55471582/128682141-b7468fdf-6e93-4e88-8059-a6ca64f64ed9.png" />
</p>

* **Quá trình chuẩn bị dữ liệu cho model(tự code):**
  1. Từ dữ liệu có sẵn đã được labeled sẵn khi train bằng model yolov4, nhóm sẽ convert các files annotations yolo format \*.txt sang files annotations VOC format \*.xml, chúng em có tham khảo từ source code github ở đây [yolo2voc](https://github.com/hai-h-nguyen/Yolo2Pascal-annotation-conversion)
  2. Convert files từ format files annotations VOC format \*.xml sang format file annotation COCO \*.json, chúng em có tìm và tham khảo được source code từ repository [voc2coco](https://github.com/yukkyo/voc2coco), quá trình chuẩn bị tài nguyên files khá rườm rà
    * Hai tập labels train và txt chứa các files annotaions \*.xml đã được labels trước đó
    * Một file train.txt chứa tên file \*.xml có trong tập train
    * Một file valid.txt chứa tên file \*.xml có trong tập valid
    * Một file txt chứa path của các file có trong tập train
    * Một file txt chứa path của các file có trong tập valid
    * Một file classes.txt chứa các nhãn theo đúng thứ tự.
  3. Khác với yolov4, Faster R - CNN sử dụng detectron2 yêu cầu hai folder train và valid nằm trong hai folder riêng biệt với nhau <span>&#8594;</span> Giải pháp: Sử dụng module split-folders để chia theo tỉ lệ **80/20**

* **Quá trình chuẩn bị dữ liệu cho mode(có sự hỗ trợ của Roboflow Team):**
* Roboflow team có hỗ trợ để chuẩn bị các chuyển đổi dữ liệu từ file format VOC \*.xml sang flie format COCO \*.json.
* Khó khăn: Server của Roboflow Team có thể xử lý được data 17.3 GB của chúng em, nhưng phải trả phí, mua gói premium (999$/tháng) <span>&#8594;</span> Giải pháp: SGmail trình bày hoàn cảnh hiện tại và mong nhận được sự hỗ trợ, được roboflow cấp cho một account premium.

<p align ="middle">
  <img src="https://user-images.githubusercontent.com/55471582/128686116-18070d8d-2644-46cd-830e-8420d9febd62.png" />
</p>

* **Quá trình training - dựa trên basline Detectron2 của Roboflow Team:**
* Upload dữ liệu lên google drive
* Đặc biệt riêng đối với detectron2, đối với mỗi tập dataset ta phải dùng hàm **register_coco_instances()** để “đăng ký” thì mới model mới có thể hiểu để training, đối với các video mẫu dùng để detect sau này, ta cũng thực hiện đăng ký tương tự, mỗi tập dataset ứng ứng một tên đăng ký riêng.
* Chỉnh sửa file config
* Các thông số chúng em tinh chỉnh trong lần training đầu tiên(dựa trên file config ban đầu là **faster_rcnn_X_101_32x8d_FPN_3x.yaml**
  * IMS_PER_BATCH = 4 
  * MAX_ITERS = 398000
  * CLASSES = 200 ( = 199 + 1)
  * EVAL_PERIOD = 500
  * BATCH_SIZE_PER_IMAGE = 64
Nhận thấy model training nhanh, nhóm chỉnh sửa lại file config như sau:
IMS_PER_BATCH = 8 <span>&#8594;</span> Model chạy tốc độ tăng đáng kể.

* **Nhận xét về Khó khăn và Cách giải quyết trong quá trình Traning Model Faster R- CNN sử dụng framework Detectron2:**
*  Quá trình Training diễn ra nhanh hơn so với model yolov4, tuy nhiên vẫn còn lâu và chậm nguyên nhân: số lượng data nhiều, dù số lượng hình ảnh được load trong cùng một batch là 8 gấp đôi so với model yolov4, nhưng với kích thước data lớn thì cũng không thực sự khả quan.
<span>&#8594;</span> **Giải pháp:** Như đã giải thích từ đầu, đây là một điều không thể tránh khỏi nhầm tránh lỗi CUDA out of memory. Khi tăng img_per_batch > 8 thì sẽ xảy ra lỗi như trên
* Quá trình chuẩn bị file phức tạp, mỗi lầ muốn train, test trên một tập dữ liệu mới phải đăng ký. 

* **Đánh giá Model:**
* Faster RCNN sử dụng framework detectron2 visualize độ chính xác thể hiện qua TensorBoard
* Model Faster R-CNN sử dụng framework detectron2 sử dụng các chỉ số mAP, AP50, AP75 để đánh giá độ dự đoán chính xác của model.


<p align ="middle">
  <img src="https://user-images.githubusercontent.com/55471582/128689134-704036c5-7aba-48bc-b29c-0a0b40ae7e8b.png" />
  <img src="https://user-images.githubusercontent.com/55471582/128689155-5b284d4d-3d08-41c6-a76f-c5d63285d1be.png" />
</p>
<div align = "center">Chỉ số mAP50 sau khi train được 46000 iterations
</div>

* **Quá trình Detect trên tập Video Test:**
* Việc sử dụng thêm model FASTER R-CNN với mục đích chủ yếu là để so sánh performance với model yolov4 nên chúng em sẽ chỉ dừng ở bước detect được trên video.
* Sử dụng framework có sẵn detectron2 của facebook research để detect (thao tác ngay trên colab)
* Sử dụng hàm register_coco_instances() để đăng ký dataset cho video chuẩn bị được detect
* Khó khăn: detectron2 của facebook reseach chỉ cung cấp visulize detect vị trí vật thể, không hiện class_name của vật thể đó nếu class không nằm trong các class_names có sẵn trong COCO dataset (chỉ hiện thỉ bbox và confidence score) <span>&#8594;</span> **Giải pháp:** Thay đổi MetaData mặc định của detectron2, “đăng ký” một metadataset chứa thông tin của tập dataset bao gồm name_classes.
* Sử dụng file weights đã train từ trước và file video tests, tiến hành detect.

* **Phân tích Trên các mẫu được Detect:**
* Trong phần trên, chúng em đã không phân tích dựa trên tiêu chí các mẫu dữ liệu video test nào mà model faster rcnn detect đúng hay sai, mà sẽ detect lại các mẫu dữ liệu video mà model yolov4 đã detect ở phần trước để đưa ra nhận xét cũng như so sánh:
    * Model Faster R – CNN detect tốt hơn so với model yolov4, mặc dù khi so sánh chỉ số AP50 khi training đến iteration 46k (model yolov4 – 98.4%, model faster rcnn – 99.92% ) chênh nhau không nhiều, các sản phẩm model yolov4 không detect ra trên video như Mì Hảo Hảo Sa Tế Hành, Hộp Cá Sốt Cà 3 Cô Gái,... Thì model faster rcnn thực hiện tốt điều đó.
    * Model Faster R – CNN giải quyết được tốt hơn vấn đề phân biệt các sản phẩm có màu sắc và hình dạng tương đối giống nhau như bơ thực vật Meizan, bơ Marrgarin,....
Bouding Box các vật thể như khi xác định localization của vật thể chính xác hơn.
    **Nguyên nhân:** Do model faster rcnn train đến ieration 325000 nên cải thiện và nắm bắt đặc trưng dữ liệu tốt hơn. 

## So Sánh Hai Model:

<p align="center">

</p>


| Các tiêu chí | Yolov4 | Faster R – CNN sử dụng framework detectron2 |
| ---          | ---    | ---                                         |
| Tài nguyên phục vụ cho model | Chỉ cần hai format file quan trọng và chủ chốt: files hình ảnh và file annotations \*.txt(tất cả đều chung một folder. Quy trình chuẩn bị tương đối đơn giản. | Cần hai dạng format files cơ bản và chủ chốt: files hình ảnh và files annotation \*.json. Quá trình chuẩn bị files khá rườm rà và phức tạp. |
| Tốc độ Training | Chậm, càng về sau càng chậm (do quy định hạn chế tài nguyên GPU của Google Colab), trung bình 1000 iteration mất 3h để training xong | Tốc độ nhanh đáng kể so với khi training model yolov4, tối thiểu tăng gấp đôi do (do đã tăng số lượng hình ảnh trong mỗi batch) |
| Bỏ sót Objet | Có, bỏ sót object số lượng nhiều hơn model faster rcnn | Có, nhưng số lượng không đáng kể |
| Performance (mAP50) - Chỉ xét đến iteration 46k | 98.37% | 99.92% |
| Các bbox detect bị chồng chéo nhau | Có, nhưng các trường hợp xảy ra rất ít. | Số lượng trường hợp xảy ra nhiều hơn so với model yolov4 |
| Nhiều sản phẩm xuất hiện trong một khung hình | Không tốt, đa số các trường hợp Bbox xác định vị trí bao quát luôn cả sản phẩm khác. | Tốt hơn model yolov4 |
| Tốc độ nhận diện Object | Tốc độ nhận diện xử lý chậm hơn model Faster R- CNN | Tốc độ nhận diện xử lý nhanh |

<a name="ungdung"></a>
<h1>5. Ứng Dụng và Hướng Phát Triển </h1>


<h2> Bài toán đặt ra </h2>
<p> Bài Toán “Nhận Diện Sản Phẩm Thương Mại” mà nhóm em hướng đến để giải quyết là bài toán có hướng phát triển và ứng dụng cao, đặc biệt là trong thời đại công nghệ ngày càng phát triển và “xâm nhập” vào thị trường mua sắm. Nếu model được cải tiến để giải quyết bài toán với model có độ chính xác cao, thì bài toán của chúng em sẽ góp phần quan trọng trong việc xây dựng mô hình mua sắm công nghệ cao, điển hình với dự án của một số công ty lớn sau: </p>

<ul>
  <li> Chuỗi của hàng Amazon Go của công ty Amazon với slogan “Just Walk Out”. </li>
  <li> Dự án quầy thanh toán không thu ngân của công ty Abto Software (Abto Cashierless Checkout). </li>
  <li> .... </li>
</ul>
 
 
<h2> Hướng cải tiến </h2>
<p> Như đã nói ở trên, để có thể giải quyết bài toán “Nhận Diện Sản Phẩm Thương Mại” ở mức độ ứng dụng được vào trong các mô hình mua sắm công nghệ cao, thì với model như trên của chúng em cần phải có những hưỡng cải tiến như sau: </p>

<ul>
  <li> <strong>Về Data</strong> </li>
  <ul> 
    <li> Tăng sự đa dạng và số lượng, loại sản phẩm nhiều hơn, ngoài ra phải thường xuyên thu thập data vì mẫu mã sản phẩm, giá cả liên tục thay đổi, ngoài ra cũng phải đáp ứng được các chương trình khuyến mãi của các chuỗi cửa hàng,... </li>
    <li> Quy trình thu thập data phải diễn ra chặt chẽ, có sự đầu tư về phần cứng thiết bị, ví dụ như set up một phòng lab riêng biệt chỉ dành cho việc chụp hình các sản phẩm, các camera set up có giá đỡ cố định ở các góc, ánh sáng điều kiện, phù hợp với bối cảnh thực tế, chú ý đến vấn đề tạo nên một balanced data,... => Clean Data </li>
    <li> Tăng cường dữ liệu, sử dụng các kỹ thuật như Data Augmentation (blur, gray scale, cutout, cutmix, rotate,...),...việc lựa chọn các bước tăng cường dữ liệu rất quan trọng, không phải phương pháp nào cũng tốt cho tập dữ liệu. </li>
  </ul>
  
  <li> <strong>Về Model</strong> </li>
  <ul>
    <li> Model trên của chúng em bị overfitting, nên phần cải tiến data như trên có thể sẽ giúp model well generalize. </li>
    <li> Ngoài ra, cũng còn một số biện pháp cải thiện model như điều chỉnh độ phức tạp lại của networks, thay đổi các tham số, sử dụng kỹ thuật early stopping,... </li>
    <li> Việc sử dụng pretrained model cũng ảnh hưởng tới kết quả detect, nên cân nhắc việc sử dụng pretrained model. </li>
  </ul>
  
  <li> <strong>Để bài toán được mở rộng và phát triển, chúng em có ý tưởng thêm một số chức năng như sau:</strong> </li>
  <ul>
    <li> Sử dụng bảng điện tử trực truyết để người dùng có thể theo dõi tình trạng đơn hàng ở quầy thanh toán, tăng tương tác giữa người dùng với hệ thống,... </li>
    <li> Phát triển một ứng dụng điện thoại kết nối với dữ liệu mua sắm của người dùng, để người dùng tiện tra cứu thông tin, giá hóa đơn, sản phẩm,.. Tuy nhiên cũng đảm bảo bảo mật thông tin người dùng. </li>
  </ul>
</ul>


