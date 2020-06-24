class Person:
    population = 0
    # 생성자
    # 인스턴스를 생성하기 위하여 호출되는 함수
    # Person(..)
    def __init__(self, name):
        self.name = name
        Person.population += 1
    
    # 인스턴스 메서드
    def greeting(self):
        print(self.name + ': hi!')

    @classmethod
    def get_pop(cls):
        return cls.population

    def __repr__(self):
        return self.name

# OOP
# 객체지향프로그래밍
# 객체 '지향' => 절차 지향
# 데이터를 중심으로 동작 + 정보
# 동작 => 메서드(greeting)
# 정보 => 변수(name)

num = 1 
def foo():
    num = 2 
    print(num)

