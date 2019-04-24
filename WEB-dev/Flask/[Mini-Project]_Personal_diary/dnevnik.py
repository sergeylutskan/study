import sqlite3
from werkzeug.security import generate_password_hash
hash = generate_password_hash('yandexlyceum')
print(hash)

con = sqlite3.connect('tmp.db', check_same_thread=False)

print(con)

cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS news ( id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(100), content VARCHAR(1000), user_id INTEGER)''')
cursor.close()
con.commit()

cursor = con.cursor()
cursor.execute('''INSERT INTO news (title, content) VALUES (?,?)''', (input(), input()))
cursor.close()
con.commit()

cursor = con.cursor()
cursor.execute("SELECT * FROM news ")
rows = cursor.fetchall()
cursor.close()
con.close()
print(rows)



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
