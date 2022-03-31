# DemoFile.py

for x in range(1,6):
    print(x, '*', x, '=', x*x)

print("---약간 서식을 벼녕 ---")
for x in range(1,6):
    print(x, '*', x, '=', str(x*x).rjust(3))

for x in range(1,6):
    print(x, '*', x, '=', str(x*x).zfill(3))

# 문자열 결합연산
url = "http://www.credu.com/?page="
print(url+str(1))

print("--서식 문자--")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(1500000000))

# 파일에 쓰기
f= open("c:\\work\\demo.txt", "wt", encoding = "utf-8")
f.write("한글 데이터\nabcd\n1234\n")
f.close()
print(f.closed)


# 파일을 읽기 (r : raw string 표기법 --> 가공하지 않은 문자열 처리)
f = open(r"c:\work\demo.txt", "rt", encoding = "utf-8")
# 첫줄부터 끝가지 읽어서 str로 리턴
result = f.read()
print(result)
print("어디쯤:", f.tell())
# 파일 커서를 파일 처음으로 이동 
f.seek(0)
print("어디쯤:", f.tell())
# 텍스트 파일을 한 줄단위로 읽음
print(f.readline(), end="")
print("어디쯤:", f.tell())
print(f.readline(), end="")
print("어디쯤:", f.tell())


# 리스트로 받기 
f.seek(0)
result = f.readlines()
print(result)
f.close()

# with 구문을 사용하기 
print("--- with 구문을 사용하기")
with open("c:\\work\\demo.txt", "rt", encoding = "utf-8") as f:
    print(f.read())
    f.seek(0)
    for item in f.readline():
        print(item)
