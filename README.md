

[TOC]

## django - MTV(model, Template, View)

M : 데이터를 관리

T : 사용자가 보는 화면

V :  중간 관리자

---

urls -> View -> Template 

장고 프로젝트 생성

`$ pip install django` : pip로 장고 설치

`$ django-admin startproject intro .`(.이 없으면 폴더가 하나 더 생김)

intro는 프로젝트 네임



`$ python manage.py runserver` - 서버기동

---

.gitignore 설정

* 프로젝트에 .gitignore 추가
* 내용에 .idea/ 추가

----

`__init__.py`  프로젝트 초기화 시켜주는 파일, 손도 안댈거임.

`setting.py` 프로젝트 모든 세팅

`urls.py` 어떤뷰를 사용할지 방향을 설정해줌

`wsgi.py` :장고와 웹서버 연결해주는 통신프로토콜

---

` python manage.py startapp pages` - page라는 application 생성

`pages`내 파일 설명

`migration` - 모델 설계도

`admin` - 관리자용 페이지

`app` - 앱 정보

`models` -  데이터베이스 조작

`test` - 테스트코드

`views` - 컨트롤러 역할을 하고 view들을 조작함.

---

`intro - settings` 에 새로 생긴 앱을 `INSTALLED_APPS`에 추가 

위에 다가 `'pages'` 혹은 `'pages.apps.PagesConfig'`(후자를 권장)

* 순서

```
#local apps

#thrid party apps

#django apps
```

----

django의 한글화

`settings.py` - #



----

url 순서가 중요하다

위에서 아래로 읽어내려가기 때문





----

ensure line feed 설정

작성순서

1 views

2 urls

3 tempates

roo url은 위로 쌓아가는데

pages url은 아래로 내려감

장고템플릿랭귀지 {{}}

<https://docs.djangoproject.com/en/1.7/topics/templates/>

askii art

[http://patorjk.com/software/taag/#p=display&f=Big%20Money-ne&t=django](http://patorjk.com/software/taag/#p=display&f=Big Money-ne&t=django)

<http://artii.herokuapp.com/>

<http://artii.herokuapp.com/fonts_list>



----

GET은 DB에서 데이터를 꺼내는것 -> 변화 없음

POST는 DB를 조작(생성/수정/삭제)! ->DB변화 있음 - redirect



---

## static 파일

- image, css, js 별도의 처리없이 파일 내용을 그대로 보여줘도 되는 파일들
- django는 오로지 `app_name/static/` 만 바라 볼 수 있음