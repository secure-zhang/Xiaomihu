# -*- coding: utf-8 -*-
# 留言板view


from __init__ import app
from model import db
from form import MessageForm
from flask import Blueprint,render_template,request,redirect,url_for
from model import Message
import requests
import json
import datetime
message = Blueprint('message',__name__)

# 留言展示页面
@app.route('/message',methods=['GET','POST'])
def messageIndex():
    ip = request.remote_addr
    addr = get_addr(ip)
    form = MessageForm()
    page = 1
    messageItems = db.session.query(Message).order_by(Message.addTime.desc()).paginate(int(page), per_page=6, error_out=False)

    if form.validate_on_submit():
        addTime = datetime.datetime.now()
        name = form.data['name']
        email = form.data['email']
        content = form.data['content']
        messageData = Message(name=name, email=email, ip=ip, addr=addr, content=content,addTime=addTime)
        db.session.add(messageData)
        db.session.commit()
        return redirect(url_for('messageIndex'))
    return render_template('new_message.html',addr=addr,form=form,messageItems=messageItems)

# 通过ip获取位置
def get_addr(ip):
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s'%ip
    res = requests.get(url)
    if res.status_code:
        item = json.loads(res.content.decode('utf-8'))
        addr = item['data'].get('region','')
        return addr
    return '地球'