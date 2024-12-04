from flask import render_template, current_app, url_for
from flask import jsonify
from models.models import UserModel #from models.User import User

def home():
    
    return render_template('dashboard.html')