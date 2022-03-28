# function2.py

# 함수 내부의 이름을 해석하는 규칙(DGB)
# 전역변수
x = 2

# 함수정의
def func(a):
    return a+x

# 함수호출
print(func(1))

# 함수정의

def func2(a):
    # 지역변수 (우선)
    x = 5
    return a+x

#호출 
print(func2(1))

# 기본값이 있는 경우 
def times(a=10, b=20):
    return a*b

# 호출
print(times())
print(times(5))
print(times(5,6))
print(times(b=2))

# 키워드 인자 (파라미터명을 명시)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

# 호출
# 중지점(Break point for debug)
print(connectURI("credu.com", "80"))
print(connectURI(port="80", server="credu.com"))

