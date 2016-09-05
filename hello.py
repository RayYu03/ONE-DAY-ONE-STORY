# -*- coding:utf-8 -*-

from flask import Flask, render_template,redirect
from flask_script import Manager
from flask_bootstrap  import Bootstrap

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/readme/')
def readme():
    return redirect('http://www.nijintianzhenhaokan.party')


if __name__ == '__main__':
    manager.run()
