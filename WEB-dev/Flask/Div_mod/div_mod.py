import json

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/div_mod', methods = ['GET','POST'])
def weather():
    if request.method == 'GET':
        return render_template('div_mod.html', title='Проверка делимости')
    elif request.method == 'POST':
        if int(request.form.get('num2')) == 0:
            return render_template('div_result.html', title='Проверка делимости', result='На ноль делить нельзя')
        if int(request.form.get('num1')) % int(request.form.get('num2')) == 0:
            return render_template('div_result.html', title='Проверка делимости', result= request.form.get('num1') + ' делится на ' + request.form.get('num2'))
        else:
            return render_template('div_result.html', title='Проверка делимости', result=request.form.get('num1') + ' не делится на ' + request.form.get('num2'))
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
