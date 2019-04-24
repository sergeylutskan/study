import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from text_red_ui import Ui_MainWindow
 
 
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.open)


    
    def save(self):
        t = self.textEdit.toPlainText()
        with open('1.txt','w') as f:
            f.write(t)
        

    def open(self):
        with open('1.txt','r') as f:
            x = f.read()
        self.textEdit.setPlainText(x)
            

            
        
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
