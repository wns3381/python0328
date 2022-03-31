# DemoForm.py
# DemoForm.ui(화면)  + DemoForm.py(로직단)

import sys
from PyQt5.QtWidgets import*
from PyQt5 import uic

# 디자인 파일을 로딩 
form_class = uic.loadUiType("c:\\work\\DemoForm.ui")[0]

# 클래스 정의 (QDialog 클래스, 상속) : 다중상속은  C++ / Python 정도만 허용
class DemoForm(QDialog, form_class):
    #  초기화 메서드 (self, this, super, base)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 Qt 데모")

# 진입점 체크 : 직접 이 모듈을 실행한 경우는 프로세서를 만들고 창을 보여줌.
# C 언어는 main() 함수가 진입점(Entry point)
if  __name__ == "__main__":
    # 실행프로세스 (ex. Excel.exe)
    app = QApplication(sys.argv)
    # 인스턴스를 생성 
    demoWindow = DemoForm()
    # Show() 메서드를 통한 전시 
    demoWindow.show()
    # 이벤트 루프(이벤트 발생 보기)
    app.exec_()

