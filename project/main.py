from flask import Blueprint, render_template,request
from flask_login import login_required, current_user
from . import db
from . import music
import flask
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/oop/')
def oop():
    p = request.args.get("file_name")
    music.abcd(p)
    return flask.redirect("/profile")
