from flask import Flask, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "<h1>Привет!</h1>"


@app.route('/greeting_form', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return '''
           <html>
            <head>
              <meta charset="utf-8">
              <link rel="stylesheet" 
                            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
              <title>Форма для приветствия</title>
            </head>
            <body>
               
	<h1 class="h1">Форма для приветствия</h1>
	<form method="post">
	<div>Введите имя:
	<br>
	<input class="form-control" type="text" placeholder="Введите имя" name="fio">
	</div>
	<br />
	<div>
	<button class="btn btn-primary" type="submit">Отправить</button>
	</div>
	</form> 		   
			   
			   
            </body>
            </html>'''


    
    elif request.method == 'POST':
        print(request.form['fio'])
        a = '''
        <html>
            <head>
              <meta charset="utf-8">
              <link rel="stylesheet" 
                            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
              <title>Приветствие</title>
            </head>
            <body>
               
	<h2 class="h2">Привет, 
	'''
        b = '''
        </h2>

            </form> 		   
			   
			   
            </body>
        </html>'''
        return a + request.form['fio'] +  b      


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
