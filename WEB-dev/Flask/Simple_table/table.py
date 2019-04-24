from flask import Flask, url_for

app = Flask(__name__)


@app.route('/table/<int:m>/<int:n>')
def table(m, n):
    res = []
    for i in range(m):
        res.append("<tr>")
        #res.append("".join([f'<td>({i}, {j})</td>' for j in range(n)]))
        res.append("".join(['<td>('+ str(i)+', '+str(j)+')</td>' for j in range(n)]))
        res.append("</tr>")
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
        <h1>Привет! Вы ввели:</h1>
        <table class="table">
       ''' + res 
    res = res + "</table></body></html>"
    return res


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
