# DRF(Django Rest Framework)

 1. REST API
 2. DRF
 3. DRF with Single Model

## REST API

 - API : 애플리케이션과 프로그래밍으로 소통하는 방법
 - WEB API
   - 웹 서버 또는 웹 브라우저를 위한 API
   - 현대 웹은 Open API 들을 활용
   - 대표적인 API 서비스 목록
     - Youtube API
     - Google Map
 - REST(Representational State Transfer) : API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론(약속)
 - RESTful API : REST라는 설계 디자인 약속을 지켜 구현한 API
 - REST에서 자원을 정의하고 주소를 지정하는 방법
    1. 자원의 식별 : URL
    2. 자원의 행위 : HTTP methods
    3. 자원의 표현 : JSON 데이터, 궁극적 표현되는 데이터 결과물

 - Server 종류
   - 웹 서버
     - 정적인 컨텐츠(html, css, 이미지 등)를 제공하기 위한 서버
     - 대표적 : Nginx, Apache
   - API 서버
     - 클라이언트가 데이터를 요청하면, 해당 데이터를 제공하기 위한 서버
     - 일반적으로 API 서버는 WAS 위에서 동작
   - WAS(Web Application Server)
     - 동적인 컨텐츠를 제공하기 위한 서버
     - DB 서버, API 서버, 세션 관리, 보안 등을 모두 포함함
   - 이런 것들을 모두 합쳐서 하나의 애플리케이션 실행 환경을 제공하는 서버

 - Django 개발 서버
   - 웹 서버, WAS 이런 거 상관없이 그냥 개발 서버
   - 위 내용들은 모두 배포 시 구분되는 것!
   - 개발 서버와 별개로 생각해야 한다.

 - asgi.py, wsgi.py
   - Django 를 WAS로 배포할 수 있도록 도와줌
     - 동적 파일 처리, db 접근 등을 도와줌
   - 정적 파일
     - 일반적으로는 Nginx 등을 활용
     - `python manage.py collectstatic`

## REST 란?

 - REST API 디자인 가이드

    1. URL은 리소스를 표현해야한다.
       - 리소스명은 동사보다는 명사를 사용
       - 행위에 대한 표현이 들어가지 말아야한다.

    2. 행위는 HTTP Method 로 표현한다.
       - 잘못된 URL 구성 => GET /articles/1/delete/
       - 자원에 대한 표현 + 행위 => DELETE /articles/1 

    3. 슬래시 구분자(/)는 계층 관계를 나타내는 데 사용한다.
       - user 가 가지고 있는 devices 들을 조회

    4. 하이픈(-)은 URL 가독성을 높이는 데 사용

    5. 언더바(_)는 URL에 사용하지 않는다.

    6. URL 에는 소문자만사용해라
       - RFC3986(URI 문법 형식 표준)에서 대문자를 구별하도록 규정
       - 대소문자에 따른 다른 리소스로 인식

    7. 파일 확장자는 URI에 포함시키지 않는다.
       - Accept header 를 사용하여 확장자를 표현함

### 자원의 식별

 - URI(Uniform Resource Identifier) : 인터넷에서 리소스를 식별하는 문자열
 - URL(Uniform Resource Locator) : 웹에서 주어진 리소스의 주소
   - http => Scheme
   - www.example.com:80 => Domain Name
   - /path/to/myfile.html => Path to the file
   - ?key1=value&key2=value2 => Parameters
   - #SomewhereInTheDocument => Anchor
   - http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomeWhereInTheDocument

 - Schema(or Protocol)
   - 브라우저가 리소스를 요청하는 데 사용해야 하는 규약
   - URL의 첫 부분은 브라우저가 어떤 규약을 사용하는지 나타냄
   - 기본적으로 웹은 HTTP(S)를 요구하며 메일을 열기위한 mailto:, 파일을 전송하기 위한 frp: 등 다른 프로토콜도 존재

 - Domain Name
   - 요청 중인 웹 서버를 나타냄
   - 어떤 웹 서버가 요구되는 지를 가리키며 직접 IP 주소를 사용하는 것도 가능하지만, 사람이 외우기 어렵기 때문에 주로 Domain Name으로 사용

 - Port
   - 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문(Gate)
   - HTTP 프로토콜의 표준 포트 => HTTP - 80 / HTTPS - 443
   - 표준 포트들은 생략 가능

 - Path
   - 웹 서버의 리소스 경로
   - 초기에는 실제 파일이 위치한 물리적 위치를 나타냈지만 추상화된 형태의 구조를 표현

 - Parameters
   - 웹 서버에 제공하는 추가적인 데이터
   - & 기호로 구분되는 key-value 쌍 목록
   - 서버는 리소스 응답하기 전 이러한 파라티머를 사용하여 추가 작업을 수행할 수 있음

 - Anchor
   - 북마크를 나타내며 브라우저에 해당 지점에 있는 콘텐츠를 표시
   - fragment identifier(부분 식별자)라고 부르는 # 이후 부분은 서버에 전송되지 않는다

### 자원의 행위

 - HTTP Request Methods : 리소스에 대한 행위(수행하고자 하는 동작)를 정의
 - 대표 HTTP Request Methods
   1. GET : 서버에 리소스의 표현을 요청, GET을 사용하는 요청은 데이터만 검색해야 함
   2. POST : 데이터를 지정된 리소스에 제출, 서버의 상태를 변경
   3. PUT : 요청한 주소의 리소스를 수정
   4. DELETE : 지정된 리소스를 삭제
 - HTTP response status codes : 특정 HTTP 요청이 성공적으로 완료 되었는지 여부를 나타냄
   - Informational responses(100-199)
   - Successful responses(200-299)
   - Redirection messages(300-399)
   - Client error responses(400-499)
   - Server error responses(500-599)

### 자원의 표현

 - 지금까지 Django 서버는 사용자에게 페이지(html)만 응답하고 있었음
 - 하지만 서버가 응답할 수 있는 것은 페이지 뿐만 아니라 다양한 데이터 타입을 응답할 수 있음
 - REST API는 이 중에서도 JSON 타입으로 응답하는 것을 권장

## Django REST framework

 - Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리

### Serialization(직렬화)

 - 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정

## DRF with Single Model

 - 사전 제공된 drf 프로젝트 기반 시작
 - 가상 환경 생성, 활성화 및 패키지 설치
 - URL 과 HTTP requests methods 설계

### GET

 - 게시글 데이터 목록 조회하기
 - 게시글 데이터 목록을 제공하는 ArticleListSerializer 정의
 - ModelSerializer : Django 모델과 연결된 Serializer 클래스
 ```Python
  #  serializers.py
  from rest_framework import serializers
  from .models import Article

  class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
      model = Article
      fields = ('id', 'title', 'content', )

  # articles/url.py
  urlpatterns = [
    path('articles/', views.articles_list),
  ]

  # articles/views.py

  from rest_framework.response import Response
  from rest_framework.decorators import api_view

  from .models import Article
  from .serializers import ArticleListSerializer

  @api_view(['GET'])
  def articles_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
 ```

 - 'api_view' decorator
   - DRF view 함수에서는 필수로 작성되며 view 함수를 실행하기 전 HTTP 메서드를 확인
   - 기본적으로 GET 메서드만 허용되며 다른 메서드를 요청에 대해서는 405 Method Not Allowed로 응답
   - DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 작성

### GET - Detail

 - 단일 게시글 데이터 조회하기
 - 각 게시글의 상세 정보를 제공하는 ArticleSerializer 정의
 ```python
  # articles/serializers.py

  class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
      model = Article
      fields = "__all__"

  # articles/urls.py

  urlpatterns = [
    path('articles/<int:article_pk>/', views.article_detail), 
  ]

  # articles/views.py
  from .serializers import ArticleListSerializer, ArticleSerializer

  @api_view(['GET'])
  def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
 ```

### POST

 - 게시글 데이터 생성하기
 - 데이터 생성이 성공했을 경우 201 Created를 응답
 - 데이터 생성이 실패 했을 경우 400 Bad request를 응답

 ```python
  # articles/views.py
  from rest_framework import status

  @api_view(['GET', 'POST'])
  def article_list(request):
    if request.method == 'GET':
      articles = Article.objects.all()
      serializer = ArticleListSerializer(articles, many=True)
      return Response(serializer.data)

    elif request.method == 'POST':
      serializer = ArticleSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=Status.HTTP_400_BAD_REQUEST)
 ```

### DELETE

 - 게시글 데이터 삭제하기
 - 요청에 대한 데이터 삭제가 성공했을 경우는 204 No Content 응답
 ```python
  # articles/views.py

  @api_view(['GET','DELETE'])
  def article_detail(reqeust, articles_pk):
    article = Article.objects.get(pk=articles_pk)
    if request.method == 'GET':
      serializer = ArticleSerializer(article)
      return Response(serializer.data)
    
    elif request.method == "DELETE":
      article.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
 ```

### PUT

 - 게시글 데이터 수정하기
 - 요청에 대한 데이터 수정이 성공했을 경우 200 OK 응답
 ```python
  # articles/views.py

  @api_view(['GET', 'DELETE', 'PUT'])
  def article_detail(request, article_pk):
    
    elif reqeust.method == 'PUT':
      serializer = ArticleSerializer(aritcle, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
 ```

### raise_exception

 - is_valid()는 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생시키는 선택적 raise_exception 인자를 사용할 수 있음
 - DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환
 ```python
  @api_view(['GET', 'POST'])
  def article_list(request):
    ...
    elif request.method == "POST":
      serializer = ArticleSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
  # raise_exception 하면 HTTP_400_BAD_REQUEST 발생시킴
 ```