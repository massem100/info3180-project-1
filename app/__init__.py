from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "RABBITSFLYBIRDS SING"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://znhmyqggjhvgxu:c599c02ecfb0f74edb722319dd1be537c0b795ed5e8b9ba7a4c7d11e15c87a3e@ec2-52-87-58-157.compute-1.amazonaws.com:5432/d2fdqrtu7g88gk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning


db = SQLAlchemy(app)
UPLOAD_FOLDER = './app/static/uploads'
# Flask_Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
