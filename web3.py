# web3.py

# 웹서버와 통신할 경우 사용 
import urllib.request
# 크롤링에 사용 
from bs4 import BeautifulSoup

# 파일로 저장
f = open("C:\\work\\webtoons.txt", "wt", encoding = "utf-8")

for i in range(1,6):

    # 페이지 처리 (1페이지가 10개 항목 * 5 페이지)
    url = "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri&page=" + str(i)
    print(url)

    data = urllib.request.urlopen(url)
    soup = BeautifulSoup(data, "html.parser")

    cartoons = soup.find_all("td", class_="title")
    
    for item in cartoons:
        title = item.find("a").text
        link = item.find("a")["href"]
        # title = item.text.strip()    
        print(title)
        print(" 링크 : " + link)
        f.write(title)
        f.write("   링크 : " + link + "\n")  

f.close()
print("크롤링 작업 종료")


