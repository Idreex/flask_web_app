from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user


auth = Blueprint('auth', __name__)


# password = request.form.get('password')
# # converting password to array of bytes 
# bytes = password.encode('utf-8') 
# # generating the salt 
# salt = bcrypt.gensalt(rounds=15) 
# # Hashing the password 
# hashed_password = bcrypt.hashpw(bytes, salt)
# # encoding user password 
# userBytes = password.encode('utf-8') 


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            # if check_password_hash(user.password, password):
            # flash('User successfully logged in', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home')) 
            # else: 
            #     flash('Incorrect username or password, try again', category='error')
        else:
            flash('User not exist, try sign up', category='error')
            
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('FirstName')
        password1 = request.form.get('Password1')
        password2 = request.form.get('Password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exist!', category='error')
        elif len(email) < 2:
            flash("Email must greater than 2 characters or more",category='error')
        elif len(password1) < 2:
            flash("Email must up to 3 characters or more",category='error')
        elif password1 != password2:
            flash("password does not match ",category='error')
        else:
           new_user = User(email = email, firstname = firstName, password = generate_password_hash(password1, method='sha256'))
           db.session.add(new_user)
           db.session.commit()
           flash("Account created successfully",category='success') 
           login_user(new_user, remember=True)
           return redirect(url_for('views.home'))
    
    return render_template('sign-up.html')

