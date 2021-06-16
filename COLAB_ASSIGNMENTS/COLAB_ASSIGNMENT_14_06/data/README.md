Link data:
Vì để quá trình train diễn ra nhanh chóng và thuận tiện, nhóm em quyết đã co-op với nhóm bạn Văn Viết Hiếu Anh [link github nhóm bạn](https://github.com/vanviethieuanh/CS114.L21), lấy data của nhóm bạn làm data test và ngược lại nhóm bạn cũng sẽ lấy data mà chúng em crawl để làm data test.
* Data train (là data mà chúng em đã crawl từ 6 trang tin hôm trước) : [link](https://github.com/lphuong304/CS114.L21/blob/main/COLAB_ASSIGNMENTS/COLAB_ASSIGNMENT_09_06/submit.csv)
* Data test (chúng em sẽ lựa chọn một trang tin chính thống và một trang tin châm biếm từ nhóm bạn mà không có trong data train của chúng em): [link]()

* Tổng quan về bộ data:
 + **Data train**: Gồm 6 trang tin (*3 châm biếm, 3 chính thống*) được crawl từ 01/01/2018 đến nay.
 

| Trang      |Link                       | Số bài báo | Thể loại    | 
|------------| ------------------------- | ---------- | ------------| 
|Clickhole   | https://clickhole.com/    | 2520       | Is_Sarcasist| 
|Daily Bonnet| https://dailybonnet.com/  | 1325       | Is_Sarcasist| 
|The Babylon Bee|https://babylonbee.com/ | 5080       | Is_Sarcasist| 
|CBS News    |  https://www.cbsnews.com/ | 44877      | Isn't_Sarcasist | 
|Fortune     |  https://fortune.com/     | 2730       | Isn't_Sarcasist | 
|The New York Times|https://www.nytimes.com/| 61611   | Isn't_Sarcasist | 

* Total: `118143`
    +   Is_Sarcasist: `8925`
    +  Isn't_Sarcasist: `109 218`

 + **Data test**: Gồm 2 trang tin (*1 châm biếm, 1 chính thống*) được lấy data nhóm bạn đã crawl.

| Trang      |Link                       | Số bài báo | Thể loại    | 
|------------| ------------------------- | ---------- | ------------| 
|The Hard Times   | https://thehardtimes.net/    | 5917      | Is_Sarcasist| 
|The Australian  |  https://www.theaustralian.com.au/ | 50151| Isn't_Sarcasist | 
* Total: `56066`
    +   Is_Sarcasist: `5917`
    +  Isn't_Sarcasist: `50151`
