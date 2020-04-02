# django-authdev #

## 專案介紹 ##

本專案AuthDev用來簡單示範如何利用Django的UserCreationForm及Form類別，來開發網站的登入驗證和註冊功能，可以搭配[[Django教學8][Django教學8]Django UserCreationForm實作網站登入驗證及註冊功能分享](https://www.learncodewithmike.com/2020/04/django-authentication-and-usercreationform.html)部落格文章來進行學習。

## 前置作業 ##

將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境，並且啟動本地端伺服器：

`$ pipenv shell`

`$ python manage.py runserver`

## 執行畫面 ##

開啟瀏覽器，在本地端伺服器的網址後面加上 /accounts (例：http://127.0.0.1:8000/accounts/) 後，即可看到登入畫面。

![Alt text](https://1.bp.blogspot.com/-MiuWqdxbu2E/XoX6j2VrBYI/AAAAAAAABwY/cqqVPj_tZawVbttxgUKJ1XzPDn3EVgoeACKgBGAsYHg/s1600/django_usercreationform_login.PNG "Optional title")

首先，需進行註冊的動作，如下畫面。

![Alt text](https://1.bp.blogspot.com/-XdcoqX8V3bQ/XoX6jxqHiwI/AAAAAAAABwY/1Yc8EB7rIVMazwbRyXAFCFzvzfNakHgwwCKgBGAsYHg/s1600/django_usercreationform_register.PNG "Optional title")

註冊成功並且登入後，即可看到首頁畫面。

![Alt text](https://1.bp.blogspot.com/-RYXNGWN88Js/XoX5o62r2fI/AAAAAAAABwA/sP_72RStI9AYcQVZjrk5kyIy7pr1uxPTwCKgBGAsYHg/s1600/django_usercreationform_homepage.PNG "Optional title")