# -*- coding: utf-8 -*-
from __init__ import app
from flask import render_template
from flask import Blueprint
blog = Blueprint('blog',__name__)

@app.route('/blog/index',methods=['GET'])
def blogIndex():
    return render_template('blog.html')