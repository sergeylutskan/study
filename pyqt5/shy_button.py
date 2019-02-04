import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.Qt import *
from shy_button_ui import Ui_MainWindow
from random import *

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.setupUi(self)


     
    def mouseMoveEvent(self, event):
        print(self.pushButton.pos().x())
        print(random.randint(-100,100))
        if (event.x() >= self.pushButton.pos().x()) and (event.x() <= self.pushButton.pos().x()+60) and (event.y() >= self.pushButton.pos().y()) and (event.y() <= self.pushButton.pos().y()+30):
            self.pushButton.move(self.pushButton.pos().x()+random.randint(-100,100),self.pushButton.pos().y()+random.randint(-100,100))

     
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
