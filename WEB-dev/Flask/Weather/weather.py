import json

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/weather', methods = ['GET','POST'])
def weather():
    with open('weather.json') as f:
        weather_list = json.loads(f.read())    
    if request.method == 'GET':
        return render_template('weather.html', title='Погода', weather=weather_list)
    elif request.method == 'POST':
        return render_template('weather.html', title='Погода', weather=weather_list, choose=request.form.get('weather'))

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
