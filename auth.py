from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('signup')
def signup():
    return "This page will be used as signup"

@auth.route('/login')
def login():
    return "This page will be login"

@auth.route('/logout')
def logout():
    return "Use this to log out"
