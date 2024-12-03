from flask import render_template, current_app, url_for, send_file, request, redirect
from models.models import UserModel
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import io

def home():
    id1 = request.args.get('1')
    id2 = request.args.get('2')
    id3 = request.args.get('3')
    id4 = request.args.get('4')
    id5 = request.args.get('5')
    id6 = request.args.get('6')
    if id1:
        UserModel().create_jar({"idJar": 1, "name": "Jar 1", "balance": 0, "category": id1}) 
    if id2:
        UserModel().create_jar({"idJar": 2, "name": "Jar 2", "balance": 0, "category": id2})
    if id3:
        UserModel().create_jar({"idJar": 3, "name": "Jar 3", "balance": 0, "category": id3})
    if id4:
        UserModel().create_jar({"idJar": 4, "name": "Jar 4", "balance": 0, "category": id4})
    if id5:
        UserModel().create_jar({"idJar": 5, "name": "Jar 5", "balance": 0, "category": id5})
    if id6:
        UserModel().create_jar({"idJar": 6, "name": "Jar 6", "balance": 0, "category": id6})


    jar_model = UserModel()
    jars = list(jar_model.get_jars())
     
    
    return render_template('jar.html', categories=jars, reset=" ")

def delete(id):
    jar_model = UserModel()
    jar_id = int(id)
    if id:
        jar_model.delete_jar(jar_id)
    return redirect(url_for('jar.jar_route'))
