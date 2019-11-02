# -*- coding: utf-8 -*-
from __init__ import app
from flask import render_template
from flask import Blueprint
photo = Blueprint('photo',__name__)

@app.route('/photo/index',methods=['GET'])
def photoIndex():
    # photo1和photo2为不同的展示图片的效果
    return render_template('photo1.html')
    # return render_template('photo2.html')
