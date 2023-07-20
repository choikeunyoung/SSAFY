# import requests
# from pprint import pprint as print

# url = "https://random-data-api.com/api/v2/users"

# response = requests.get(url).json()

# print(response["address"]["country"])

# dust = int(input())

# if dust > 150:
#     print("매우 나쁨")
# elif dust > 80:
#     print("나쁨")
# elif dust > 30:
#     print("보통")
# else:
#     print("좋음")

# 2번째 elif 범위는?  80 < dust <= 150
# 3번째 elif 범위는? 30 < dust <= 80

# 실습1. 정수를 입력받아 짝수면 "EVEN" 출력, 홀수면 "ODD" 출력
# N = int(input())

# if N % 2 == 0:
#     print("EVEN")
# else:
#     print("ODD")

# # 실습2. 윤년 판별하기, 윤년이면 "leap year". 그렇지 않으면 "common year"출력
# # 윤년의 조건 1. 연도가 4로 나누어 떨어지지만 100으로는 나누어 떨어지면 안된다.
# # 윤년의 조건 2. 연도가 400으로 나누어 떨어진다.

# year = int(input())

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("leap year")
# else:
#     print("common year")


# 반복문 실습

# 실습 1. 구구단 출력
# for i in range(2,10):
#     print(f"<{i}단>")
#     for j in range(1,10):
#         print(f"{i} * {j} = {i*j}")
#     print()

# # 실습 2. N을 입력받아 N단의 왼쪽 직각 이등변 삼각형을 그리는 프로그램
# for k in range(1,6):
#     print("*"*k)


# 실습1. continue를 이용하여 1부터 10까지 정수중 홀수만 출력하기
# for i in range(1,11):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)

# # 실습2. break를 이용하여 "Shall we close? (y/n)" 문구에 y를 입력해야 반복문을 탈출하고 'The end'를 출력하는 프로그램 작성
# while True:
#     ans = input("Shall we close? (y/n) ")
#     if ans == 'y':
#         print('The end')
#         break

# 실습3. 정수를 입력받아 그 정수가 몇 자리수 숫자읹 알아내는 프로그램 작성.
# num = int(input())
# cnt = 0
# while num > 0:
#     num //= 10
#     print(num)
#     cnt += 1
# print(cnt)

# import math

# numbers = [1, 4, 9, 16, 25]

# sqrt_numbers = []

# for number in numbers:
#     sqrt_numbers.append(math.sqrt(number))

# print(sqrt_numbers)

# sqrt_number = [ math.sqrt(number) for number in numbers if number % 2 == 0]
# print(sqrt_number)

number_of_people = 0
number_of_book = 100

def decrease_book(num):
    num -= num
    return num

def increase_user(user_cnt):
    user_cnt += 1
    return user_cnt

def create_user(name,age,address):
    print(f"{name}님 환영합니다!")
    people_dict = {}
    people_dict["name"] = name
    people_dict["age"] = age
    people_dict["address"] = address
    return people_dict

def rental_book(info):
    pass

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

many_user = list(map(create_user,name,age,address,number_of_people))
number_of_people = increase_user(many_user)

