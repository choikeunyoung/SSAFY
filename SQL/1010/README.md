# DB 기초

 - 조직화된 데이터의 모음
   - 프로그램에서 사용할 데이터를 구조화해서 저장만 해놓은 것
   - 저장, 조회, 삭제, 수정 등의 추가작업은 어떻게할까?
 - 일반적으로 DBMS(Database Management System)을 DB라 부름
 - 즉, 관리 시스템을 DB 라고 칭한다.

## DB의 종류

 1. 관계형 데이터베이스(RDBMS)
    - 데이터를 테이블, 행, 열 등으로 나누어 구조화 하는 방식
    - 테이브 간 관계를 설정하여 여러 데이터를 조작, 관리 할 수 있음
    - 데이터의 무결성(정확성, 일관성) 유지에 장점이 있음
      - 정확성 : 데이터가 정확한 값을 갖는 것(제약 조건에 위반은 없는가, 누락이 없는가, 중복은 없는가 등등)
      - 일관성 : DB 내의 모든 데이터가 일관된 상태를 유지하는 것
    - 단점
      - 테이블이 나뉘어져 있다.
        - 쿼리문이 복잡하다.
        - 대용량 데이터 처리가 어렵다.
      - 데이터 규모가 커지면 성능 개선을 해야한다.
        - 수평적 확장이 불가능하다.
        - 수직적 확장
          - 더 좋은 컴퓨터를 쓴다.
        - 수평적 확장
          - 여러 PC 에서 분산하여 처리한다.
          - 하나의 DBMS를 여러 서버에 분산하여 저장 및 처리
          - 이를 분산 데이터베이스(Distributed Database)

 2. 비관계형 데이터베이스(NoSQL)
    - 관계형 데이터베이스의 한계를 극복하기 위해 사용
        - 확장성 : 수직, 수평적 확장이 모두 가능하다
        - 유연성 : 스키마가 고정된 RDB 와 달리 스키마가 유동적이다.
          - 데이터의 구조를 유연하게 변경할 수 있다.

## Database

 - 체계적인 데이터 모음
 - 데이터 : 저장이나 처리에 효율적인 형태로 변환된 정보
 - 데이터를 저장하고 잘 관리하여 활용하는 기술이 중요해짐
   - 증가하는 데이터 사용량
   - 데이터 센터의 성장
 - Table은 데이터가 기록되는 곳
 - Talbe에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 있으며, 외래 키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만들 수 있음
 - 데이터는 기본 키 또는 외래 키를 통해 결합(join)될 수 있는 여러 테이블에 걸쳐 구조화 됨

### 기존의 데이터 저장 방식

 1. 파일 이용
    - 어디서나 쉽게 사용 가능
    - 데이터를 구조적으로 관리하기 어려움
 2. 스프레드 시트 이용
    - 테이블의 열과 행을 사용해 데이터를 구조적으로 관리가능
 3. 스프레드 시트의 단점
    - 일반적으로 100만 행까지만 저장가능
    - 단순히 파일이나 링크 소유 여부에 따른 단순한 접근 권한 기능 제공
    - 정확성
      - 만약 공식적 "부산" 지명이 "서울"로 바뀌면 모든 테이블 위치 값을 찾아서 업데이트 해야함
      - 찾기 및 바꾸기 기능을 사용해 바꿀 수 있지만 데이터가 여러 시트에 분산시 변경에 누락이 생기거나 문제가 발생

## DB의 구성요소

 - 개체(Entity), 스키마(Schema), 테이블(Table)
   - 저장하고자 하는 실제 객체나 개념을 정리한 것
   - 각 엔티티는 여러 속성(Attributes)으로 구성된다
   - ex) 서울 4반의 성별,나이에 따른 롤 티어를 분석하고 싶다.
     - 서울 4반 학생: 이름, 나이, 롤 티어 등등 < 엔티티

 - 스키마(Schema)
   - 엔티티와 속성들의 구조, 관계, 제약 조건 등의 정의 한 것
   - 엔티티들을 어떻게 구조화할 지(저장할 지) 논리적으로 설계한 것
   - ex) 서울 4반 학생
     - 이름 : 문자열로 저장
     - 나이 : 숫자로 저장
     - 롤티어 : 문자열로 저장
   - 테이블(Table)
     - 실제로 DB에 저장되는 객체
     - 구성 요소
       - 행(Row), 레코드(Record), 튜플(Tuple)
         - 가로 줄
         - 하나의 데이터 항목
       - 열(Column), 속성(Attribute), 필드(Field)
         - 세로 줄
         - 어떤 데이터를 저장할 것인지 나타냄

 - 속성(Attribute)
   - 엔티티가 가지는 항목으로, 저장하고 싶은 개체의 특정 항목을 의미함
 - 관계(Relationship)
   - 두 가지 이상의 엔티티 사이의 관계
   - ex) 추가적으로 서울 4반의 강사 정보를 관리하고 싶다.
     - 강사 정보를 따로 저장해야 한다.
       - 다 같이 저장하면, 중복이 매우 많이 발생한다!
     - 서울 4반 학생 - 강사 는 연관된 데이터. 관계가 있다고 말한다.


## Relational Database

 - 데이터 간에 관계가 있는 데이터 항목들의 모음
 - 테이블, 행, 열의 정보를 구조화하는 방식
 - 서로 관련된 데이터 포인터를 저장하고 이에 대한 액세스를제공
 - 관계 : 여러 테이블 간의 논리적 연결

## RDBMS(Relational Database Management System)

 - 관계형 데이터베이스를 관리하는 소프트웨어 프로그램
 - 데이터를 저장 및 관리를 용이하게 하는 시스템
 - 데이터베이스와 사용자 간의 인터페이스 역할
 - 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움

### SQLite

 - 경량의 오픈 소스 데이터베이스 관리 시스템
 - 컴퓨터나 모바일 기기에 내장되어 간단하고 효율적인 데이터 저장 및 관리를 제공


## SQL(Structure Query Language)

 - 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
 - 관계형 데이터베이스와의 대화를 위해 사용하는 프로그래밍 언어
 - SQL 키워드는 대소문자를 구분하지 않음
   - 대문자 작성을 권장
 - SQL Statements의 끝에는 세미콜론(;)이 필요
   - 각 SQL Statements을 구분하는 방법

### SQL 문을 사용하기 전 필수 지식

 - SQL 문(statement)
   - 데이터를 조작하거나 검색하는 작업을 수행하는 명령어의 집합
   - ex) SELECT, INSERT, UPDATE, DELETE 등
   - 여러 개의 절(clause)로 구성됨
 - SQL 절(clause)
   - SQL 문의 구성요소 중 하나
   - SQL 문의 구문 구조를 완성하기 위해 사용됨
   - ex) FROM, WHERE, GROUP BY, ORDER BY 등

## SQL Statements 예시

 ```SQL
    SELECT column_name FROM table_name;
 ```

 - SELECT Statement라 부름
 - SELECT, FROM 2개의 keyword로 구성

### 수행 목적에 따른 SQL Statements 4가지 유형

 1. DDL - 데이터 정의
 2. DQL - 데이터 검색
 3. DML - 데이터 조작
 4. DCL - 데이터 제어

 유형 | 역할 | SQL 키워드
 ---------|----------|---------
  DDL(Data Definition Language) | 데이터의 기본 구조 및 형식 변경 | CREATE, DROP, ALTER
  DQL(Data Query Language) | 데이터 검색 | SELECT
  DML(Data Manipulation Language) | 데이터 조작(추가, 수정, 삭제) | INSERT, UPDATE, DELETE
  DCL(Data Control Language) | 데이터 및 작업에 대한 사용자 권한 제어 | COMMIT, ROLLBACK, GRANT, REVOKE
  
  - Query
    - 데이터베이스로부터 정보를 요청 하는 것
    - 일반적으로 SQL로 작성하는 코드를 쿼리문(SQL문)이라 함


## Querying data

 - SELECT statement : 테이블에서 데이터를 조회
 - SELECT syntax
   - SELECT 키워드 이후 데이터를 선택하려는 필드를 하나 이상 지정
   - FROM 키워드 이후 데이터를 선택하려는 테이블의 이름을 지정

 - ORDER BY statement : 조회 결과의 레코드를 정렬
 - ORDER BY synatx
   - FROM clause 뒤에 위치
   - 하나 이상의 컬럼을 기준으로 결과를 (오름차순-ASC, 내림차순-DESC)정렬

### DISTINCT statement

 - 조회 결과에서 중복된 레코드를 제거
 - SELECT 키워드 바로 뒤에 작성해야 함
 - SELECT DISTINCT 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드를 지정

### WHERE statement

 - 조회시 특정 검색 조건을 지정
 - FROM clause 뒤에 위치
 - search_condition은 비교연산자 및 논리연산자(AND, OR, NOT)를 사용하는 구문이 사용됨

## Comparison Operators

 - 비교 연산자 : =, >=, <=, !=, IS, LIKE, IN, BETWEEN...AND
 - 논리 연산자 : AND(&&), OR(||), NOT(!)
 - IN Operator : 값이 특정 목록 안에 있는지 확인
 - LIKE Operator : 값이 특정 패턴에 일치하는지 확인(Wildcards와 함께 사용)
 - Wildcard Characters
   - "%" : 0개 이상의 문자열과 일치 하는지 확인
   - "_" : 단일 문자와 일치하는지 확인

### LIMIT clause

 - 조회하는 레코드 수를 제한
 - 하나 또는 두개의 인자를 사용 (0 or 양의 정수)
 - row_count는 조회하는 최대 레코드 수를 지정
 ```SQL
    SELECT select_list FROM table_name LIMIT [offset, ] row_count;
 ```

 ### GROUP BY clause

  - 레코드를 그룹화하여 요약본 생성 ( 집계 함수와 사용 )
  - Aggregation Functions(집계 함수)
    - 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
    - SUM, AVG, MAX, MIN, COUNT