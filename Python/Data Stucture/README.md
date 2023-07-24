# Data Structure

 - 여러 데이터를 효과적으로 사용, 관리하기 위한 구조 (str, list, dict 등)

## 메서드

 - 객체에 속한 함수 => 객체의 상태를 조작하거나 동작을 수행
 - 클래스(class) 내부에 정의되는 함수
 - 파이썬에서 "타입을 표현하는 방법"
 - 어딘가에 속해있는 함수, 각 데이터 타입별 다양한 기능을 가진 메서드 존재

 ```python
    # 문자열 메서드 예시
    pirnt("Hello".capitalize()) # Hello 첫 글자를 대문자로
 ```

## Sequence Types

 - 여러 값들을 순서대로 나열하여 저장
 - String, List, Tuple ... 등

### String

 #### 문자열 조회 / 탐색 및 검증 메서드

 메서드 | 설명
 ---------|----------
 s.find(x) | x의 첫 번째 위치를 반환. 없으면 -1을 반환
 s.index(x) | x의 첫 번째 위치를 반환. 없으면 오류 발생
 s.isalpha() | 알파벳 문자 여부 ( 유니코드 상 Letter )
 s.isupper() | 대문자 여부
 s.islower() | 소문자 여부
 s.istitle() | 타이틀 형식 여부

 ```python
    # find
    print("banana".find("a")) # 1
    print("banana".find("z")) # -1
    
    # index
    print("banana".index("a")) # 1
    print("banana".index("z")) # ValueError : substring not found

    # isupper / islower
    string1 = "HELLO"
    string2 = "Hello"
    print(string1.isupper()) # True
    print(string2.isupper()) # False
    print(string1.islower()) # False
    print(string2.islower()) # False

    # isalpha(x)
    string1 = "Hello"
    string2 = "123"
    print(string1.isalpha()) # True
    print(string2.isalpha()) # False
 ```

 #### 문자열 조작 메서드
 
 메서드 | 설명
 ---------|----------
 s.replace(old, new[, count]) | 바꿀 대상 글자를 새로운 글자로 바꿔서 변환
 s.strip(x) | 공백이나 특정 문자를 제거
 s.split(sep=None, maxsplit=-1) | 공백이나 특정 문자를 기준으로 분리
 "separator".join([iterable]) | 구분자로 iterable을 합침
 s.capitalize() | 가장 첫 번쨰 글자를 대문자로 변경
 s.title() | 문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자, 나머지는 소문자
 s.upper() | 모두 대문자 변경
 s.lower() | 모두 소문자 변경
 s.swapcase() | 대 <-> 소 서로 변경
  

 ```python
    # .replace(old, new[, count]) 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
    text = "Hello, world!"
    new_text = text.replace("word", "Python")
    print(new_text) # Hello, Python!

    # .strip([chars]) 문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거
    text = '     Hello, world!     '
    new_text = text.strip()
    print(new_text) # "Hello, world!"

    # .split(sep=None, maxsplit=-1) 지정한 문자를 구분자로 문자열을 분리하여 문자열 리스트 반환
    text = "Hello, world!"
    words = text.split(',')
    print(words) # ['Hello', ' world!']

    # "separator".join([iterable]) iterable 요소들을 원래 문자열을 구분자로 이용하여 하나의 문자열로 연결
    words = ['Hello', 'world!']
    text = '-'.join(words)
    print(text) # 'Hello-world!'

    # 그 외
    text = "heLLo, woRld!"
    new_text1 = text.capitalize()
    new_text2 = text.title()
    new_text3 = text.upper()
    new_text4 = text.swapcase()
    
    print(new_text1) # Hello, world!
    print(new_text2) # Hello, World!
    print(new_text3) # HELLO, WORLD!
    print(new_text4) # HEllO, WOrLD!
 ```

### List

 #### 리스트 값 추가 및 삭제 메서드

 메서드 | 설명
 ---------|----------
 L.append(x) | 리스트 마지막에 항목 x를 추가
 L.extend(x) | Iterable m의 모든 항목들을 리스트 끝에 추가 ( += 과 같은 기능 )
 L.insert(i, x) | 리스트 인덱스 i에 항목 x를 삽입
 L.remove(x) | 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거 (항목이 존재하지 않을 경우, ValueError)
 L.pop() | 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거
 L.pop(i) | 리스트의 인덱스 i에 있는 항목을 반환 후 제거
 L.clear() | 리스트의 모든 항목 삭제

 ```python
    # .append(x) 리스트 마지막에 항목 x를 추가
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list) # [1, 2, 3, 4]

    # .extend(iterable) 리스트에 다른 반복 가능한 객체의 모든 항목을 추가
    my_list = [1, 2, 3]
    my_list.extend([4, 5, 6])
    print(my_list) # [1, 2, 3, 4, 5, 6]

    # .insert(i, x) 리스트의 지정한 인덱스 I 위치에 항목 x를 삽입
    my_list = [1, 2, 3]
    my_list.insert(1, 5)
    print(my_list) # [1, 5, 2, 3]

    # .remove(x) 리스트에서 첫 번째로 일치하는 항목을 삭제
    my_list = [1, 2, 3]
    my_list.remove(2)
    print(my_list) # [1, 3]

    # .pop(i) 리스트에서 지정한 인덱스의 항목을 제거하고 반환 작성하지 않을 경우 마지막 항목 제거
    my_list = [1, 2, 3, 4, 5]

    item1 = my_list.pop()
    item2 = my_list.pop(0)

    print(item1) # 5
    print(item2) # 1
    print(my_list) # [2, 3, 4]

    # .clear() 리스트의 모든 항목을 삭제
    my_list = [1, 2, 3]
    my_list.clear()
    print(my_list) # []
 ```

 #### 리스트 탐색 및 정렬 메서드

 메서드 | 설명
 ---------|----------
 L.index(x, start, end) | 리스트에 있는 항목 중 가장 왼쪽에 있는 항목x의 인덱스를 반환
 L.reverse() | 리스트를 거꾸로 출력
 L.sort() | 리스트를 정렬 (매개변수 이용가능)
 L.count() | 리스트에서 항목 x의 개수를 반환

 ```python
    # .index(x) 리스트에서 첫 번째로 일치하는 항목의 인덱스를 반환
    my_list = [1, 2, 3]
    index = my_list.index(2)
    print(index) # 1

    # .count(x) 리스트에서 항 목 x가 등장하는 횟수를 반환
    my_list = [1, 2, 2, 3, 3, 3]
    count = my_list.count(3)
    print(count) # 3

    # .sort() 원본 리스트를 오름차순으로 정렬
    my_list = [3, 2, 1]
    my_list.sort()
    print(my_list) # [1, 2, 3]
    # 내림차순
    my_list.sort(reverse=True)
    print(my_list) # [3, 2, 1]

    # .reverse() 리스트의 순서를 역으로 변경
    my_list = [1, 3, 2, 8, 1, 9]
    my_list.reverse()
    print(my_list) # [9, 1, 8, 2, 3, 1]
 ```