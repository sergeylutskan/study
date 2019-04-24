from flask import Flask, url_for

app = Flask(__name__)


@app.route('/list/<int:m>')
def list(m):
    res = []
    for i in range(m):
        res.append('<li class="list-group-item">')
        res.append("Элемент списка №" + str(i+1))
        res.append("</li>")
    res = ''.join(res)
    res = '''
      <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" >
        </head>
        <body>
        <h1>Мы сгенерировали список:</h1>
        <ol class="list-group">
       ''' + res 
    res = res + "</ol></body></html>"
    return res


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
