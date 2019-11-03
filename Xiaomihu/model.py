from __init__ import app
from _datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# 配置mysql数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Xiaomihu:a123456!@#@129.211.78.19/Xiaomihu'
# 这个配置将来会被禁用,设置为True或者False可以解除警告信息,建议设置False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class BlogType(db.Model):
    # 博客类型表,与博客表存在主外键关系
    # id 类型名称 添加时间
    __tablename__ = 'BlogType'
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    typeName = db.Column(db.String(64),nullable=False,unique=True)
    addTime = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    def __repr__(self):
        return '<id %r>' % (self.id)
#

class Blog(db.Model):
    # id 类型id 阅读量 标题 内容 添加时间
    __tablename__ = 'Blog'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    typeId = db.Column(db.Integer,db.ForeignKey('BlogType.id'),nullable=False,default=1)
    reading = db.Column(db.Integer(), nullable=False,default=0)
    title = db.Column(db.String(200), nullable=False, unique=True)
    img64base = db.Column(db.Text(), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    addTime = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    def __repr__(self):
        return '<id %r>' % (self.id)

class BlogComments(db.Model):
    # id 博客id 邮箱 名称 ip  内容 添加时间
    __tablename__ = 'BlogComments'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    blogId = db.Integer,db.ForeignKey('Blog.id')
    email = db.Column(db.String(64), nullable=False, unique=True)
    name = db.Column(db.String(64), nullable=False)
    ip = db.Column(db.String(64), nullable=False)
    content = db.Column(db.String(400), nullable=False)
    addTime = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    def __repr__(self):
        return '<id %r>' % (self.id)
#
class Photo(db.Model):
    # id 图片 添加时间
    __tablename__ = 'Photo'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    imgData = db.Column(db.Text(), nullable=False)
    addTime = db.Column(db.DateTime(), nullable=False, default=datetime.now())

    def __repr__(self):
        return '<id %r>' % (self.id)

if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    #  添加分类
    # db.session.add(BlogType(typeName='测试分类'))
    # db.session.commit()

    #
    pass
