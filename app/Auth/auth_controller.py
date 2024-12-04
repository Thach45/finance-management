from flask import render_template, request, redirect, url_for
from datetime import datetime
from flask import make_response
from models.models import UserModel
from bson.objectid import ObjectId
import uuid as uuid
import hashlib

def home():
    return render_template('auth.html')

def login():
    auth_model = UserModel()
    auth = auth_model.get_auth({"phone": request.form["phone"],
                          "password": str(hashlib.sha256(request.form["password"].encode()).hexdigest())})
    if auth:
        response = make_response(redirect(url_for("dashboard.dashboard_route")))
        response.set_cookie("token", auth["token"])
        response.set_cookie("user_id", str(auth["_id"]))
        return response
    return render_template('auth.html', error="Số điện thoại hoặc mật khẩu không đúng")

def register():
    return render_template('register.html')

def register_post():
    data = request.form.to_dict()
    data["createTime"] = str(datetime.now())
    data["token"] = str(uuid.uuid4())
    data["password"] = str(hashlib.sha256(data["password"].encode()).hexdigest())
    existing_auth = UserModel().get_auth({"phone": data["phone"]})
    if existing_auth:
        return render_template("register.html", error="Số điện thoại đã tồn tại")
    auth_model = UserModel()
    auth_model.create_auth(data)
    return redirect(url_for("auth.auth_route"))

def logout():
    response = make_response(redirect(url_for("auth.auth_route")))
    response.delete_cookie("token")
    return response