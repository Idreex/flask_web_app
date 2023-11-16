from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from os import path
from flask_login import LoginManager
# import bcrypt

db = SQLAlchemy()

DB_NAME = 'database.db'

# def valid(password):
#     # converting password to array of bytes 
#     bytes = password.encode('utf-8') 
#     # generating the salt 
#     salt = bcrypt.gensalt(rounds=15) 
#     # Hashing the password 
#     hashed_password = bcrypt.hashpw(bytes, salt)
#     # encoding user password 
#     userBytes = password.encode('utf-8') 
#     # checking password 
#     is_valid = bcrypt.checkpw(userBytes, hashed_password) 
#     return is_valid

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bola123'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    from .models import User, Note
    
    app.register_blueprint(views, url_prefix='/') 
    app.register_blueprint(auth, url_prefix='/')
    
    with app.app_context():
        if not path.exists('website/' + DB_NAME):
            db.create_all()
            print('Database Created!')
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) 
    return app




