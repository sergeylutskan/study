#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QPushButton, QApplication, QLCDNumber)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        num1 = QLabel('Число 1')
        num2 = QLabel('Число 2')
        num3 = QLabel('Сложение')
        num4 = QLabel('Вычитание')
        num5 = QLabel('Произведение')
        num6 = QLabel('Деление')
        
        num11 = QLineEdit()
        num22 = QLineEdit()
        lcd1=QLCDNumber()
        lcd2=QLCDNumber()
        lcd3=QLCDNumber()
        lcd4=QLCDNumber()
        btn=QPushButton()
        btn.setText('Рассчитать')
       
       
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(num1, 1, 0)
        grid.addWidget(num11, 1, 1)

        grid.addWidget(num2, 2, 0)
        grid.addWidget(num22, 2, 1)

        grid.addWidget(num2, 2, 0)
        grid.addWidget(num22, 2, 1)

        grid.addWidget(lcd1, 4, 1)
        grid.addWidget(lcd2, 5, 1)
        grid.addWidget(lcd3, 6, 1)
        grid.addWidget(lcd4, 7, 1)
        grid.addWidget(num3, 4, 0)
        grid.addWidget(num4, 5, 0)
        grid.addWidget(num5, 6, 0)
        grid.addWidget(num6, 7, 0)
        grid.addWidget(btn, 3, 0)
        
        self.setLayout(grid)


        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Миникалькулятор')
        btn.clicked.connect(lambda checked, q1=num11,q2=num22,l1=lcd1, l2=lcd2, l3=lcd3, l4=lcd4 : self.calc(q1,q2,l1,l2,l3,l4))
        
        self.show()
        
    def calc(self,q1,q2,l1,l2,l3,l4):
        a=int(q1.text())
        b=int(q2.text())
        l1.display(a+b)
        l2.display(a-b)
        l3.display(a*b)
        l4.display(a/b)
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
