# -*- coding: utf-8 -*-
# 博客展示view
from __init__ import app
from model import Blog,db,BlogType
from form import PostForm
from flask import render_template,jsonify,request,Response,redirect,url_for
from flask import Blueprint
import datetime
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
    return render_template('new_blog_admin.html',form=form)

# 博客分类页面
@app.route('/blog/blogType/<string:typeId>',methods=['GET'])
def blogType(typeId):
    return typeId

# 博客评论页面
@app.route('/blog/blogComment/',methods=['GET'])
def blogComment():
    return '1'


# 自定义时间过滤器
@app.template_filter("time_filter")
def time_filter(time):
    if not isinstance(time, datetime.datetime):
        return time
    _period = (datetime.datetime.now() - time).total_seconds()
    if _period < 60:
        return "刚刚"
    elif 60 <= _period < 3600:
        return "%s分钟前" % int(_period / 60)
    elif 3600 <= _period < 86400:
        return "%s小时前" % int(_period / 3600)
    elif 86400 <= _period < 2592000:
        return "%s天前" % int(_period / 86400)
    else:
        return time.strftime('%Y-%m-%d %H:%M')