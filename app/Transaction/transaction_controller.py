from flask import render_template, current_app, url_for, jsonify,request,redirect
from models.models import UserModel
from bson.objectid import ObjectId
from datetime import datetime
def home():

    transactions =  list(UserModel().get_transactions({"user_id": ObjectId(request.cookies.get('user_id'))}))
    accounts = list(UserModel().get_account({"user_id": ObjectId(request.cookies.get('user_id'))}))
    categories = list(UserModel().get_jars({"user_id": ObjectId(request.cookies.get('user_id'))}))
    # Example dynamic data
    if request.args.get('type') == "income":
            transactions = [transaction for transaction in transactions if transaction["type"] == "income"]
    elif request.args.get('type') == "expense":
            transactions = [transaction for transaction in transactions if transaction["type"] == "expense"]
    elif request.args.get('type') == "transfer":
            transactions = [transaction for transaction in transactions if transaction["type"] == "transfer"]
    else:
        transactions = transactions
    if request.args.get('account'):
        transactions = [transaction for transaction in transactions if transaction["account"] == request.args.get('account')]
    else:
        transactions = transactions
   
        
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

def add_transaction():
    if request.method == 'POST':
        data = request.form
        new_transaction = {
            "user_id": ObjectId(request.cookies.get('user_id')),
            "date": datetime.now().replace(microsecond=0),
            "type": data.get('type'),
            "account": data.get('account'),
            "category": data.get('category'),
            "description": data.get('description'),
            "amount": float(data.get('amount'))
        }
        account = list(UserModel().get_account({"name": (data.get('account')),"user_id": ObjectId(request.cookies.get('user_id'))}))
        account = account[0]
        if data.get('type') == "income":
            account["balance"] += float(data.get('amount'))
        else:
            account["balance"] -= float(data.get('amount'))
        UserModel().update_account(account["_id"], account)
        if data.get('type') == "expense":
            jar = list(UserModel().get_jars({"category": data.get('category'), "user_id": ObjectId(request.cookies.get('user_id'))}))
            jar = jar[0]
            idJar = jar["idJar"]
            name = jar["name"]
            deduct_money = {
                "user_id": ObjectId(request.cookies.get('user_id')),
                "idJar": idJar,
                "category": data.get('category'),
                "balance": float(data.get('amount'))*-1,
                "name": name,
                "type": "expense"
            }
            UserModel().create_jar(deduct_money)
        UserModel().create_transaction(new_transaction)  # Giả sử bạn có hàm này trong model
        return redirect(url_for('transaction.transaction_route'))  # Quay lại trang chính sau khi thêm
    
def edit_transaction(transaction_id):
    if request.method == 'POST':
        data = request.form
        updated_transaction = {
            "date": datetime.now().replace(microsecond=0),
            "type": data.get('type'),
            "account": data.get('account'),
            "category": data.get('category'),
            "description": data.get('description'),
            "amount": float(data.get('amount')),
        }
        # Cập nhật giao dịch trong cơ sở dữ liệu
        UserModel().update_transaction(ObjectId(transaction_id), updated_transaction)
        return redirect(url_for('transaction.transaction_route'))  # Quay lại trang giao dịch
    else:
        categories = list(UserModel().get_jars({"user_id": ObjectId(request.cookies.get('user_id'))}))
        transaction = UserModel().get_transactions({"_id": ObjectId(transaction_id)}).next()
        return render_template('editTransaction.html', transaction=transaction, categories=categories)

def delete_transaction(transaction_id):
    try:
        # Chuyển đổi id từ chuỗi thành ObjectId
        transaction_id = ObjectId(transaction_id)
        
        # Kiểm tra giao dịch tồn tại
        transaction = UserModel().mongo.db.transaction.find_one({"_id": transaction_id})
        
        if transaction:
            # Thực hiện xóa
            result = UserModel().mongo.db.transaction.delete_one({"_id": transaction_id})
            if result.deleted_count > 0:
                print(f"Transaction with id {transaction_id} was successfully deleted.")
            else:
                print(f"Failed to delete transaction with id {transaction_id}.")
        else:
            print(f"Transaction with id {transaction_id} does not exist.")
    except Exception as e:
        print(f"Error during deletion: {e}")

    return redirect(url_for('transaction.transaction_route'))  # Quay lại trang giao dịch
