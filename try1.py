# try1.py

# 함수정의 
def divide(a, b):
    return a/b

# 에러처리
try:
    result = divide(5, 3)
except ZeroDivisionError:
    print("두번재 인자는 0이어서는 안됩니다.")
except TypeError:
    print("모든 인자는 숫자여야 합니다.")
except:
    print('음~ 무슨 에러인지 모르겠어요')
else:

    print("결과{0}".format(result))
finally:
    print("무조건 실행(이중체크)")

# 호출
# divide(5,3)
# print("결과{0}".format(result))
print("전체 코드 실행 종료")