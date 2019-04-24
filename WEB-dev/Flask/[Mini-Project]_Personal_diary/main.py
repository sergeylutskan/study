from flask import Flask, request, render_template, redirect
from db import DB
from newsmodel import NewsModel
from usermodel import UsersModel
from add_news import AddNewsForm, LoginForm
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

session = {}
db = DB()
con = db.get_connection()
print(con)
nws = NewsModel(con)
nws.init_table()

print(nws.get_all())
cursor = nws.connection.cursor()
cursor.execute("SELECT * FROM news ")
rows = cursor.fetchall()
print(rows)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        user_name = form.username.data
        password = form.password.data 
        user_model = UsersModel(db.get_connection())
        user_model.init_table()
        
        exists = user_model.exists(user_name, password)
        if (exists[0]):
            session['username'] = user_name
            session['user_id'] = exists[1]
        if user_name != 'admin':
            return redirect("/index")
        else:
            return redirect("/admin")
    else:
        return render_template('login.html', title='Авторизация', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form = LoginForm()
    if request.method == 'POST':
        user_name = form.username.data
        password = form.password.data 
        user_model = UsersModel(db.get_connection())
        user_model.init_table()
        user_model.insert(user_name,generate_password_hash(password))
        exists = user_model.exists(user_name, password)

        if (exists[0]):
            session['username'] = user_name
            session['user_id'] = exists[1]
            
        return redirect("/index")
    else:
        return render_template('register.html', title='Регистрация', form=form)



@app.route('/logout')
def logout():
    session.pop('username',0) # "забыть" информацию
    session.pop('user_id',0)
    return redirect('/login')


@app.route('/')
@app.route('/index')
def index():
    if 'username' not in session:
        return redirect('/login')
    news = NewsModel(db.get_connection()).get_all(session['user_id'])
    return render_template('index.html', username=session['username'], news=news)

@app.route('/admin')
def admin():
    if session['username'] != 'admin':
        return redirect('/login')
    else:
        c = []
        users = UsersModel(db.get_connection()).get_all()
        for user in users:
            news = NewsModel(db.get_connection()).get_all(user[0])
            c.append([user[1],len(news)])
        return render_template('admin.html', username=session['username'], news=c)


@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    if 'username' not in session:
        return redirect('/login')
    form = AddNewsForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        nm = NewsModel(db.get_connection())
        nm.insert(title,content,session['user_id'])
        return redirect("/index")
    return render_template('add_news.html', title='Добавление новости', form=form, username=session['username'])

@app.route('/delete_news/<int:news_id>', methods=['GET'])
def delete_news(news_id):
    if 'username' not in session:
        return redirect('/login')
    nm = NewsModel(db.get_connection())
    nm.delete(news_id)
    return redirect("/index")

@app.route('/sort_by/<int:sort>', methods=['GET'])
def sort_by(sort):
    if 'username' not in session:
        return redirect('/login')
    nm = NewsModel(db.get_connection())
    news = nm.sort(sort, user_id=session['user_id'])
    return render_template('index.html', username=session['username'], news=news)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
