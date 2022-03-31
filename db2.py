# db1.py 
import sqlite3

# 전역함수로 연결객체 리턴 (dB 파일 활용한 영구적 저장) 
con = sqlite3.connect("c:\\work\\sample.db")

# 두번째 인스턴스인 커서를 리턴 받기 
cur = con.cursor()

# 테이블을 가장 먼저 생성
# ANSI SQL 92, 99 (미국 표준안)
cur.execute("create table PhoneBook(name text, phoneNum text);")

# 1건을 입력 
print("----- 메소드를 이용한 1건 직접 입력-----")
cur.execute("insert into PhoneBook values ('derkck', '010-2222-3333');")

# 입력 파라미터 처리 
print("----- 인자를 이용한 DB 입력-----")
name = "김  준"
phoneNumber = "010-3060-3381"
cur. execute("INSERT INTO PhoneBook VALUES(?,?);", (name, phoneNumber))

# 여러건을 입력 (배열의 배열 / 2차원 배열)
print("----- 객체를 이용한 연속적 입력-----")
datalist = (('박영란', '010-2292-8728'), ('김민지',  '010-5543-8728'), ('김민주', '010-5122-8728'))
cur.executemany("INSERT INTO PhoneBook VALUES(?,?);", datalist)

cur.execute("select * from PhoneBook;")
print(cur. fetchall())    

# 작업완료(정상적인 작업종료)
con.commit()