# -*- coding: utf-8 -*-
from __init__ import app
from flask import render_template

@app.route('/',methods=['GET','POST'])
def test():
    return render_template('index.html')
if __name__ == '__main__':
    # app.run('0.0.0.0',8000)
    app.run()