# function3.py

# 가변인자 포함 함수 정의 
def union(*ar):
    # 지역변수를 리스트로 초기화
    result = []
    for item in ar:
        for x in item:
            if not x in result:
                result.append(x)
    return result

# 호출
print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))
print(union("girl", "generation", "gee"))

# 정의되지 않은 인자 처리하기 
def userURIBuilder(server, port, **user):
    str = "http://"+server + ":"+ port +"/?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

print(userURIBuilder("test.com", "8080", id='userid', passwd='1234'))
print(userURIBuilder("test.com", "8080", id='userid', passwd='1234', name='mike', age='20'))


# 람다함수
g = lambda x,y : x*y
print(g(2,3))

print((lambda x : x*x)(3))
print(globals())
