# 제어문

 - 코드의 실행 흐름을 제어하는데 사용되는 구문, 조건에 따라 코드 블록을 실행하거나 반복적 실행

# 조건문 : 

 - 주어진 식을 평가하여 해당 조건이 참인 경우에만 코드 블록을 실행하거나 건너뜀

 ```python
    if 표현식:
        코드 블록
    elif 표현식:
        코드 블록
    else:
        코드 블록
    
    a = 3

    if a > 3:
        print("3 초과")
    else:
        print("3 이하")
    # 3 이하

    if a >= 3:
        print("3 이상")
    else:
        print("3 이하")
    
    dust = 35
    if dust > 150:
        print("매우 나쁨")
    elif dust > 80:
        print("나쁨")
    elif dust > 30:
        print("보통")
    else:
        print("좋음")
    # 보통

    # 중첩 조건문
    dust = 480
    if dust > 150:
        print("매우 나쁨")
        if dust > 300:
            print("위험해요! 나가지 마세요!")
    elif dust > 80:
        print("나쁨")
    elif dust > 30:
        print("보통")
    else:
        print("좋음")
 ```

# 반복문

 - 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
 - for / while 존재

## for

 - 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복

 ```python
    # 기본 구조
    for 변수 in 반복 가능한 객체:
        코드 블록
 ```
 
 - 리스트 내 첫 항목이 반복 변수에 할당되고 코드블록이 실행
 - 다음으로 반복 변수에 리스트의 2번째 항목이 할당되고 코드블록이 다시 실행
 - 마지막으로 반복 변수에 리스트의 마지막 요소가 할당되고 코드블록이 실행

 ```python
    # 리스트 순회
    items = ["apple", "banana", "coconut"]

    for item in items:
        print(item)
    
    # apple
    # banana
    # coconut

    # 문자열 순회
    country = "Korea"

    for char in country:
        print(char)
    
    # K
    # o
    # r
    # e
    # a

    # range 순회
    for i in range(5):
        print(i)
    
    # 0
    # 1
    # 2
    # 3
    # 4

    # 인덱스 요소로 순회
    numbers = [4, 6, 10, -8, 5]

    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2
    print(numbers)

    # [8, 12, 20, -16, 10]

    # 중첩 반복문
    outers = ['A', 'B']
    inners = ['c', 'd']

    for outer in outers:
        for inner in inners:
            print(outer, inner)
    
    # A c
    # A d
    # B c
    # B d
 ```

## while

 - 주어진 조건식이 참인 동안 코드를 반복해서 실행 => 조건이 거짓이 될 때 까지 반복

 ```python
    # 기본 구조
    while 조건식:
        코드 블록

    a = 0

    while a < 3:
        print(a)
        a += 1
    
    print("끝")
    # 0
    # 1
    # 2
    # 끝
 ```

 - while문을 사용한 특정 입력 값에 대한 종료 조건 활용하기

 ```python
    number = int(input("양의 정수를 입력해주세요.: "))

    while number <= 0:
        if number < 0:
            print("음수를 입력했습니다.")
        else:
            print("0은 양의 정수가 아닙니다.")

        number = int(input("양의 정수를 입력해주세요.: "))
    
    print("잘했습니다!")
 ```

 
차이점 | for | while
---------|----------|---------
 -- | 반복 횟수가 명확할때 유용 | 반복 횟수가 불명확 하거나 조건에 따라 종료해야 할 때 유용
 -- | 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때 | 사용자 입력을 받아 특정 조건이 충족될 때까지 반복

# 반복 제어

 - for문과 while은 매 반복마다 본문 내 코드를 실행하지만 일부만 실행하는 것이 필요할 때가 있음
 - break : 반복을 즉시 중지
 - continue : 다음 반복으로 건너뜀

## Break

 ```python
    number = int(input("양의 정수를 입력해주세요.: "))

    while number <= 0:
        if number == -9999:
            break

        if number < 0:
            print("음수를 입력했습니다.")
        else:
            print("0은 양의 정수가 아닙니다.")

        number = int(input("양의 정수를 입력해주세요.: "))
    
    print("잘했습니다!")

    # 리스트에서 홀수만 출력하기
    numbers = [1, 3, 5, 6, 7, 9, 10, 11]
    found_even = False

    for num in numbers:
        if num % 2 == 0:
            print("첫 번째 짝수를 찾았습니다:", num)
            found_even = True
            break
    
    if not found_even:
        print("짝수를 찾지 못했습니다.")
 ```

## Continue

 ```python
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for num in numbers:
        if num % 2 == 0:
            continue
        print(num)
    
    # 1
    # 3
    # 5
    # 7
    # 9
 ```

## break와 continue 주의사항

 - break와 continue를 남용하는 것은 코드의 가독성을 저하시킬 수있음
 - 특정한 종료 조건을 만들어 break을 대신하거나, if 문을 사용해 continue 처럼 코드를 건너 뛸 수도 있음
 - 약간의 시간이 들더라도 가능한 코드의 가독성을 유지하고 코드의 의도를 명확하게 작성하도록 노력하는 것이 중요


# List Comprehension

 - 간결하고 효율적인 리스트 생성

 ```python
    [ expression for 변수 in iterable ]

    list(expression for 변수 in iterable)

    # 1. 일반적인 방법
    new_list = []
    for i in range(10):
        if i % 2 == 1:
            new_list.append(i)
    print(new_list)

    # 2. list comprehension
    new_list_2 = [ i for i in range(10) if i % 2 == 1]
    print(new_list_2)
 ```

# 기타

 - 리스트 구현 방법

 ```python
    # 1. for loop
    new_numbers = []
    for number in numbers:
        new_numbers.append(int(number))
    print(new_numbers)

    # 2. map
    new_numbers_2 = list(map(int,numbers))
    print(new_numbers_2)

    # 3. list comprehension
    new_numbers_3 = [ int(number) for number in numbers ]
    print(new_numbers_3)
 ```

 - enumerate 예시 ( index 와 list 내용을 반환 )

 ```python
    fruits = ['apple', 'banana', 'cherry']

    for index, fruit in enumerate(fruits):
        print(f'인덱스 {index}: {fruit}')
    
    # 인덱스 0: apple
    # 인덱스 1: banana
    # 인덱스 2: cherry
 ```