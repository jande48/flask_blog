from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LogInForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

post= [
    {
        'author': 'Michael Scott',
        'title': 'Past and Future of the Paper Industry',
        'content': 'As you know, I am the district manager of Dunker Mifflin.',
        'date_posted': 'April 1, 1985'
    },
    {
        'author': 'Jim',
        'title': 'Why Working at Dunker Mifflin is terrible',
        'content': 'Michael scott is worst.',
        'date_posted': 'April 2, 1985'
    }

]

@app.route("/")
def home():
    return render_template('home.html',posts=post)

@app.route("/about")
def about():
    return render_template('about.html',title="The About Title")

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LogInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check your email and password','danger')
    return render_template('login.html', title='Log In', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

