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
    return 'jaisodfjasdfijasoufbuiawfoijaweufhiuwhefouhaseifhaishdfhafh\nbonkers'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'assets/img/favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
   app.run(debug = True)
