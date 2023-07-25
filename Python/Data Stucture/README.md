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

### Set

 - 고유한 항목들의 정렬되지 않은 컬렉션

 메서드 | 설명
 ---------|----------
 s.add(x) | 세트 s에 항목 x를 추가. 이미 x가 있다면 변화 없음
 s.clear() | 세트 s의 모든 항목을 제거
 s.remove(x) | 세트 s에서 항목 x를 제거. 항목 x가 없을 경우 Key error
 s.pop() | 세트 s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거
 s.discard(x) | 세트 s에서 항목 x를 제거
 s.update(iterable) | 세트 s에 다른 iterable 요소를추가

 ```python
   # .add(x) 세트에 x를 추가
   my_set = {1, 2, 3}
   my_set.add(4)
   print(my_set) # {1, 2, 3, 4}

   my_set.add(4)
   print(my_set) # {1, 2, 3, 4}

   # .clear(x) 세트의 모든 항목을 제거
   my_set = {1, 2, 3}
   my_set.clear()
   print(my_set) # set()

   # .remove(x) 세트에서 항목 x를 제거
   my_set = {1, 2, 3}
   my_set.remove(2)
   print(my_set) # {1, 3}

   my_set.remove(10)
   print(my_set) # KeyError

   # .discard() 세트 s에서 항목 x를 제거. remove와 달리 에러 없음
   my_set = {1, 2, 3}
   my_set.discard(2)
   print(my_set) # {1, 3}
   
   my_set.discard(10)

   # .pop() 세트에서 임의의 요소를 제거하고 반환
   my_set = {1, 2, 3}
   element = my_set.pop()

   print(element) # 1
   print(my_set) # {2, 3}

   # .update(iterable) 세트에 다른 iterable 요소를 추가
   my_set = {1, 2, 3}
   my_set.update([4, 5, 1])
   print(my_set) # {1, 2, 3, 4, 5}
 ```

  메서드 | 설명 | 연산자
 ---------|----------|----------
 set1.difference(set2) | set1에는 있지만 set2에는없는 항목으로 세트를 생성 후 반환 | set1 - set2
 set1.intersection(set2) | set1과 set2 모두 들어있는 항목으로 세트를 생성 후 반환 | set1 & set2
 set1.issubset(set2) | set1의 항목이 모두 set2에 들어있으면 True를 반환 | set1 <= set2
 set1.issuperset(set2) | set1가 set2의 항목을 모두 포함하면 True를 반환 | set1 >= set2
 set1.union(set2) | set1 or set2에 들어있는 항목으로 세트를 생성 후 반환 | set1 \| set2

 ```python
   set1 = {0, 1, 2, 3, 4}
   set2 = {1, 3, 5, 7, 9}

   print(set1.difference(set2)) # {0, 2, 4}
   print(set1.intersection(set2)) # {1, 3}
   print(set1.issubset(set2)) # False
   print(set1.issuperset(set2)) # False
   print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9}
 ```

### 딕셔너리

 - 고유한 항목들의 정렬되지 않은 컬렉션

 메서드 | 설명
 ---------|----------
 D.clear() | 딕셔너리 D의 모든 키/값 쌍을 제거
 D.get(k) | 키 k에 연결된 값을 반환 (키가 없으면 None을 반환)
 D.get(k, v) | 키 k에 연결된 값을 반환하거나 키가 없으면 기본 값으로 v를 반환
 D.keys() | 딕셔너리 D의 키를 모은 객체를 반환
 D.values(x) | 딕셔너리 D의 값을 모은 객체를 반환
 D.items() | 딕셔너리 D의 키/값 쌍을 모은 객체를 반환
 D.pop(k) | 딕셔너리 D에서 k를 제거하고 연결됐던 값을 반환 (없으면 오류)
 D.pop(k, v) | 딕셔너리 D의 K를 제거하고 연결됐던 값을 반환 (없으면 v를 반환)
 D.setdefault(k) | 딕셔너리 D에서 키 k와 연결된 값을 반환
 D.setdefault(k, v) | 딕셔너리 D에서 키 k와 연결된 값을 반환 k가 D의 키가 아니면 값 v와 연결한 키 k를 D에 추가하고 v를 반환
 D.update(other) | other 내 각 키에 대해 D에 있는 키면 D에 있는 그 키의 값을 other에 있는 값으로 대체. other에 있는 각 키에 대해 D에 없는 키면 키/값 쌍을 D에 추가

```python
   # .get(key[, default]) 키 연결된 값을 반환하거나 없으면 None 혹은 기본값
   person = {"name" : "Alice", "age" : 25}

   print(person.get("name")) # Alice
   print(person.get("country")) # KeyError
   print(person.get("country")) # None
   print(person.get("country", "Unknow")) # Unknow

   # .clear() 딕셔너리 D의 모든 키/값 쌍을 제거
   person = {"name" : "Alice", "age" : 25}
   person.clear()
   print(person) # {}

   # .keys() 딕셔너리 키를 모은 객체를 반환
   person = {"name" : "Alice", "age" : 25}
   print(person.keys()) # dict_keys(["name", "age"])

   for k in person.keys():
      print(k) # name / age

   # .values() 딕셔너리 값을 모은 객체를 반환
   person = {"name" : "Alice", "age" : 25}
   print(person.values()) # dict_values(["Alice", 25])

   for v in person.values():
      print(v) # Alice / 25
   
   # .items() 딕셔너리 키/값 쌍을 모은 객체를 반환
   person = {"name" : "Alice", "age" : 25}

   print(person.items()) # dict_items([("name", "Alice"), ("age", 25)])

   for k, v in person.items():
      print(k, v) # name Alice / age 25
   
   # .pop(key[, default]) 키를 제거하고 연결됐던 값을 반환 (없으면 에러나 default를 반환)
   person = {"name" : "Alice", "age" : 25}

   print(person.pop("age")) # 25
   print(person) # { "name" : "Alice" }
   print(person.pop("country", None)) # None
   print(person.pop("country")) # KeyError

   # .setdefault(key[, default]) 키와 연결된 값을 반환 없다면 default와 연결한 키를 딕셔너리에 추가 후 default를 반환
   person = {"name" : "Alice", "age" : 25}

   print(person.setdefault("country", "KOREA")) # KOREA
   print(person.setdefault("age", 50)) # age : 25
   print(person) # {"name" : "Alice", "age" : 25, "country" : "KOREA"}

   # .update([other]) other가 제공하는 키/값 쌍으로 딕셔너리를 갱신 기존 키는 덮어씀 (여러개도 가능)
   person = {"name" : "Alice", "age" : 25}
   other_person = {"name" : "Jane", "gender" : "Female"}

   person.update(other_person)
   print(person) # {"name" : "Jane", "age" : 25, "gender" : "Female" }
   
   person.updage(age=50)
   print(person) # {"name" : "Jane", "age" : 50, "gender" : "Female" }
   
   person.update(country="KOREA")
   print(person) # {"name" : "Jane", "age" : 50, "gender" : "KOREA" }
```

# 복사

 - 데이터에 분류에 따라 복사가 달라짐
 - 변경 가능한 데이터 타입과 변경 불가능한 데이터 타입을 다르게 다룸

 ```python
   # 가변 데이터 타입
   a = [1, 2, 3, 4]
   b = a
   b[0] = 100

   print(a) # [100, 2, 3, 4]
   print(b) # [100, 2, 3, 4]

   # 불변 데이터 타입
   a = 20
   b = a
   b = 10

   print(a) # 20
   print(b) # 10
 ```

## 복사 유형

 1. 할당 (Assignment)
 
 2. 얕은 복사(Shallow copy)

 3. 깊은 복사(Deep copy)

### 할당

 ```python
   #복사 예시
   original_list = [1, 2, 3]
   copy_list = original_list
   print(original_list, copy_list) # [1, 2, 3] [1, 2, 3]

   copy_list[0] = "hi"
   print(original_list, copy_list) # ["hi", 2, 3] ["hi", 2, 3]
 ```

 - 할당 연산자(=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사

### 얕은 복사

 - 슬라이싱을 통해 생성된 객체는 원본 객체와 독립적으로 존재

 ```python
   a = [1, 2, 3]
   b = a[:]
   print(a,b) # [1, 2, 3] [1, 2, 3]

   b[0] = 100
   print(a,b) # [1, 2, 3] [100, 2, 3]
 ```

 - 2차원 리스트와 같이 변경가능한 객체 안에 변경 가능한 객체가 있는 경우

 ```python
   a = [1, 2, [1, 2]]
   b = a[:]
   print(a, b) # [1, 2, [1, 2]] [1, 2, [1, 2]]

   b[2][0] = 100
   print(a, b) # [1, 2, [100, 2]] [1, 2, [100, 2]]
 ```

 - a와 b의 주소는 다르지만 내부 객체의 주소는 같기 때문에 함께 변경된다.

### 깊은 복사

 ```python
   import copy

   original_list = [1, 2, [1, 2]]
   deep_copied_list = copy.deepcopy(original_list)

   deep_copied_list[2][0] = 100

   print(original_list) # [1, 2, [1, 2]]
   print(deep_copied_list) # [1, 2, [100, 2]]
 ```

 - 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참조하도록 함