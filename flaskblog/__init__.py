from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd3a3eb9eaa2309249b50ea8357ed0708819bba72'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../flaskblog/site.db'
app.app_context().push()
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from flaskblog import routes
# import flaskblog.routes