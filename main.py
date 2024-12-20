from dotenv import load_dotenv
from flask import render_template
import os
from models.models import UserModel
from flask_pymongo import PyMongo
from flask import Flask
from app.Dashboard import dashboard_bp
from app.Account import account_bp
from app.Transaction import transaction_bp
from app.Report import report_bp
from app.Loan import loan_bp
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
if __name__ == '__main__':
    app.run(debug=True, port=8000)