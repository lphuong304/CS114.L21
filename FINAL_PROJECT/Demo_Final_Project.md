

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
  4. Chỉnh sửa source code trong file `detector.c` để model sẽ tự động tính mAP sau khi traninig được `1/10 epoch` và `lưu weights` sau khi train được `1000 ierations`  
  5. Training.
  6. Sử dụng file 
* Nhận xét về khó khăn và cách giải quyết trong quá trình Training Model Yolov4:       
  * Quá trình Training diễn ra rất chậm, **nguyên nhân:** số lượng data nhiều, tuy nhiên số lượng hình ảnh được xử lý cùng một lúc trong quá trình training model là `2` nên tốn thời gian rất lâu.
   
<span>&#8594;</span> **Giải pháp**: Như đã giải thích từ đầu, đây là một điều không thể tránh khỏi nhầm tránh lỗi `CUDA out of memory`.
  * Quá trình Training hay bị crashed đột ngột, dẫn đến phải train lại, **nguyên nhân:** file path dẫn đến tập tin có vấn đề, ví dụ đối với các file có tên như, tên file có dấu, tên file có dấu cách.
   
<span>&#8594;</span> **Giải pháp**: Tìm và xóa các file như trên, do số lượng file không nhiều nên chúng em list ra trong một file txt và dùng chức năng search để xóa bằng “cơm”.

<span>&#8594;</span> Model training khi train đến iteration từ 46000 trở đi không có dấu hiệu giảm nên chúng em quyết định dừng train và dùng các file weights đã train được đem đi test model

* **Đánh giá Model yolov4:**  
<a name="ungdung"></a>
<h1>5. Ứng Dụng và Hướng Phát Triển </h1>



