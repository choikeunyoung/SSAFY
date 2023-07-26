# 클래스 정의
class Person:
    # 속성(변수)
    blood_color = 'red'

    # 메서드 
    # 자연스럽게 동작함
    def __init__(self, name):
        self.name = name
    
    def singing(self):
        return f'{self.name}가 노래합니다.'

# 인스턴스 생성
singer1 = Person("iu")
singer2 = Person("BTS")

# 메서드 호출
print(singer1.singing())
print(singer2.singing())

# 속성(변수) 사용
print(singer1.blood_color)
print(singer2.blood_color)

# 클래스 변수의 활용
class Person():
    count = 0 # 클래스 변수

    def __init__(self, name): # 생성자 함수
        self.name = name # 인스턴스 변수
        Person.count += 1

# 인스턴스를 생성할때마다 count가 1씩 증가
person1 = Person("에스파")
person2 = Person("BTS")

print(Person.count)