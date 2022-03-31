# DemoForm2.py
# DemoForm2.ui(화면)  + DemoForm2.py(로직단)
import sys
from PyQt5.QtWidgets import*
from PyQt5 import uic

# 웹크롤링
import urllib.request
from bs4 import BeautifulSoup

# 디자인 파일을 로딩 
form_class = uic.loadUiType("c:\\work\\DemoForm2.ui")[0]

# 클래스 정의 (QMainWindow 클래스, 상속) : 다중상속은  C++ / Python 정도만 허용
class DemoForm(QMainWindow, form_class):
    #  초기화 메서드 (self, this, super, base)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("두번째 Qt GUI 데모")

    # slot 메서드 정의 
    def firstClick(self):
        # 네이버 웹툰 크롤링        
        f = open("webtoons.txt", "a+", encoding="utf-8")

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
                f.write(title)
                f.write("  링크 : " + link + "\n")  

        self.label.setText("네이버 웹툰 리스트 크롤링")
        f.close()

    def secondClick(self):
        self.label.setText("두번째 버튼 클릭")

    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭")

# 실행프로세스 (ex. Excel.exe)
app = QApplication(sys.argv)
# 인스턴스를 생성 
demoWindow = DemoForm()
# Show() 메서드를 통한 전시 
demoWindow.show()
# 이벤트 루프(이벤트 발생 보기)
app.exec_()

