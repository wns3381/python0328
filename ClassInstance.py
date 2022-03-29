# ClassInstance.py

# 클래스 : 새로운 Type을 정의 
from asyncio import SendfileNotAvailableError


class Person:  
    # 클레스 멤버 변수 (Static  키워드 없이 위치를 가지고 구분)
    num_person = 0

    # 초기화 (생성자 메서드)
    def __init__(self):
        # 인스턴스 멤버 변수를 초기화(복사본)
        self.name = "Default Name"
        Person.num_person += 1
    def Print(self):
        print("My Name is {0}".format(self.name))

# 인스턴스 생성 
p1 = Person()
p2 = Person()
print("인스턴스 개수 :{0}".format(Person.num_person))

p1.Print()
p1.name = " 내이름은 김연아!"
p1.Print()

p2.name = "김연아"
print("p2's name:", p2.name)

Person.title = "New title"
print("p1's title: ", p1.title )
p2.title = "Researcher"
print("p2's title: ", p2.title )

p1.age = 20
print("p1's age: ", p1.age)
#print("p1's age: ", p2.age)

# 멤버 메서드에서 self가 누락된 경우
str = "Not Class Member"
class GString:
    # 인스턴스 멤버 변수 
    def __init__(self):
        self.str = []
    def Set(self, msg):
        self.str = msg
    def Print(self):
        print(str)
    def Print1(self):
        print(self.str)

g = GString()
g.Set("First Message")
g.Print()
g.Print1()

