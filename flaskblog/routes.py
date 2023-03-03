from flask import render_template,url_for,flash,redirect,request
from flaskblog import app,db,bcrypt
from flaskblog.forms import Registerform,Loginform
from flaskblog.models import User, Post
from flaskblog import login_manager
from flask_login import login_user, current_user,logout_user,login_required

posts = [
    {'autor':'Heidi Lua',
    'title':'First post',
    'content':'Soy un comentario perdido',
    'date':'June 8 1993'},

    {'autor':'Ani Lu',
    'title':'Second post',
    'content':'Soy un comentario perdido',
    'date':'June 8 2003'},

    {'autor':'Shu li',
    'title':'Third post',
    'content':'Soy un comentario perdido',
    'date':'December 28 2020'}
]

@app.route("/")
@app.route("/Flask_blog/home") #se puede crear varias ruta a la misma pagina
def home():
    return render_template('home.html', posts = posts, title= 'Posts')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Registerform()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(user_name=form.user_name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account create for {form.user_name.data}!", 'success')
        return redirect(url_for('login'))
    return render_template('register.html',title= 'Register', form=form)

@app.route("/login",methods = ['GET','POST'])
def login():
    form = Loginform()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        # flash("Welcome again!!!", 'success')
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            flash("Welcome Again!!!")
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect('next_page') if next_page else redirect(url_for('home'))
        else:
            flash("There's a problem please check your Email and password", 'danger')
    return render_template('login.html',title= 'Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html',title= 'Account')

