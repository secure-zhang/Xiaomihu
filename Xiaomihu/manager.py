# -*- coding: utf-8 -*-
from __init__ import app
from flask import render_template

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('new_base.html')

@app.route('/index',methods=['GET','POST'])
def base():
    return render_template('base.html')

@app.route('/xk',methods=['GET','POST'])
def xk():
    return render_template('xk.html')

if __name__ == '__main__':
    app.run('0.0.0.0',8000)
    # app.run()