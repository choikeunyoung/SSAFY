# # # 2023 - 7 - 24

# # # Sting

# # a = " Practice makes perfect "

# # #1. 문자열 a에서 'e'의 개수 세기
# # print(a.count('e'))
# # #2. 문자열 a에서 'i'의 위치 찾기(2가지 방법)
# # print(a.find('i'))
# # print(a.index('i'))
# # #3. 문자열 a의 문자 사이에 .(점) 삽입
# # print(".".join(a))
# # #4. 문자열 a를 공백 기준으로 분리하여 출력
# # print(a.split())
# # #5. 문자열 a에서 'makes'를 'made'로 바꿔서 출력
# # print(a.replace("makes","made"))
# # #6. 문자열 a를 대문자와 소문자로 변환하여 출력
# # print(a.upper())
# # print(a.lower())
# # #7. 문자열 a에서 양쪽 공백 삭제하기
# # print(a.strip())

# # # List

# # a = ["b", "a", "n", "a", "n"]

# # #1. 리스트 a의 마지막에 'a' 추가하기
# # a.append("a")
# # print(a)
# # #2. 리스트 a를 오름차순으로 정렬
# # a.sort()
# # print(a)
# # #3. 리스트 a를 내림차순으로 정렬
# # a.sort(reverse=True)
# # print(a)
# # #4. 리스트 a를 역순으로 뒤집기
# # a.reverse()
# # print(a)
# # #5. 리스트 a에서 문자 'a' 삭제하기
# # a.remove("a")
# # print(a)
# # #6. 리스트 a의 마지막 요소를 꺼내서 삭제하고 삭제한 요소 출력
# # print(a.pop())
# # #7. 리스트 a에서 문자 'n'의 개수를 출력
# # print(a.count("n"))

# # 2023 - 7 - 25

# # 세트 가변형 비시퀀스 -> 중복을 허용하지 않는다 -> 집합과 같은 특징

# list1 = [1, 2, 3]
# list2 = [4, 5, 6, 7, 8, 9]
# set1 = set(list1)
# set2 = set(list2)

# #1. set1에 4추가
# set1.add(4)
# print(set1)
# #2. set1에 [5, 6, 7] 추가
# set1.update([5, 6, 7])
# print(set1)
# #3. set1에서 7제거(2가지 방법)
# set1.remove(7)
# print(set1)
# set1.discard(7)
# print(set1)
# #4. set1 차집합 set2 출력
# print(set1.difference(set2))
# #5. set1 교집합 set2 출력
# print(set1.intersection(set2))
# #6. set1 합집합 set2 출력
# print(set1.union(set2))

# d = {
#     "plus" : ["더하기", "장점"],
#     "minus" : ["빼기", "적자"],
#     "multiply" : ["곱하기", "다양하게"],
#     "division" : ["나누기", "분열"]
# }

# # 1.
# word = input()
# print(d[word])
# print(d.get(word))
# print(d.setdefault(word))

# # 2.
# print(d.keys())

# # 3.
# d['square'] = ["제곱", "사각형"]
# d.setdefault('square', ["제곱", "사각형"])
# new_d = {'square' : ["제곱", "사각형"]}
# d.update(new_d)
# print(d.items())

# # 4. key와 value를 삭제하는 프로그램

# word = input()
# d.pop(word)
# # del d[word]
# print(d)

# from collections import Counter

# blood_types = ['A', 'B', 'C', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
# print(Counter(blood_types))

# 1. 할당 : 원본 데이터 변경 O

list1 = [1, 2, 3, 4]
list2 = list1
list2[0] = 5

print(id(list1), id(list2))
print(list1, list2)

# 2. 얕은 복사(슬랑싱, copy()) : 객체안에 객체가 있는 경우 원본 데이터가 변경 O

list1 = [1, 2, [3, 4]]
list2 = list1.copy()

list2[0] = 5
list2[2][0] = 5

print(id(list1), id(list2))
print(id(list1[2]), id(list2[2]))
print(list1, list2)

# 3. 깊은 복사 : 원본 데이터 변경 X

import copy

list1 = [1, 2, [3, 4]]
list2 = copy.deepcopy(list1)

list2[2][0] = 5

print(id(list1), id(list2))
print(id(list1[2]), id(list2[2]))
print(list1, list2)