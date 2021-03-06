import os

from flask import Flask, render_template, url_for, redirect, send_from_directory

app = Flask(__name__)




@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/home/')
def home():
    return render_template('Basic-Header.html')

@app.route('/bonkers/')
def bonkers():
    return '<h1>bonkers</h1>'

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/info/')
def info():
    return render_template('info.html')

@app.route('/play/')
def play():
    return render_template('game/index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'assets/img/favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
   app.run(debug = True)
