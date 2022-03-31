# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
# 정규표현식으로 검색 
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

f = open("C:\\work\\clien.txt", "wt", encoding = "utf-8")

# 페이징 처리 0번에서 9번까지  
for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(data)
        #웹브라우져 헤더 추가        
        req = urllib.request.Request(data, headers = hdr)
        data = urllib.request.urlopen(req).read()

        # 한글이 깨지는 경우는 디코딩이 필요
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        
        # <span class="subject_fixed" data-role="list-title-text" title="서피스북3 15인치 i7 256gb">
        #                     서피스북3 15인치 i7 256gb
        # </span>

        #list = soup.findAll('a', attrs={'class':'list_subject'})
        # find_all(태그), attributes(속성들)
        list = soup.find_all('span', attrs ={'data-role':'list-title-text'})

        for item in list:
                try:
                        title = item.text                                      
                        # print(title.strip()) 
                        if (re.search('아이폰', title)):
                                print(title.strip())
                                f.write(title.strip() + "\n")
                except:
                        pass

f.close()
print("크롤링 종료")