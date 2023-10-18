# DRF(Django Rest Framework)

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

 - URL(Uniform Resource Locator) : 웹에서 주어진 리소스의 주소
   - http => Scheme
   - www.example.com:80 => Domain Name
   - /path/to/myfile.html => Path to the file
   - ?key1=value&key2=value2 => Parameters
   - #SomewhereInTheDocument => Anchor
   - http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomeWhereInTheDocument

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
 - HTTP response status codes
   - Informational responses(100-199)
   - Successful responses(200-299)
   - Redirection messages(300-399)
   - Client error responses(400-499)
   - Server error responses(500-599)

## Django REST framework

 - Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리

### Serialization(직렬화)

 - 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정