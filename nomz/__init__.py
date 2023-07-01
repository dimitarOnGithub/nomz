import os
import json
import logging.config

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
mail = Mail()

app = Flask(__name__)
conf_path = os.environ.get("APP_CONFIG_PATH")
if not conf_path:
    raise ValueError("No 'APP_CONFIG_PATH' environmental value defined to use as configuration file.")
app.config.from_file(conf_path, load=json.load)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
mail.init_app(app)

from nomz.home.routes import home
from nomz.auth.routes import auth

from nomz.auth.models.user import User
from nomz.home.models.category import Category

app.register_blueprint(home)
app.register_blueprint(auth)

