# django-authdev #

## 專案介紹 ##

本專案AuthDev用來簡單示範如何利用Django的UserCreationForm及Form類別，來開發網站的登入驗證和註冊功能，可以搭配[[Django教學8]Django UserCreationForm實作網站登入驗證及註冊功能分享](https://www.learncodewithmike.com/2020/04/django-authentication-and-usercreationform.html)部落格文章來進行學習。

另外，Google登入的機制，是利用django-allauth套件來進行整合開發，在執行網站前，需先搭配[[Django教學13]Django Allauth套件整合Google登入驗證實作教學](https://www.learncodewithmike.com/2020/04/django-allauth-google.html)部落格文章，在Django Administration的部分，進行Google登入的相關設定，才不會發生錯誤。

在註冊成功時，會透過Gmail所提供的SMTP伺服器來發送通知信，同樣在執行時，需事先進行SMTP的設定，可以搭配[[Django教學16]建構Django網站該知道的Email寄送方式](http://www.learncodewithmike.com/2020/05/django-send-email.html)部落格文章來進行學習。

## 前置作業 ##

將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境，執行Django Migration(資料遷移)，並且啟動本地端伺服器：

`$ pipenv shell`

`$ python manage.py migrate`

`$ python manage.py runserver`

## 執行畫面 ##

開啟瀏覽器，本地端伺服器的網址後面加上 /login (例：http://127.0.0.1:8000/login) 後，即可看到登入畫面。

![Alt text](https://1.bp.blogspot.com/-cuX1yOtrb1A/XqG7cv8GRkI/AAAAAAAACA8/AZ19WVzguvgA91voS-sv3bLKtpuBX3pZwCPcBGAsYHg/s1600/django_allauth_google.PNG "Optional title")

可以透過一般登入或Google登入，如果為一般登入則先進行註冊的動作，如下畫面。

![Alt text](https://1.bp.blogspot.com/-XdcoqX8V3bQ/XoX6jxqHiwI/AAAAAAAABwY/1Yc8EB7rIVMazwbRyXAFCFzvzfNakHgwwCKgBGAsYHg/s1600/django_usercreationform_register.PNG "Optional title")

註冊成功並且登入後，即可看到首頁畫面。

![Alt text](https://1.bp.blogspot.com/-RYXNGWN88Js/XoX5o62r2fI/AAAAAAAABwA/sP_72RStI9AYcQVZjrk5kyIy7pr1uxPTwCKgBGAsYHg/s1600/django_usercreationform_homepage.PNG "Optional title")