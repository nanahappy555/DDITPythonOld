"""
버튼 클릭하면 good evening으로 바뀌게
"""
from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication
import sys


# ui파일 연결
form_class = uic.loadUiType("myqt01.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.buttonClick)
        
    
    def buttonClick(self):
        print("pushbutton click")
        self.lbl.setText("good evening~~~")
        
    
if __name__ == "__main__":
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()