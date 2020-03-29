"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, session, abort
from flask_login import login_user, logout_user, current_user, login_required
from app.form import ProfileForm
from app.models import UserProfile
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy



###
# Routing for your application.
###
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route('/profiles', methods= ['POST','GET'])
def profiles(): 
    form = ProfileForm()
    # if request.method == "POST" and form.validate():
    #     if form.validate_on_submit():

    return render_template('profiles.html', form = form)

# def get_profile_images():
#     lst = []
#     rootdir = os.getcwd()
#     # print rootdir
#     for subdir, dirs, files in os.walk(rootdir + '/app/static/uploads'):
#         for file in files:
#             lst.append(file)
#     return lst

#     return render_template('profiles.html')


@app.route('/profile', methods = ['POST','GET'])
def addProfile():
    profileform = ProfileForm()
    if request.method == "POST" and profileform.validate():
        if profileform.validate_on_submit():
            first_name = profileform.first_name.data
            last_name = profileform.last_name.data
            gender = profileform.gender.data
            email = profileform.email.data
            location = profileform.location.data
            bio = profileform.bio.data
            photo = profileform.photo.data
            
            filename = secure_filename(photo.filename)
            # photo.save(os.path.join(app.config))
            return redirect(url_for('home'))
    else: 
        return render_template('addProfile.html', form = profileform)

    if request.method =="GET":
        return render_template('addProfile.html')


@app.route('/profile/<userid>')
def profile(userid): 
    userid= "Mary"
    return render_template('profile.html', userid = userid)

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session

@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
 
