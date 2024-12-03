from flask import render_template, current_app, url_for
from flask import jsonify
from models.models import UserModel
from datetime import datetime

def home():
    user = UserModel()
    accounts = list(user.get_account())
    transactions = list(user.get_transactions())
    bank_accounts = [account for account in accounts if account["type"] == "bank"]
    ewallet_accounts = [account for account in accounts if account["type"] == "ewallet"]
    cash_accounts = [account for account in accounts if account["type"] == "cash"]
    transactions_recently = sorted(
        transactions, 
        key=lambda x: x['date'],#datetime.strptime(x["date"], "%d/%m/%Y"), 
        reverse=True
    )

    description_transaction1 = transactions_recently[0]['category']+' / '+transactions_recently[0]['description']
    date_transaction1 = transactions_recently[0]['date']
    amount_transaction1 = transactions_recently[0]['amount']
    description_transaction2 = transactions_recently[1]['category']+' / '+transactions_recently[1]['description']
    date_transaction2 = transactions_recently[1]['date']
    amount_transaction2 = transactions_recently[1]['amount']

    total_balance_bank = sum(account["balance"] for account in bank_accounts)
    total_balance_ewallet = sum(account["balance"] for account in ewallet_accounts)
    total_balance_cash = sum(account["balance"] for account in cash_accounts)
    total_amount = total_balance_bank+total_balance_ewallet+total_balance_cash
    return render_template('dashboard.html',
                            total_amount=total_amount,
                           total_balance_bank=total_balance_bank,
                           total_balance_ewallet=total_balance_ewallet,
                           total_balance_cash=total_balance_cash,
                            description_transaction1 = description_transaction1,
                            date_transaction1 = date_transaction1,
                            amount_transaction1 = amount_transaction1,
                            description_transaction2 = description_transaction2,
                            date_transaction2 = date_transaction2,
                            amount_transaction2 = amount_transaction2
                           )

    
