from flask import render_template, current_app, url_for, jsonify

def home():
    # Example dynamic data
    transactions = [
        {
            "id": 1,
            "date": "20/03/2024",
            "type": "income",
            "account": "Vietcombank",
            "category": "Lương",
            "description": "Lương tháng 3",
            "amount": "15000000"
        },
        {
            "id": 2,
            "date": "19/03/2024",
            "type": "expense",
            "account": "Momo",
            "category": "Ăn uống",
            "description": "Ăn trưa",
            "amount": "50000"
        },
        {
            "id": 3,
            "date": "18/03/2024",
            "type": "transfer",
            "account": "Tiền mặt",
            "category": "Chuyển khoản",
            "description": "Chuyển khoản cho bạn",
            "amount": "100000"
        }
    ]

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
    return render_template('transaction.html',
                         transactions=transactions,
                         accounts=accounts,
                         total_balance=total_balance,
                         bank_accounts=bank_accounts,
                         ewallet_accounts=ewallet_accounts,
                         cash_accounts=cash_accounts)

def edit_transaction(transaction_id):
    transactions = [
        {
            "id": 1,
            "date": "20/03/2024",
            "type": "income",
            "account": "Vietcombank",
            "category": "Lương",
            "description": "Lương tháng 3",
            "amount": "15000000"
        },
        {
            "id": 2,
            "date": "19/03/2024",
            "type": "expense",
            "account": "Momo",
            "category": "Ăn uống",
            "description": "Ăn trưa",
            "amount": "50000"
        },
        {
            "id": 3,
            "date": "18/03/2024",
            "type": "transfer",
            "account": "Tiền mặt",
            "category": "Chuyển khoản",
            "description": "Chuyển khoản cho bạn",
            "amount": "100000"
        }
    ]
    transaction = next((t for t in transactions if t["id"] == transaction_id), None)
    return render_template('editTransaction.html', transaction=transaction)