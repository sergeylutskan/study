import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidget, QTableWidgetItem
from table1 import Ui_MainWindow
 
 
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        f = ''
        xn = 0
        n = 0
        s = 0
        self.tableWidget.setHorizontalHeaderLabels(['Точка x', 'Значение f в точке х'])
        self.tableWidget.resizeColumnsToContents()

    
    def run(self):
        
        f = self.lineEdit.text()
        xn = int(self.lineEdit_2.text())
        n = int(self.lineEdit_3.text())
        s = int(self.lineEdit_4.text())
        self.tableWidget.setRowCount(n)
        print(f,xn,n,s)
        k = 0
        for x in range(xn,xn+n*s+1,s):
            print(eval(f))
            self.tableWidget.setItem(k, 0, QTableWidgetItem(str(x)))
            self.tableWidget.setItem(k, 1, QTableWidgetItem(str(eval(f))))
            k = k+1
            

            
        
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
