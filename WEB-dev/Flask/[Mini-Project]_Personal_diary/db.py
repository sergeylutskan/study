import sqlite3 
class DB:
    def __init__(self):
        conn = sqlite3.connect('tmp.db', check_same_thread=False)
        self.conn = conn # запоминаем в классе подключение к БД
    def get_connection(self):
        return self.conn # возвращаем ссылку на подключение
    def __del__(self):
        # уничтожаем объект
        self.conn.close()
    # закрываем соединение с БД
