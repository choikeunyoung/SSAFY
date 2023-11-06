# DB 심화

## DB 관계 종류

 - 1:1
   - A 테이블 하나의 레코드가, B 테이블의 하나의 레코드와 연결된 경우
   - ex) 각 사용자는 하나의 프로필을 가짐(사용자:프로필 = 1:1)
   - ex2) 

 - 1:N
   - 
 - M:N
   - 

## Many to on relationships

 - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계
 - comment(N) : article(1) 관계 (N:1)
 - N쪽이 외래키를 가지고 있어야 한다.

### ForeignKey()

 - N:1 관계 설정 모델 필드

## 댓글 모델 정의

 - ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형으로 작성하는 것을 권장
 - ForeignKey 클래스를 작성하는 위치와 관계없이 외래 키는 테이블 필드 마지막에 생성됨
 - ForeignKey(to, on_delete)
   - 외래 키가 참조하는 객체(1)가 사라졌을 때, 외래 키를 가진 객체(N)를 어떻게 처리할 지를 정의하는 

### 역참조 사용 예시

 - article.comment_set.all() : 모델 인스턴스 + related manager(역참조 이름) + QuerySet API
 - related manager : N:1 혹은 M:N 관계에서 역참조 시 사용하는 매니저