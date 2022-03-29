# if / elif / else 조건문 
# ifelse.py

score =  int(input("점수를 입력 : "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
elif 50 <= score < 60:
    grade = "E"
else:
    grade = "F"

print("등급은 : ", grade)



momey = 50
item = "apple" if momey > 100 else "banana"
print(item)
    

lst = [100, "문자열", 3.14]
for item in lst:
    print(item, type(item))
