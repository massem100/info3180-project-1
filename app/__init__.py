from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "RABBITSFLYBIRDS SING"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres: // gtdxgzynorfyfb: eb9e877586aefb23db0561c7ef59c060569f84bab6ca5940c015bc80f94e6971@ec2-54-152-175-141.compute-1.amazonaws.com: 5432/d4ein5o6rtssfg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning


db = SQLAlchemy(app)
UPLOAD_FOLDER = './app/static/uploads'
# Flask_Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
