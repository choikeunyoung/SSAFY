# 객체.메서드()
# "abc".upper()
# 인스턴스? 인스턴스는 객체과 같은말
# 객체만 지칭할 때는 객체, 클래스와 연관지어 부를때는 인스턴스
# 인스턴스.메서드()

class Person:
    name = "kai"

# 실습1. 클래스 변수에 접근하여 kai를 출력해 보세요.
# 1. 인스턴스 생성(인스턴스 = 클래스명())
kai = Person()
# 2. 클래스 변수 호출(인스턴스.클래스변수)
print(kai.name)

# 실습2. say()메서드를 호출해 보세요

class Person:
    def say(self):
        print("Welcome.")

kai = Person()
kai.say()

# 실습3. say() 메서드를 호출해 보세요.

class Person:
    def __init__(self, name): # 생성자 함수
        self.name = name

    def say(self): # 인스턴스 메서드
        print(f"Welcome. {self.name}")
    
kai = Person("kai")
kai.say()


# 2023 - 07 - 26 실습

class Car:
    model = "Sonata" # 클래스 변수 = 맴버 변수
    color = "White"

    def speedchange(self, v):
        print(f"speed : {v}")
        self.speed = v

# Sonata 출력, white 출력, speed : 80 출력
car_info = Car()
print(car_info.model)
print(car_info.color)
car_info.speedchange(80)

# ---> 생성자 메서드 구조로 바꾸기
# model : Sonata, color : white, speed : 80

class Car:
    def __init__(self, model, color, speed): # 생성자 함수
        self.model = model # 인스턴스 변수
        self.color = color
        self.speed = speed
    
    def info(self): # 인스턴스 메서드
        print(f"model : {self.model}, color : {self.color}, speed : {self.speed}")

car_info = Car("Sonata", "white", 80) # 인스턴스 = 클래스명()
car_info.info()


class Talent:

    def __init__(self, work="가수", birth="1993년 5월 16일", public="대한민국"):
        self.work = work
        self.birth = birth
        self.public = public
        print(f"직업 : {work} \n생년월일 : {birth} \n국적 : {public}")

    def rap(self):
        print(f"랩")

    def dance(self):
        print(f"춤")

    def somall(self):
        print(f"소몰이")

tal = Talent()
tal.rap()
tal.dance()
tal.somall()

# ClassMethod

class Talent:
    work = "가수"
    birth = "1993년 5월 16일"
    public = "대한민국"
    print(f"직업 : {work} \n생년월일 : {birth} \n국적 : {public}")

    @classmethod
    def rap(cls):
        print(f"랩")

    @classmethod
    def dance(cls):
        print(f"춤")

    @classmethod
    def somall(cls):
        print(f"소몰이")

tal = Talent()
tal.rap()
tal.dance()
tal.somall()

# ClassMethod

class Talent:
    work = "가수"
    birth = "1993년 5월 16일"
    public = "대한민국"
    print(f"직업 : {work} \n생년월일 : {birth} \n국적 : {public}")

    @staticmethod
    def rap():
        print(f"랩")

    @staticmethod
    def dance():
        print(f"춤")

    @staticmethod
    def somall():
        print(f"소몰이")

tal = Talent()
tal.rap()
tal.dance()
tal.somall()