from werkzeug.security import generate_password_hash, check_password_hash

class UsersModel:
    def __init__(self, connection):
        self.connection = connection
    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_name VARCHAR(50), password_hash VARCHAR(128))''')
        cursor.close()
        self.connection.commit()
    def insert(self, user_name, password_hash):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users (user_name, password_hash) VALUES (?,?)''', (user_name, password_hash))
        cursor.close()
        self.connection.commit()
    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(user_id),))
        row = cursor.fetchone()
        return row
    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows
    def exists(self, user_name, password):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name = ?", (user_name,))
        row = cursor.fetchone()
        if row:
            check = check_password_hash(row[2],password)
            return (True, row[0]) if check else (False,)
        else:
            return (False,)
