from flask import Flask
from flask_wtf.csrf import CsrfProtect
import os
app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = os.urandom(24)
app.secret_key = os.urandom(24)
# csrf protection
csrf = CsrfProtect()
csrf.init_app(app)



from blog import blog
from photo import photo
app.register_blueprint(blog,url_prefix='/blog')
app.register_blueprint(photo,url_prefix='/photo')


