from flask import render_template, current_app, url_for, jsonify,request,redirect
from models.models import UserModel
from bson.objectid import ObjectId
from datetime import datetime
def home():
    # Example dynamic data
    # transactions = [
    #     {
    #         "id": 1,
    #         "date": "20/03/2024",
    #         "type": "income",
    #         "account": "Vietcombank",
    #         "category": "Lương",
    #         "description": "Lương tháng 3",
    #         "amount": "15000000"
    #     },
    #     {
    #         "id": 2,
    #         "date": "19/03/2024",
    #         "type": "expense",
    #         "account": "Momo",
    #         "category": "Ăn uống",
    #         "description": "Ăn trưa",
    #         "amount": "50000"
    #     },
    #     {
    #         "id": 3,
    #         "date": "18/03/2024",
    #         "type": "transfer",
    #         "account": "Tiền mặt",
    #         "category": "Chuyển khoản",
    #         "description": "Chuyển khoản cho bạn",
    #         "amount": "100000"
    #     }
    # ]
    transactions =  list(UserModel().get_transactions())
    accounts = list(UserModel().get_account())
    categories = list(UserModel().get_jars())
    # Example dynamic data
    bank_accounts = [account for account in accounts if account["type"] == "bank"]
    ewallet_accounts = [account for account in accounts if account["type"] == "ewallet"]
    cash_accounts = [account for account in accounts if account["type"] == "cash"]
    total_balance = sum(account["balance"] for account in bank_accounts) + sum(account["balance"] for account in ewallet_accounts) + sum(account["balance"] for account in cash_accounts)
    return render_template('transaction.html',
                         transactions=transactions,
                         accounts=accounts,
                         total_balance=total_balance,
                         bank_accounts=bank_accounts,
                         ewallet_accounts=ewallet_accounts,
                         cash_accounts=cash_accounts,
                         categories=categories
                         )

def edit_transaction(transaction_id):
    transactions = list(UserModel().get_transactions())
    transaction = ObjectId(transaction_id)
    transaction = next((t for t in transactions if t["_id"] == transaction), None)
    return render_template('editTransaction.html', transaction=transaction)

