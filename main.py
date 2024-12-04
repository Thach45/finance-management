from dotenv import load_dotenv
from flask import render_template, request, redirect, url_for
import os
from models.models import UserModel

# from models.user import User

from flask_pymongo import PyMongo
from flask import Flask
from app.Dashboard import dashboard_bp
from app.Account import account_bp
from app.Jar import jar_bp
from app.Transaction import transaction_bp
from app.Report import report_bp
from app.Loan import loan_bp
from app.Auth import auth_bp
load_dotenv()
app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)
app.config['MONGO'] = mongo
app.register_blueprint(dashboard_bp)

app.register_blueprint(account_bp)

app.register_blueprint(transaction_bp)
app.register_blueprint(loan_bp)
app.register_blueprint(report_bp)
app.register_blueprint(jar_bp)
app.register_blueprint(auth_bp)
@app.before_request
def check_token():
    # Bỏ qua kiểm tra cho các route không cần xác thực
    if request.endpoint in ["auth.login_route", "auth.register_route", "auth.register_post_route", "auth.auth_route"]:
        return

    token = request.cookies.get('token')
    if not token:
        return render_template("auth.html", error="Token không hợp lệ")

    if not UserModel().get_auth({"token": token}):
        return render_template("auth.html", error="Token không hợp lệ")
    
    # #phan chinh sua
    # if not User().get_auth({"token": token}):
    #     return render_template("auth.html", error="Token không hợp lệ")

if __name__ == '__main__':
    app.run(debug=True, port=8000)