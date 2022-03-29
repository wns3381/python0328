# ClassInstance.py

# 클래스 : 새로운 Type을 정의 
class Person:    
    # 초기화 (생성자)
    def __init__(self):
        # 인스턴스 멤버 변수를 초기화(복사본)
        self.name = "Default Name"

    def Print(self):
        print("My Name is {0}".format(self.name))

p1 = Person()
p2 = Person()
p1.Print()

p1.name = " 내이름은 김연아!"
p1.Print()

p2.name = "김연아"
print("p2's name:", p2.name)

Person.title = "New title"
print("p1's title: ", p1.title )
    