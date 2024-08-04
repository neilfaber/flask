from flask import Blueprint, render_template

main = Blueprint('main', __name__) #BLueprint is a way to organize your files and you can access them using bluprint function

@main.route('/')
def index():
    return "Hello, World!"

@main.route('/profile')
def profile():
    return "Profile Here!"