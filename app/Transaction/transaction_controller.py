from flask import render_template, current_app, url_for, jsonify,request,redirect
from models.models import UserModel
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from sqlalchemy import extract

def home():
    transactions =  list(UserModel().get_transactions({"user_id": ObjectId(request.cookies.get('user_id'))}))
    accounts = list(UserModel().get_account({"user_id": ObjectId(request.cookies.get('user_id'))}))
    categories = list(UserModel().get_jars({"user_id": ObjectId(request.cookies.get('user_id'))}))
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

def add_transaction():
    if request.method == 'POST':
        data = request.form
        new_transaction = {
            "user_id": ObjectId(request.cookies.get('user_id')),
            "date": datetime.strptime(data.get('date'), '%Y-%m-%d'),
            "type": data.get('type'),
            "account": data.get('account'),
            "category": data.get('category'),
            "description": data.get('description'),
            "amount": float(data.get('amount'))
        }
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
            "date": datetime.strptime(data.get('date'), '%Y-%m-%d'),
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
        # Lấy thông tin giao dịch để hiển thị trong form
        transaction = UserModel().get_transactions({"_id": ObjectId(transaction_id)}).next()
        return render_template('editTransaction.html', transaction=transaction)

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



def get_filtered_transactions():
    # Các tham số lọc từ request
    account = request.args.get('account', 'all')
    time = request.args.get('time', 'all')
    transaction_type = request.args.get('type', 'all')

    transactions = {}
    # Lọc theo tài khoản
    if account != 'all':
        transactions = [t for t in transactions if t['account'] == account]

    # Lọc theo thời gian
    if time != 'all':
        today = datetime.now().date()
        if time == 'today':
            transactions = [t for t in transactions if datetime.strptime(t['date'], '%Y-%m-%d').date() == today]
        elif time == 'week':
            start_week = today - timedelta(days=today.weekday())
            transactions = [t for t in transactions if datetime.strptime(t['date'], '%Y-%m-%d').date() >= start_week]
        elif time == 'month':
            transactions = [t for t in transactions if datetime.strptime(t['date'], '%Y-%m-%d').date().month == today.month]

    # Lọc theo loại giao dịch
    if transaction_type != 'all':
        transactions = [t for t in transactions if t['transaction_type'] == transaction_type]

    # Trả kết quả
    return render_template('transaction.html')

# def get_filtered_transactions():
#     filters = {}

#     # Lấy các tham số từ request
#     time_filter = request.args.get('time')  # "today", "this_week", "this_month"
#     transaction_type = request.args.get('type')  # "income", "expense", "transfer"
#     account = request.args.get('account')  # Tên tài khoản hoặc "all"

#     # Xử lý lọc theo thời gian
#     if time_filter == "today":
#         start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
#         end_date = datetime.now()
#         filters["date"] = {"$gte": start_date, "$lte": end_date}
#     elif time_filter == "week":
#         start_date = datetime.now() - timedelta(days=datetime.now().weekday())
#         start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
#         end_date = datetime.now()
#         filters["date"] = {"$gte": start_date, "$lte": end_date}
#     elif time_filter == "month":
#         start_date = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
#         end_date = datetime.now()
#         filters["date"] = {"$gte": start_date, "$lte": end_date}

#     # Lọc theo loại giao dịch
#     if transaction_type and transaction_type != "all":
#         filters["type"] = transaction_type

#     # Lọc theo tài khoản
#     if account and account != "all":
#         filters["account"] = account

    
#     # Lấy dữ liệu từ database 
#     transactions = list(UserModel().mongo.db.transactions.find(filters))
#     return jsonify(transactions)  # Trả về JSON
