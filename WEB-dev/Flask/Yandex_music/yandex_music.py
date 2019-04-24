from flask import Flask, url_for

app = Flask(__name__)


@app.route('/yandex_music/')
def music():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" 
                    >                  </head>
                  <body>
                    <h1>Послушаем музыку:</h1>
                    <div>
                <iframe frameborder="0" style="border:none;width:600px;height:100px;" width="600" height="100" src="https://music.yandex.ru/iframe/#track/49961817/6876308/">Слушайте <a href='https://music.yandex.ru/album/6876308/track/49961817'>Грустный дэнс</a> — <a href='https://music.yandex.ru/artist/666984'>Artik & Asti</a> на Яндекс.Музыке</iframe>
                </div>
                  </body>
                </html>'''



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
