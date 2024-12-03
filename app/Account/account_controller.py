from flask import flash, render_template, current_app, url_for, request, redirect
from flask import jsonify
from app import Account
from models.models import UserModel #from models.User import User
from datetime import datetime
from bson import ObjectId

def home():
    account_model = UserModel()
    accounts = list(account_model.get_account())
    # ví dụ trong database đuọc lưu như sau:
    # accounts = [
    #     {"name": "Vietcombank", "type": "bank", "balance": 1},
    #     {"name": "SeABank", "type": "bank", "balance": 2},
    #     {"name": "TPBank", "type": "bank", "balance": 3},
    #     {"name": "BIDV",  "type": "bank", "balance": 5},
    #     {"name": "ZaloPay", "type": "ewallet", "balance": 1},
    #     {"name": "VNPay", "type": "ewallet", "balance": 2},
    #     {"name": "Tiền mặt", "type": "cash", "balance": 10}
    # ]
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

def add_account():
    account_model = UserModel()
    data = request.form.to_dict()
    data['balance'] = int(data['balance'])
    data['createTime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    account_model.create_account(data)
    return redirect(url_for('account.account_route'))

def delete_account(id):
    account_model = UserModel()
    account_id = ObjectId(id)
    if id:
        account_model.delete_account(account_id)
    return redirect(url_for('account.account_route'))

def index_account(id):
    account_model = UserModel()
    account_id = {"_id": ObjectId(id)}
    accounts = list(account_model.get_account(account_id))
    account = [account for account in accounts if account['_id'] == ObjectId(id)][0]
    return render_template('editAccount.html',account=account)
   
def edit_account(id):
    account_model = UserModel()
    data = request.form.to_dict()
    data['balance'] = int(data['balance'])
    data['createTime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    account_model.update_account(ObjectId(id), data)
    return redirect(url_for('account.account_route')) 

def transfer_account():
    account_model = UserModel()
    source_account_id = request.form.get('sourceAccount')  
    target_account_id = request.form.get('targetAccount')
    amount = int(request.form.get('amount'))  
    note = request.form.get('note')  
   
    source_id = ObjectId(source_account_id)
    target_id = ObjectId(target_account_id)
    
    source_account = account_model.get_account({'_id': source_id})
    target_account = account_model.get_account({'_id': target_id})
    
    source_account = source_account[0]
    target_account = target_account[0]
    
    source_account['balance'] = int(source_account['balance'])    
    target_account['balance'] = int(target_account['balance'])
    
    source_account['balance'] -= amount
    target_account['balance'] += amount
    
    account_model.update_account(source_id,source_account)
    account_model.update_account(target_id,target_account)

    return redirect(url_for('account.account_route'))

def filter_account():
    account_model = UserModel()
    accounts = list(account_model.get_account())
        
    bank_accounts = [account for account in accounts if account["type"] == "bank"]
    ewallet_accounts = [account for account in accounts if account["type"] == "ewallet"]
    cash_accounts = [account for account in accounts if account["type"] == "cash"]
    total_balance = sum(account["balance"] for account in bank_accounts) + sum(account["balance"] for account in ewallet_accounts) + sum(account["balance"] for account in cash_accounts)
    
    account_type = request.args.get('type')
    if account_type:
        accounts = [account for account in accounts if account["type"] == account_type]
        
    return render_template('account.html',
                         bank_accounts=bank_accounts,
                         ewallet_accounts=ewallet_accounts,
                         cash_accounts=cash_accounts,
                         total_balance=total_balance,
                         accounts=accounts)