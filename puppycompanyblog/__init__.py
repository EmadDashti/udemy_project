import os
from flask import Flask
from puppycompanyblog.core.views import core
from puppycompanyblog.error_pages.handlers import error_pages
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
login_manager = LoginManager()

app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + \
    os.path.join(basedir, 'data.sqlite')

db = SQLAlchemy(app)
Migrate(app, db)


login_manager.init_app(app)
login_manager.login_view = 'login'


app.register_blueprint(core)
app.register_blueprint(error_pages)
