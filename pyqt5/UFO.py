#импортируем модуль для работы с системой
import sys
#Импортируем необходимые для работы программы классы (Приложение, Виджет, Основное окно)
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
#импортируем все из подраздела PyQt5.Qt (без этого не заработает Pixmap - наша картинка НЛО)
from PyQt5.Qt import *
#импортируем сгенерированный из дизайнера код формы nlo_ui
from ufo_ui import Ui_MainWindow

#создаем основной класс MyWidget, который унаследован от классов QMainWindow(встроен в PyQT5) и Ui_MainWindow(содержится в файле nlo_ui)
class MyWidget(QMainWindow, Ui_MainWindow):
    #функция инициализации, выполняющаяся сразу при старте программы
    def __init__(self):
        #вызвать функцию инициализации родительского класса для отрисовки окна, созданного в дизайнере и описанного в nlo_ui
        super().__init__()
        #вызвать функцию отрисовки окна из nlo_ui
        self.setupUi(self)
        #задаем начальные координаты положения нашего НЛО
        self.x = 250
        self.y = 250
        #перемещаем наше НЛО (имеет тип QLabel) в эти координаты
        self.nlo.move(self.x,self.y)
        #вешаем на наш QLabel картинку НЛО
        self.nlo.setPixmap(QPixmap('1.jpg'))

    #функция вызывается от 2 аргументов - сам класс(self) и событие (event)
    def keyPressEvent(self, event):
        #если нажата клавиша "Влево", то переместить по оси Х наше НЛО в меньшую сторону
        if event.key() == Qt.Key_Left:
            self.x = (self.x - 20)%600
            #окно имеет размер 600*600, поэтому мы вычисляем остаток от деления на 600, чтобы выходя за границы окна, НЛО возвращалось с другой стороны
            self.nlo.move(self.x,self.y)
        #если нажата клавиша "Вверх", то уменьшаем ось Y и перемещаем наше НЛО в новые координаты
        #остальное аналогично для клавиш "Вниз" и "Вправо".
        if event.key() == Qt.Key_Up:
            self.y = (self.y - 20)%600
            self.nlo.move(self.x,self.y)
        if event.key() == Qt.Key_Down:
            self.y = (self.y + 20)%600
            self.nlo.move(self.x,self.y)
        if event.key() == Qt.Key_Right:
            self.x = (self.x + 20)%600
            self.nlo.move(self.x,self.y)          
#следует обратить внимание, что Вверх уменьшает ось Y, а Вниз - увеличивает, хотя и кажется, что должно быть наоброт :)     

#функции отрисовки окна в системе
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
