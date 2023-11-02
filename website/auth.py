from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return '<h3>Login</h3>'

@auth.route('/logout')
def logout():
    return '<h3>Logout</h3>'

@auth.route('/sign-up')
def sign_up():
    return '<h3>sign-up</h3>'

