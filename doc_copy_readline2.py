# 8장 파일처리와 정규표현식 활용 
import re 

# 파일 오픈 
f=open('c:\\work\\PV3.txt','rt')
g=open('c:\\work\\PV3_copy.txt','wt',encoding='utf-8')

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
# EOF가 아니면 반복
while (line != ''):
    if (re.search("\d{4}", line)):
        g.write(line + "\n")
    line = f.readline()

f.close() 
g.close()




f1=open('c:\\work\\PV3.txt','rt')
g1=open('c:\\work\\PV3_copy_2.txt','wt',encoding='utf-8')

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f1.readline()
# EOF가 아니면 반복
while (line != ''):
    if (re.search("error", line)):
        g1.write(line + "\n")
    line = f1.readline()

f1.close() 
g1.close()





