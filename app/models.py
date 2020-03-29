from . import db
from werkzeug.security import                                                                generate_password_hash
from flask_login._compat import unicode
from datetime import date 



class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(6))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    bio = db.Column(db.String(150))
    photo = db.Column(db.String(120))
    date_created = db.Column(db.Date())



    def __init__(self, first_name, last_name,gender, location, email, bio, photo):
        self.first_name = first_name
        self.last_name = last_name
        # self.username = username
        self.gender = gender
        self.email = email 
        self.location = location
        self.photo = photo
        self.bio = bio 
        self.date_created = date.today()
        
        # self.password = generate_password_hash(
        #     password, method='pbkdf2:sha256')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
