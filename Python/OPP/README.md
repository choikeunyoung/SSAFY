# 객체지향 프로그래밍

 - 프로그램을 "데이터"와 "절차"로 구성하는 방식의 프로그래밍 패러다임

## 절차 지향 프로그래밍 특징

 - "데이터"와 해당 데이터를 처리하는 "함수(절차)"가 분리되어 있으며, 함수 호출의 흐름이 중요
 - 코드의 순차적인 흐름과 함수 호출에 의해 프로그램이 진행
 - 실제로 실행되는 내용이 무엇이 무엇인가 중요함

 ![절차 지향](https://velog.velcdn.com/images%2Fzzangzzong%2Fpost%2F5fdfc882-6ccd-4a3e-acce-f02384e4c639%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-03-07%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.23.42.png)

 - 하드웨어의 발전으로 컴퓨터 계산용량과 문제의 복잡성이 급격히 증가함에 따라 소프트웨어 충격이 발생

## 객체 지향 프로그래밍

 - 데이터와 해당 데이터를 조작하는 메서드를 하나의 객체로 묶어 관리하는 방식의 프로그래밍 패러다임

 절차 지향 | 객체 지향
 ----------|---------
  데이터와 해당 데이터를 처리하는 함수가 분리 | 데이터와 해당 데이터를 처리하는 메서드를 하나의 객체로 묶음
  함수 호출의 흐름이 중요 | 객체 간 상호작용과 메세지 전달이 중요

# 클래스(Class)

 - 파이썬에서 타입을 표현하는 방법
 - 코드의 재사용성

 ```python
    # 클래스 정의
    class Person:
        pass
    
    # 인스턴스 생성
    iu = Person()

    # 메서드 호출
    iu.메서드()

    # 속성(변수) 접근
    iu.attribute
 ```

## 객체(Object)

 - 클래스에서 정의한 것을 토대로 메모리에 할당된 것 "속성"과 "행동"으로 구성된 모든 것
 - 클래스로 만든 객체를 인스턴스 라고함

 ```python
    "Hello", "", "1" # 문자열의 인스턴스
    [1, 2, 3], [1, 2] [3] # 리스트의 인스턴스
 ```

 - 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
 - 속성(attribute) : 어떤 상태(데이터)를 가지는가?
 - 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

## 클래스 기본 활용

 - 생성자 함수
    - 객체를 생성할 때 자동으로 호출되는 특별한 메서드
    - __init__이라는 이름의 메서드로 정의되며, 객체의 초기화를 담당
    - 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값을 설정
  
    ```python
      def __init__(self, name):
          self.name = name
    ```

 - 인스턴스 변수
    - 인스턴스(객체)마다 별도로 유지되는 변수
    - 인스턴스마다 독립적인 값을 가지며, 인스턴스가 생성될 때마다 초기화됨

    ```python
        def __init__(self, name):
            self.name = name # 인스턴스 변수
        
        print(singer1.name) # 인스턴스 변수
    ```

 - 클래스 변수
    - 클래스 내부 선언된 변수
    - 클래스로 생성된 모든 인스턴스들이 공유하는 변수

    ```python
        class Person:
            blood_color = "red" # 클래스 변수

        print(singer1.blood_color) # 클래스 속성(변수) 접근
    ```
 
 - 인스턴스 메서드
    - 각각의 인스턴스에서 호출할 수 있는 메서드
    - 인스턴스 변수에 접근하고 수정하는 등의 작업을 수행

    ```python
        def singing(self):
            return f'{self.name}가 노래합니다.'

        print(singer1.singing()) # 인스턴스 메서드 호출
    ```

## 클래스 변수 활용

 - 인스가 생성 될 때마다 클래스 변수가 늘어나도록 설정할 수 있음

 ```python
    class Person:
        count = 0

        def __init__(self, name):
            self.name = name
            Person.count += 1
    
    person1 = Person("iu")
    person2 = Person("BTS")

    print(Person.count) # 2
 ```

## 클래스 변수와 인스턴스 변수

 - 클래스 변수를 변경할 때는 항상 클래스.클래스변수 형식으로 변경

 ```python
    class Circle():
        pi = 3.14

        def __init__(self, r):
            self.r = r
    
    c1 = Circle(5)
    c2 = Circle(10)

    print(Circle.pi) # 3.14
    print(c1.pi) # 3.14
    print(c2.pi) # 3.14

    Circle.pi = 5 # 클래스 변수 변경
    print(Circle.pi) # 5
    print(c1.pi) # 5
    print(c2.pi) # 5

    c2.pi = 5 인스턴스 변수 변경
    print(Circle.pi) # 3.14 (클래스 변수)
    print(c1.pi) # 3.14 (클래스 변수)
    print(c2.pi) # 5 (새로운 인스턴스 변수가 생성)
 ```

### 인스턴스와 클래스 간의 이름 공간(namespace)
 
 - 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
 
 - 인스턴스를 만들면, 인스턴스 객체가 생성되고 독립적인 이름 공간 생성
 
 - 인스턴스에서 특정 속성에 접근하면, 인스턴스 -> 클래스 순으로 탐색

 ```python
    # Person 정의
    class Person:
        name = 'unknow'

        def talk(self):
            print(self.name)
        
    # p1 인스턴스 변수가 정의되지 않아서 클래스 변수(unknown)가 출력됨
    p1 = Person()
    p1.talk() # unknow

    # p2 인스턴스 변수 설정 전/후
    # p2는 인스턴스 변수가 정의되어 (Kim)가 출력됨
    p2 = Person()
    p2.talk() # unknow
    p2.name = 'Kim'
    p2.talk() # Kim

    # Person 클래스 값이 Kim으로 변경된 것이 아닌 p2 인스턴스의 이름 공간에 name이 Kim으로 저장
    print(Person.name) # unknow
    print(p1.name) # unknow
    print(p2.name) # Kim
 ```

### 독립적인 이름공간을 가지는 이점

 - 각 인스턴스는 독립적 메모리 공간을 가지며, 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근이 불가능

 - 객체 지향 프로그래밍의 중요한 특성 중 하나로, 클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장

 - 클래스와 인스턴스는 다른 객체들과 상호작용에서 서로 충돌이나 영향을 주지 않고 독립적으로 동작한다.

 - 코드의 가독성, 유지보수성, 재사용성을 높이는데 도움을 줌

# 메서드

 - 행동의 역할을 함
 - 인스턴스 메서드, 클래스 메서드, 정적 메서드 존재

## 인스턴스 메서드

 - 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드

 - 인스턴스 메서드 구조
   - 클래스 내부에 정의되는 메서드의 기본
   - 반드시 첫 번째 매개변수로 인스턴스 자신(self)을 전달받음

    ```python
        class MyClass:

            def instance_method(self, arg1, ...):
                pass
    ```

 - self 동작 원리
    - upper 메서드를 사용해 문자열 'hello'를 대문자로 변경하기

        `hello.upper()`
    
    - 실제 동작은

        `str.upper('hello')`
    
    - str 클래스가 upper 메서드를 호출했고, 그 첫번째 인자로 문자열 인스턴스가 들어간 것이다.
    - 'hello'라는 문자열 객체가 단순히 어딘가의 함수로 들어가는 인자가 아닌 객체 스스로 메서드를 호출하여 코드를 동작하는 객체 지향적 표현이다.

## 생성자 메서드

 - 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드

 ```python
    class Person:

        def __init__(self):
            print("인스턴스가 생성되었습니다.")
    
    person1 = Person() # 인스턴스가 생성되었습니다.
 ```

## 클래스 메서드

 - 클래스가 호출하는 메서드 -> 클래스 변수를 조작 or 클래스 레벨의 동작을 수행
 - @classmethod 데코레이터를 사용하여 정의
 - 호출 시, 첫번째 인자로 호출하는 클래스(cls)가 전달됨

 ```python
    class MyClass:

        @classmethod
        def class_method(cls, arg1, ...):
            pass

    # 예시
    class Person:
        count = 0

        def __init__(self, name):
            self.name = name
            Person.count += 1

        @classmethod
        def number_of_population(cls):
            print(f'인구수는 {cls.count}입니다.')
    
    person1 = Person('iu')
    person2 = Person('BTS')

    Person.number_of_population() # 인구수는 2입니다.
 ```

## 스태틱(정적) 메서드

 - 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드 -> 주로 클래스와 관련이 있지만 인스턴스와 상호작용이 필요하지 않은 경우에 사용
 - @staticmethod 데코레이터를 사용하여 정의
 - 호출 시 필수적으로 작성해야 할 매개변수가 없음
 - 즉, 객체 상태나 클래스 상태를 수정할 수 없으며 단지 기능(행동)만을 위한 메서드로 사용

 ```python
    class MyClass:

        @staticmethod
        def static_method(arg1, ...):
            pass

    # 스태틱 메서드 예시

    class StringUtils:
        @staticmethod
        def reverse_string(string):
            return string[::-1]

        @staticmethod
        def capitalize_string(string):
            return string.capitalize()
    
    text = "hello, world"

    reversed_text = StringUtils.reverse_string(text)
    print(reversed_text) # dlrow, olleh

    capitalized_text = StringUtils.capitalize_string(text)
    print(capitalized_text) # Hello, world
 ```

### 메서드 정리

 - 인스턴스 메서드
   - 인스턴스의 상태를 변경하거나, 해당 인스터스의 특정 동작을 수행

 - 클래스 메서드
   - 인스턴스의 상태에 의존하지 않는 기능을 정의
   - 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

 - 스태틱 메서드
   - 클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행

### 각자의 역할

 - 클래스
   - 클래스 메서드
   - 스태틱 메서드

 - 인스턴스
   - 인스턴스 메서드

 ```python
    class MyClass:

        def instance_method(self):
            return 'instance method', self

        @classmethod
        def class_method(cls):
            return 'class method', cls

        @staticmethod
        def static_method():
            return 'static method'
 ```

# 참고

## 매직 메서드

 - 특별한 인스턴스 메서드
 - 특정 상황에 자동으로 호출되는 메서드
    - __str__(self), __len__(self), __lt__(self, other) ... 등