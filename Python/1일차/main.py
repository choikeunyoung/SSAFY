# # 시작
# print("Hello World")

# # 데이터 타입

# a1 = 1
# a2 = 2.3
# a3 = 2 + 3j
# a4 = "Hello World"
# a5 = list() # [[1, 2, 3], [4, 5, 6]]
# a6 = tuple() # (1, 2, 3, 4)
# a7 = range(3) 
# a8 = lambda x, y : y + x
# a9 = set() # {1, 2, 3, 4}
# a10 = dict() # {"apple" : 2, "banana" : 3}
# a11 = None
# a12 = True

# for i in range(1,13):
#     var = f"a{i}"
#     var = eval(var)
#     print(type(var))

# # 산술 연산자

#     print("7/3 :", 7/3, "\n7//4 :", 7//4, "\n7%4 :",7%4)
    
# # 연산자 우선 순위

#     print(-2 ** 4) # -16
#     print(-(2 ** 4)) # -16
#     print((-2) ** 4) # 16

# # 변수와 메모리

#     degree = 36.5
#     print(id(degree))

#     degree = 37.5
#     print(id(degree))

# # 변수의 재할당

#     degrees = 10
#     number = 2 * degrees
#     print(number)

#     degrees = 5
#     print(number)

# # 변수명

#     name = "min"
#     age = 33
#     height = 111
#     weight = 76.6
#     # 참 거짓은 앞에 is
#     is_student = True
#     # 상수명은 대문자
#     SECOND = 10
#     MAX_VALUE = 100
#     PI = 3.14159

#     person_name = "Alice"

#     def calculate_sum(x, y):
#         return x + y
    

#     def calculate_sub(x, y):
#         return x - y
    
# num_list = list(map(int, input().split()))
# print(num_list)


# name = input()
# age = int(input())
# height = float(input())

# # 1. 포맷 코드
# print("저의 이름은 %s, 나이는 %d, 키는 %f" %(name, age, height))

# # 2. f-string
# print(f"저의 이름은 {name}, 나이는 {age}, 키는 {height}")

# # 3. .format
# print("저의 이름은 {}, 나이는 {}, 키는 {}".format(name, age, height))


# array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# #1. 인덱싱 하여 3을 출력해 보세요.
# print(array[0][2])
# #2. 인덱싱 하여 7을 출력해 보세요.
# print(array[2][0])

# #2차원 리스트를 입력 받는 방법

# rows = int(input())

# matrix = [ list(map(int,input().split())) for _ in range(N) ]

# for row in matrix:
#     print(row)


# my_dict = {
#     "a1" : {"b1" : 1, "b2" : 2, "b3" : 3},
#     "a2" : {"b1" : 4, "b2" : 5, "b3" : 6},
#     "a3" : {"b1" : 7, "b2" : 8, "b3" : 9}
# }

# print(my_dict['a2']['b2'])

# set_1 = {1, 2, 3, 4, 5, 6}
# set_2 = {4, 5, 6, 7, 8, 9}

# print(set_1 | set_2)
# print(set_1 - set_2)
# print(set_1 & set_2)

# 로또 번호 추첨

# import random

# num_list = set()

# while len(num_list) < 6:
#     number = random.randint(1, 45)
#     num_list.add(number)
# print(num_list)


# print(int(float("3.5")))

# numbers = [1, 2, 3, 4, 5]

# total = 0

# for number in numbers:
#     total += number

# print(total)

# vowels = 'aeiou'

# print(('a' and 'b') in vowels)
# print(('b' and 'a') in vowels)

# print( 3 and 5 and 6 )
# print( 3 and 0 )
# print( 0 and 3 )
# print( 0 and 0 )

# print( 3 or 5 or 6 )
# print( 3 or 0 )
# print( 0 or 3 )
# print( 0 or 0 )

# print('다음은 이형기 시인의 "낙화"의 한 구절이다.\n- 1연\n\t가야할 때 언제인가를\n\t분명히 알고 가는 이의\n\t뒷모습은 얼마나 아름다운가.\n\n나는 이 시를 보며 \'나는 내가 가야할 때가 언제일까?\' 를 생각해 보았다.')

# author_1 = '권필'
# author_2 = '허균'
# book_1 = '주생전'
# book_2 = '홍길동전'

# print(f"{book_1}의 작가는 {author_1}이고,\n{author_2}은 {book_2}를 집필하였다.")

# books = ['광문자전', '유연전', '심청전', '홍길동전', '수성지']
# authors = ['작자 미상', '허균', '박지원', '이항복', '임제']

# print(f"{authors[1]} : {books[3]}")
# print(f"{authors[3]} : {books[1]}")
# print(f"{authors[0]} : {books[2]}")
# print(f"{authors[2]} : {books[0]}")
# print(f"{authors[4]} : {books[4]}")


# information = dict()
# authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
# books = [
#     ['장화홍련전', '가락국 신화', '온달 설화'],
#     ['금오신화', '이생규장전', '만복자서포기'],
#     ['수성지', '백호집', '원생몽유록'],
#     ['홍길동전', '장생전', '도문대작'],
#     ['옥루몽', '옥련몽'],
# ]

# '''
# - 작가와 작품 목록 참고
# - 허균 : 홍길동전, 장생전, 도문대작
# - 임제 : 수성지, 백호집, 원생몽유록
# - 작자 미상 : 장화홍련전, 가락국 신화, 온달 설화
# '''

# information[authors[0]] = books[1]
# information[authors[1]] = books[3]
# information[authors[2]] = books[4]
# information[authors[3]] = books[0]
# information[authors[4]] = books[2]
# for k,v in information.items():
#     print(f"{k} : {v}")


# catalog = [
#     ['시간의 틈', '반짝임의 어둠', '망각의 경계'], 
#     ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'], 
#     ['황금의 칼날', '비열한 간신', '무명의 영웅'], 
#     ['성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀']
# ]

# backup_catalog = [
#     ['시간의 틈', '반짝임의 어둠', '망각의 경계'], 
#     ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'], 
#     ['황금의 칼날', '비열한 간신', '무명의 영웅'], 
#     ['성공의 열쇠', '내면의 변화', '목표의 달성']
# ]

# ''' 
# 도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
# '성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
# '''

# print('catalog와 backup_catalog를 비교한 결과')
# # 식별 연산자로 catalog와 backup_catalog를 비교한 결과를 출력하시오. 
# print(catalog == backup_catalog)

# print('backup_catalog : ')
# print(backup_catalog)
# print()

# print('catalog : ')
# print(catalog)


number_of_book = 100

def decrease_book(count_book):
    print(f"남은 책의 수 : {number_of_book - count_book}")
    return number_of_book - count_book

# ws_3_3.py

def rental_book(name, count):
    decrease_book(count)
    print(f"{name}님이 {count}권의 책을 대여하였습니다.")

rental_book("홍길동", 3)
