from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('log-out.html')

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('Password1')
        password2 = request.form.get('Password2')

        if len(email) < 4:
            flash("Email must greater than 3 characters or more",category='error')
        if len(password1) < 8:
            flash("Email must up to 8 characters or more",category='error')
        if password1 != password2:
            flash("password does not match ",category='error')
        else:
           flash("Account created successfully",category='success') 
    return render_template('sign-up.html')

