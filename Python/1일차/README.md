# 프로그래밍

  - 명령어들의 집합
  - 프로그래밍의 핵심 => 문제를 해결하는 매우 강력한 방법
  - 프로그래밍 언어 => 컴퓨터에게 작업을 지시하고 문제를 해결하는 도구

# 파이썬

  - 간결하고 읽기 쉬움
  - 다양한 응용 분야 => 데이터 분석, 인공지능, 웹 개발, 자동화
  - 커뮤니티 지원 => 언어가 살아남기 위해서는 사람들이 많이 사용하고 커뮤니티가 활성화 되야한다.

  - 파이썬은 인터프리터 언어로 구성되어 있다.
    - 프로그래머가 작성한 코드를 기계어로 변환하는 과정 없이 한 줄 해석해서 바로 명령어를 실행
    - 기계어로 변환하지 않기 때문에 빌드 과정 없이 실행 가능
    - 런타임 상황에서 한 줄씩 읽기 때문에 컴파일 언어에 비해 속도가 느리다.
    - 프로그램 수정이 간단


    ![Inter](https://velog.velcdn.com/images%2Fchldppwls12%2Fpost%2Fdd484a3d-bcd5-46e7-976a-ba2ceff4a815%2Fimage.png)

## 파이썬 인터프리터 사용하는 2가지 방법

  1. shell 이라는 프로그램으로 한 번에 한 명령어 씩 입력해서 실행
    
    ![Alt text](image.png)

  2. 확장자가 .py인 파일에 작성된 파이썬 프로그램을 실행


## 표현식과 값

  ![expre](https://thebook.io/img/006793/p033.jpg)
<br>
  - 표현식(Expression) : 값, 변수, 연산자 등을 조합하여 계산되고 결과를 내는 코드 구조 ( 5 * 21 - 4 )
  - 평가(Evaluate) : 표현식이나 문장을 순차적으로 평가하여 프로그램의 동작을 결정
  - 문장 : 실행 가능한 동작을 기술하는 코드
<br>
  ```python
    if a > b: # if a > b 는 문장 a > b 는 표현식
        break
    # 문장안에 표현식이 들어있음
  ```

## 데이터 타입

  - 값이 어떤 종류의 데이터인지, 어떻게 해석되고 처리되어야 하는지 정의

  ### Numeric Type : 숫자형 데이터로 사칙연산 뿐만 아니라 수학적 기능이 사용 가능한 타입

   #### int(정수)

   ```python
       a = 1 # int()
       b = 2 # int()
       print(0b10) # 2진수 b => binary
       # 2
       print(0o30) # 8진수 o => octal
       # 24
       print(0x10) # 16진수 x => hexadeciaml
       # 16
   ```

   #### float(실수) : 실수를 표현하는 자료형 실수에 대한 근삿값

   ```python
       print(2 / 3)
       # 0.6666666666
       print(5 / 3)
       # 1.6666666667s

       a = 3.2 - 3.1 # float()
       b = 1.2 - 1.1 # float()
       # 1. 임의의 작은 수 활용
       print(abs(a - b) <= 1e-10)
       # 2. math 모듈 활용
       import math
       print(math.isclose(a, b)) # True

       # 지수 표현 방식
       number = 314e-2 # 314 * 0.01
   ```
  - 컴퓨터는 2진수를 사용, 사람은 10진법을 사용
  - 10진수 0.1은 2진수로 0.0001100~ 무한으로 반복
  - 무한대 숫자를 저장할 수 없어 사람이 사용하는 10진법 근삿값을 표시
  - 이런 연산과정에서 예상치 못한 결과가 나타남
  - Floating point rounding error 발생

   #### complex(복소수)

   ```python
       a = 2 + 3j #complex()
       b = 1 + 4j #complex()
   ```

  ### Sequence Types : 순서가 유지되고, 정수로 인덱싱하며, 길이가 존재, 여러 값들을 순서대로 나열하여 저장하는 자료형

   1. 순서(Sequence) => 값들이 순서대로 저장 (정렬X)

   2. 인덱싱(indexing) => 각 값에 고유한 인덱스(번호)가 존재하며, 인덱스를 이용하여 특정 위치 값을 선택 수정 가능

   3. 슬라이싱(Slicing) => 인덱스 범위를 조절해 부분적인 값을 추출

   4. 길이(Length) => len() 함수를 사용하여 저장된 값의 개수(길이)를 구할 수있음

   5. 반복(Iteration) => 반복문을 사용하여 저장된 값들을 반복적으로 처리 가능

   #### str : 문자들의 순서가 있는 변경 불가능한 시퀸스 자료형

   - 문자열은 단일 문자나 여러 문자의 조합으로 이루어짐

   ```python
       "Hello" # 작은따옴표(') 혹은 큰따옴표(") 감싸서 표현
       "Hi"
       # 중첩 따옴표
       "문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다."
       '문자열 안에 "큰따옴표"를 사용하려면 작은따옴표로 묶는다.'

       my_str = "Hello"

       # 인덱싱
       print(my_str[1]) # e

       # 슬라이싱
       print(my_str[2:4]) # ll
       print(my_str[3:]) # lo
       print(my_str[0:5:2]) # hlo
       print(my_str[::-1]) #olleH

       # 길이
       print(len(my_str)) # 5

       my_str[1] = "z"
       # TypeError: 'str' object does not support item assignment 문자열은 변경 불가
   ```

   항목 | h | e | l | l | o
  ---------|----------|---------|----------|---------|----------
   index | 0 | 1 | 2 | 3 | 4 
   index | -5 | -4 | -3 | -2 | -1

   #### Escape sequence

   - 역슬래시(backslash)뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합
   - 파이썬의 일반적인 문법 규칙을 잠시 탈출한다는 의미

  이스케이프 문자 | 이름 | 아스키 값(Numeric Value)
  ---------|----------|---------
   \b | 백스페이스(backspace) | 8
   \t | 탭(tab) | 9
   \n | 라인피드(Linefeed) | 10
   \f | 폼피드(Formfeed) | 12
   \r | 캐리지 Carriage Return | 13
   \\ | 역슬래시(Backslash) | 92
   \" | 큰 따옴표(Double Quote) | 39
   \' | 작은 따옴표(Single Quote) | 34

   #### String Interpolation : 문자열 내 변수나 표현식을 삽입하는 방법

   - f-string => 문자열에 f 또는 F 접두어를 붙이고 표현식을 {expression}로 작성하여 문자열에 파이썬 표현식 값을 삽입할 수있음

   ```python
    bugs = 'roaches'
    counts = 13
    area = 'living room'

    print(f"Debugging {bugs} {counts} {area}")
    print("Debugging {} {} {}".format(bugs, counts, area))
    print("Debugging %s %d %s" % (bugs, counts, area))
   ```

   #### list : 여러 개의 값을 순서대로 저장하는 변경 가능한 시퀀스 자료형

   - 0개 이상의 객체를 포함하며 데이터 목록을 저장
   - 대괄호([])로 표기
   - 데이터는 어떤 자료형도 저장할 수 있음

   ```python
       a = [1, 2, 3, 4]
       b = list()
       c = [1, 'a', 3, 'b', 5]
       d = [1, 2, 3, 'python', ['hello', 'world']]
       # a에 1, 2, 3, 4 이 들어있으며 값을 바꿀 수 있다.
       # a[0] = 6 넣으면 1이 6으로 변함

       # 인덱싱
       print(c[1]) # a

       # 슬라이싱
       print(c[2:4]) # [3, 'b']
       print(c[:3]) # [1, 'a', 3]
       print(c[3:]) # ['b', 5]
       print(c[0:5:2]) # [1, 3, 5]
       print(c[::-1]) # [5, 'b', 3, 'a', 1]

       # 길이
       print(len(c)) # 5
   ```

   #### tuple : 여러 개의 값을 순서대로 저장하는 변경 불가능한 시퀀스 자료형

   - 0개 이상의 객체를 포함하며 데이터 목록을 저장
   - 대괄호([])로 표기
   - 데이터는 어떤 자료형도 저장할 수 있음

   ```python
      a = (1, 2, 3)
      b = tuple()
      c = (1,)
      my_tuple = (1, 'a', 3, 'b', 5)
      my_tuple[1] = 'z'
      # TypeError: 'tuple' object does not support item assignment 튜플은 변경 불가

      # 인덱싱
      print(my_tuple[1]) # a

      # 슬라이싱
      print(my_tuple[2:4]) # (3, 'b')
      print(my_tuple[:3]) # (1, 'a', 3)
      print(my_tuple[3:]) # ('b', 5)
      print(my_tuple[0:5:2]) # (1, 3, 5)
      print(my_tuple[::-1]) # (5, 'b', 3, 'a', 1)

      # 길이
      print(len(my_tuple)) # 5
   ```

   #### range : 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형
   
   - range(n)
     - 0 ~ n-1 까지 숫자의 시퀀스
   - range(n, m)
     - n ~ m-1 까지의 숫자 시퀀스
  
   ```python
     range(3)
     # 0, 1, 2
     range(0, 5)
     # 0, 1, 2, 3, 4
     range(10, 5, -1)
     # 10, 9, 8, 7, 6
     range(0, 6, 2)
     # 0, 2, 4
   ```


  - Set Types
    - set

  - Mapping Types
    - dict

  - 기타
    - None
    - Boolean

## 산술 연산자 & 우선 순위




## 변수와 메모리 값이 저장되는 법

  - 변수(Variable) : 값을 참조하는 이름

### 변수명 규칙

  - 영문 알파벳, 언더스코어(_), 숫자로 구성
  - 숫자로 시작할 수 없음
  - 대소문자 구분
  
  