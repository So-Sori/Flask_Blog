from datetime import datetime
from flaskblog import db,login_manager
from flask_login import UserMixin


#Login buscando por id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Lo bueno de trabajar bases de datos con sqlalchemy es que te permite trabajar las tablas como clases
class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key  = True)
    user_name = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(20), nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    posts = db.relationship('Post', backref = 'author', lazy = True)

    def __repr__(self):
        return f' User ({self.user_name},{self.email},{self.image_file})'

class Post(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    title = db.Column(db.String(100), nullable = False)
    date_post = db.Column(db.DateTime,nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f' Post ({self.title},{self.date_post})'
