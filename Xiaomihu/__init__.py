from flask import Flask

app = Flask(__name__)
app.debug = True

from blog import blog
from photo import photo
app.register_blueprint(blog,url_prefix='/blog')
app.register_blueprint(photo,url_prefix='/photo')

