from flask import render_template, current_app, url_for
from flask import jsonify

def home():

    accounts = [
        {"name": "Vietcombank", "type": "bank", "balance": 1},
        {"name": "SeABank", "type": "bank", "balance": 2},
        {"name": "TPBank", "type": "bank", "balance": 3},
        {"name": "BIDV", "type": "bank", "balance": 5},
        {"name": "ZaloPay", "type": "ewallet", "balance": 1},
        {"name": "VNPay", "type": "ewallet", "balance": 2},
        {"name": "Tiền mặt", "type": "cash", "balance": 10}
    ]
    bank_accounts = [account for account in accounts if account["type"] == "bank"]
    ewallet_accounts = [account for account in accounts if account["type"] == "ewallet"]
    cash_accounts = [account for account in accounts if account["type"] == "cash"]


    total_balance = sum(account["balance"] for account in bank_accounts) + sum(account["balance"] for account in ewallet_accounts) + sum(account["balance"] for account in cash_accounts)
    return render_template('account.html',
                         bank_accounts=bank_accounts,
                         ewallet_accounts=ewallet_accounts,
                         cash_accounts=cash_accounts,
                         total_balance=total_balance,
                         accounts=accounts)
