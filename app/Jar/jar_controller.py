from flask import render_template, current_app, url_for, send_file, request, redirect
from bson.objectid import ObjectId
from models.models import UserModel
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import io


def add_category():
    id1 = request.args.get('1')
    id2 = request.args.get('2')
    id3 = request.args.get('3')
    id4 = request.args.get('4')
    id5 = request.args.get('5')
    id6 = request.args.get('6')
    if id1:
        UserModel().create_jar({"idJar": 1, "name": "Jar 1", "balance": 0, "category": id1, "type":"expense", "user_id": ObjectId(request.cookies.get('user_id'))}) 
    if id2:
        UserModel().create_jar({"idJar": 2, "name": "Jar 2", "balance": 0, "category": id2, "type":"expense", "user_id": ObjectId(request.cookies.get('user_id'))})
    if id3:
        UserModel().create_jar({"idJar": 3, "name": "Jar 3", "balance": 0, "category": id3, "type":"expense", "user_id": ObjectId(request.cookies.get('user_id'))})
    if id4:
        UserModel().create_jar({"idJar": 4, "name": "Jar 4", "balance": 0, "category": id4, "type":"expense", "user_id": ObjectId(request.cookies.get('user_id'))})
    if id5:
        UserModel().create_jar({"idJar": 5, "name": "Jar 5", "balance": 0, "category": id5, "type":"expense", "user_id": ObjectId(request.cookies.get('user_id'))})
    if id6:
        UserModel().create_jar({"idJar": 6, "name": "Jar 6", "balance": 0, "category": id6, "type":"expense", "user_id": ObjectId(request.cookies.get('user_id'))})
    return redirect(url_for('jar.jar_route'))  

def home():
    total = (request.args.get('total')) 
    if total:
        total = float(total)
        UserModel().update_total({"total": total})
       
    else:
        total = 0
    total = (UserModel().get_total())
    if not total:
        total = 0
    else:
        total = total["total"]

    jar_model = UserModel()
    jars = list(jar_model.get_jars({"user_id": ObjectId(request.cookies.get('user_id'))}))
    jars = list({str(jar['category']): jar for jar in jars}.values())
    print(jars)
    jar1 = ([jar for jar in jars if jar["idJar"] == 1])
    sum1 = sum(jar["balance"] for jar in jar1)
    jar2 = [jar for jar in jars if jar["idJar"] == 2]
    sum2 = sum(jar["balance"] for jar in jar2)
    jar3 = [jar for jar in jars if jar["idJar"] == 3]
    sum3 = sum(jar["balance"] for jar in jar3)
    jar4 = [jar for jar in jars if jar["idJar"] == 4]
    sum4 = sum(jar["balance"] for jar in jar4)
    jar5 = [jar for jar in jars if jar["idJar"] == 5]
    sum5 = sum(jar["balance"] for jar in jar5)
    jar6 = [jar for jar in jars if jar["idJar"] == 6]
    sum6 = sum(jar["balance"] for jar in jar6)
    return render_template('jar.html', categories=jars,
                            jar1=sum1,
                            jar2=sum2,
                            jar3=sum3,
                            jar4=sum4,
                            jar5=sum5,
                            jar6=sum6,
                            total=total
                           )

def delete(id):
    jar_model = UserModel()
    jar_id = int(id)
    if id:
        jar_model.delete_jar(jar_id)
    return redirect(url_for('jar.jar_route'))
