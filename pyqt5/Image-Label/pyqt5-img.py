import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QPushButton, QApplication, QLineEdit)
from PyQt5.QtGui import QPixmap
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):      
        hbox = QHBoxLayout(self)
        textbox = QLineEdit()
        btn = QPushButton('Открыть картинку')
        lbl = QLabel('Здесь будет картинка')
        btn.clicked.connect(lambda checked, l=lbl,t=textbox : self.foto(t,l))
        hbox.addWidget(textbox)
        hbox.addWidget(btn)
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.move(100, 200)
        self.setWindowTitle('Вывод изображения QPixmap')
        self.show()

    def foto(self,t,l):
        img = t.text()
        pixmap = QPixmap(img)
        l.setPixmap(pixmap)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
