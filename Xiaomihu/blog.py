# -*- coding: utf-8 -*-
from __init__ import app
from model import Blog,db,BlogType
from form import PostForm
from flask import render_template,jsonify,request,Response,redirect,url_for
from flask import Blueprint
import json
blog = Blueprint('blog',__name__)

# 博客索引页面
@app.route('/blog/blogIndex',methods=['GET'])
def blogIndex():
    page = request.args.get('page',1)
    blogItems = db.session.query(Blog).join(BlogType,Blog.typeId == BlogType.id).order_by(Blog.addTime.desc()).paginate(int(page), per_page=4, error_out=False)
    return render_template('new_blog_index.html',blogItems=blogItems)

# 博客详情页面
@app.route('/blog/blogDetail',methods=['GET'])
@app.route('/blog/blogDetail/<string:blogId>.html',methods=['GET'])
def blogDetail(blogId):
    blogItem = Blog.query.filter(Blog.id==blogId).first()
    blogTypeItem = BlogType.query.filter(BlogType.id==blogItem.typeId).first()
    return render_template('new_blog_detail.html',blogItem=blogItem,blogTypeItem=blogTypeItem)

# 博客上传页面
@app.route('/blog/blogAdmin',methods=['GET','POST'])
def blogAdmin():
    form = PostForm()
    if form.validate_on_submit():
        title = request.form['title']
        typeId = request.form['typeId']
        img64base = request.form['img64base']
        content = request.form['fancy-editormd-html-code'].strip()
        blogData = Blog(title=title, typeId=typeId, img64base=img64base, content=content)
        db.session.add(blogData)
        db.session.commit()
        return redirect(url_for('blogIndex'))
    return render_template('blogAdmin.html',form=form)

@app.route('/blog/blogType/<string:typeId>',methods=['GET'])
def blogType(typeId):
    return typeId