from flask import render_template, current_app, url_for, jsonify,request,redirect
from flask import jsonify
from models.models import UserModel
from bson.objectid import ObjectId
from datetime import datetime

def home():
    user = UserModel()
    accounts = list(user.get_account({"user_id": ObjectId(request.cookies.get('user_id'))}))
    transactions = list(user.get_transactions({"user_id": ObjectId(request.cookies.get('user_id'))}).sort("date", -1).limit(3))
    # Many Accounts
    bank_accounts = [account for account in accounts if account["type"] == "bank"]
    ewallet_accounts = [account for account in accounts if account["type"] == "ewallet"]
    cash_accounts = [account for account in accounts if account["type"] == "cash"]
    # ---------------------
    print(transactions)
    total_balance_bank = sum(account["balance"] for account in bank_accounts)
    total_balance_ewallet = sum(account["balance"] for account in ewallet_accounts)
    total_balance_cash = sum(account["balance"] for account in cash_accounts)
    total_amount = total_balance_bank+total_balance_ewallet+total_balance_cash
    user = (UserModel().get_auth({"_id": ObjectId(request.cookies.get('user_id'))}))
    name = user['name']
    return render_template('dashboard.html',
                            total_amount=total_amount,
                           total_balance_bank=total_balance_bank,
                           total_balance_ewallet=total_balance_ewallet,
                           total_balance_cash=total_balance_cash,
                            transactions=transactions,
                            name=name
                           )

    
    
    
    
