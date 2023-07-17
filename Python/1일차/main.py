# 시작
print("Hello World")

# 데이터 타입

a1 = 1
a2 = 2.3
a3 = 2 + 3j
a4 = "Hello World"
a5 = list() # [[1, 2, 3], [4, 5, 6]]
a6 = tuple() # (1, 2, 3, 4)
a7 = range(3) 
a8 = lambda x, y : y + x
a9 = set() # {1, 2, 3, 4}
a10 = dict() # {"apple" : 2, "banana" : 3}
a11 = None
a12 = True

for i in range(1,13):
    var = f"a{i}"
    var = eval(var)
    print(type(var))

# 산술 연산자

    print("7/3 :", 7/3, "\n7//4 :", 7//4, "\n7%4 :",7%4)
    
# 연산자 우선 순위

    print(-2 ** 4) # -16
    print(-(2 ** 4)) # -16
    print((-2) ** 4) # 16

# 변수와 메모리

    degree = 36.5
    print(id(degree))

    degree = 37.5
    print(id(degree))

# 변수의 재할당

    degrees = 10
    number = 2 * degrees
    print(number)

    degrees = 5
    print(number)

# 변수명

    name = "min"
    age = 33
    height = 111
    weight = 76.6
    # 참 거짓은 앞에 is
    is_student = True
    # 상수명은 대문자
    SECOND = 10
    MAX_VALUE = 100
    PI = 3.14159

    person_name = "Alice"

    def calculate_sum(x, y):
        return x + y
    

    def calculate_sub(x, y):
        return x - y
    
num_list = list(map(int, input().split()))
print(num_list)


name = input()
age = int(input())
height = float(input())

# 1. 포맷 코드
print("저의 이름은 %s, 나이는 %d, 키는 %f" %(name, age, height))

# 2. f-string
print(f"저의 이름은 {name}, 나이는 {age}, 키는 {height}")

# 3. .format
print("저의 이름은 {}, 나이는 {}, 키는 {}".format(name, age, height))
