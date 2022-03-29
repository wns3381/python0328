# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    # 초기값을 셋팅(인스턴스)
    def __init__(self, id, name, balance):
        # 멤버 변수를 숨김 
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    # 입금
    def deposit(self, amount):
        self.__balance += amount 
    # 출금
    def withdraw(self, amount):
        self.__balance -= amount
    # 문자열 리턴(ToString() 메서드)
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1)
# 멤버변수에 접근
account1.__balance = 15000000
print(account1.__balance)
# _클래스명__변수명(이름변경) : 백도야 
print(account1._BankAccount__balance)
