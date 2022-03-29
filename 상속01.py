# 부모 클래스 정의 
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

# 자식 클래스 정의 
class Student(Person):
    # 생성자 재정의 (override) - 멤버변수가 추가 
    # 상속받은 메서드를 재정의(덮어쓰기,Override)
    def __init__(self, name, phoneNumber, subject, studentID):
        # 명시적으로 부모 생성자를 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1}, Subject: {2}, \
                 StudentID: {3})".format(self.name, self.phoneNumber, self.subject, self.studentID))

# 인스턴스 생성 
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "소프트웨어 공학", "20221122")

# 클래스의 변수를 Dict로 호출 
print(p.__dict__)
print(s.__dict__)

p.printInfo()
s.printInfo()







