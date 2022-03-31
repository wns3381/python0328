# web2.py

# 웹서버와 통신할 경우 사용 
import urllib.request
# 크롤링에 사용 
from bs4 import BeautifulSoup

data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
soup = BeautifulSoup(data, "html.parser")

# 블럭 주석 : ctrl + / 
# <td class="title">
# 	<a href="/webtoon/detail?titleId=20853&no=50&weekday=fri" ">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>

cartoons = soup.find_all("td", class_="title")
print("개수:{0}".format(len(cartoons)))
title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title)
print(link)

# 파일로 저장
f = open("C:\\work\\webtoons.txt", "wt", encoding = "utf-8")
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


