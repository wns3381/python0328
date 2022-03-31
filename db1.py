# db1.py 
import sqlite3

# 전역함수로 연결객체 리턴 (dB 파일 활용 
# con = sqlite3.connect("c:\\work\\test.db")

# 전역함수로 연결객체 리턴 (메모리 작업)
con = sqlite3.connect(":memory:")


# 두번째 인스턴스인 커서를 리턴 받기 
cur = con.cursor()

# 테이블을 가장 먼저 생성
# ANSI SQL 92, 99 (미국 표준안)
cur.execute("create table PhoneBook(name text, phoneNum text);")

# 1건을 입력 
print("----- 메소드를 이용한 1건 직접 입력-----")
cur.execute("insert into PhoneBook values ('derkck', '010-2222-3333');")

# 검색하기 
cur. execute("select * from PhoneBook;")
for row in cur:
    print(row)

# 입력 파라미터 처리 
print("----- 인자를 이용한 DB 입력-----")
name = "김  준"
phoneNumber = "010-3060-3381"
cur. execute("INSERT INTO PhoneBook VALUES(?,?);", (name, phoneNumber))
cur. execute("select * from PhoneBook;")
for row in cur:
    print(row)

# 여러건을 입력 (배열의 배열 / 2차원 배열)
print("----- 객체를 이용한 연속적 입력-----")
datalist = (('박영란', '010-2292-8728'), ('김민지',  '010-5543-8728'), ('김민주', '010-5122-8728'))
cur.executemany("INSERT INTO PhoneBook VALUES(?,?);", datalist)

cur.execute("select * from PhoneBook;")
print("----- fetchone() 출력 -----")
print(cur. fetchone())    
print("----- fetchmany(2) 출력 -----")
print(cur. fetchmany(2))    
print("----- fetchall() 출력 -----")
print(cur. fetchall())    

print("----- re-search / fetchall() 출력 -----")
cur.execute("select * from PhoneBook;")
print(cur. fetchall())    