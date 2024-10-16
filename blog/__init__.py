from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app =Flask(__name__)
app.config['SECRET_KEY'] ='989f7fd5ec8ec4cbebd7d3e7613f93c4ex'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../blog.db'
db= SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view ='login'
login_manager.login_message='first loggin please'
login_manager.login_message_category='info'

from blog import routes



