from flask import Flask

app = Flask(__name__)
app.debug = True

from blog import blog
app.register_blueprint(blog,url_prefix='/blog')

