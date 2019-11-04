# -*- coding: utf-8 -*-
# 留言板view


from __init__ import app
from model import db
from flask import Blueprint
message = Blueprint('message',__name__)