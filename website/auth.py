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
        firstName = request.form.get('FirstName')
        password1 = request.form.get('Password1')
        password2 = request.form.get('Password2')
    
   

        if len(email) < 2:
            flash("Email must greater than 2 characters or more",category='error')
        elif len(password1) < 3:
            flash("Email must up to 4 characters or more",category='error')
        elif password1 != password2:
            flash("password does not match ",category='error')
        else:
           flash("Account created successfully",category='success') 
    
    return render_template('sign-up.html')

