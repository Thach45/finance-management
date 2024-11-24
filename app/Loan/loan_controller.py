from flask import render_template, current_app, url_for
from flask import jsonify
from models.models import UserModel
def home():
    # Dữ liệu trong database
    # loans = [
    #     {
    #         "id": 1,
    #         "type": "Vay mua xe",
    #         "borrower": "Nguyễn Văn A",
    #         "status": "Chưa đến hạn",
    #         "amount": 50000000,
    #         "interest_rate": 5,
    #         "interest_type": "simple",
    #         "loan_date": "2024-03-01",
    #         "due_date": "2024-09-01",
    #         "contact": "0912345678",
    #         "paid": 20000000,
    #         "interest": 1250000,
    #         "description": "Ghi chú về khoản vay",
    #         "remaining": 31250000,
    #         "progress": 40
    #     },
    #     {
    #         "id": 2,
    #         "type": "Vay mua nhà",
    #         "borrower": "Nguyễn Văn B",
    #         "status": "Đã đến hạn",
    #         "amount": 100000000,
    #         "interest_rate": 7,
    #         "interest_type": "simple",
    #         "loan_date": "2024-03-01",
    #         "due_date": "2024-09-01",
    #         "description": "Ghi chú về khoản vay",
    #         "contact": "0912345678",
    #         "paid": 20000000,
    #         "interest": 1250000,
    #         "remaining": 31250000,
    #         "progress": 90
    #     },
    #     {
    #         "id": 3,
    #         "type": "Vay kinh doanh",
    #         "borrower": "Nguyễn Văn C",
    #         "status": "Chưa đến hạn",
    #         "amount": 20000000,
    #         "interest_rate": 10,
    #         "interest_type": "simple",
    #         "loan_date": "2024-03-01",
    #         "due_date": "2024-09-01",
    #         "description": "Ghi chú về khoản vay",
    #         "contact": "0912345678",
    #         "paid": 20000000,
    #         "interest": 1250000,
    #         "remaining": 31250000,
    #         "progress": 40
    #     }
    # ]
    # lendings = [
    #     {
    #         "id": 1,
    #         "type": "Cho vay",
    #         "lender": "Nguyễn Văn D",
    #         "amount": 10000000,
    #         "interest_rate": 10,
    #         "interest_type": "simple",
    #         "loan_date": "2024-03-01",
    #         "due_date": "2024-09-01",
    #         "contact": "0912345678",
    #         "paid": 999000000,
    #         "interest": 1250000,
    #         "remaining": 31250000,
    #         "progress": 40,
    #         "description": "Ghi chú về khoản vay"
    #     },
    #     {
    #         "id": 2,
    #         "type": "Cho vay",
    #         "lender": "Nguyễn Văn E",
    #         "amount": 20000000,
    #         "interest_rate": 10,
    #         "interest_type": "simple",
    #         "loan_date": "2024-03-01",
    #         "due_date": "2024-09-01",
    #         "contact": "0912345678",
    #         "paid": 20000000,
    #         "interest": 1250000,
    #         "remaining": 31250000,
    #         "progress": 40,
    #         "description": "Ghi chú về khoản vay"
    #     }
    # ]
    loan_model = UserModel()
    loans = list(loan_model.get_loans())
    lendings = list(loan_model.get_lendings())

    total_loan = sum(loan['amount'] for loan in loans)
    total_lending = sum(lending['amount'] for lending in lendings)
    return render_template('loan.html',
                           loans=loans,
                           lendings=lendings,
                           total_loan=total_loan,
                           total_lending=total_lending)

def edit_loan(id):
    loans = [
        {
            "id": 1,
            "type": "Vay mua xe",
            "borrower": "Nguyễn Văn A",
            "status": "Chưa đến hạn",
            "amount": 50000000,
            "interest_rate": 5,
            "interest_type": "simple",
            "loan_date": "2024-03-01",
            "due_date": "2024-09-01",
            "contact": "0912345678",
            "paid": 20000000,
            "interest": 1250000,
            "remaining": 31250000,
            "progress": 40,
            "description": "Ghi chú về khoản vay"
        },
        {
            "id": 2,
            "type": "Vay mua nhà",
            "borrower": "Nguyễn Văn B",
            "status": "Đã đến hạn",
            "amount": 100000000,
            "interest_rate": 7,
            "interest_type": "simple",
            "loan_date": "2024-03-01",
            "due_date": "2024-09-01",
            "contact": "0912345678",
            "paid": 20000000,
            "interest": 1250000,
            "remaining": 31250000,
            "progress": 90,
            "description": "Ghi chú về khoản vay"
        },
        {
            "id": 3,
            "type": "Vay kinh doanh",
            "borrower": "Nguyễn Văn C",
            "status": "Chưa đến hạn",
            "amount": 20000000,
            "interest_rate": 10,
            "interest_type": "simple",
            "loan_date": "2024-03-01",
            "due_date": "2024-09-01",
            "contact": "0912345678",
            "paid": 20000000,
            "interest": 1250000,
            "remaining": 31250000,
            "progress": 40,
            "description": "Ghi chú về khoản vay"
        }
    ]
    loan = [loan for loan in loans if loan['id'] == id][0]

    return render_template('editLoan.html', loan=loan)

def edit_lending(id):
    lendings = [
        {
            "id": 1,
            "type": "Cho vay",
            "lender": "Nguyễn Văn D",
            "amount": 10000000,
            "interest_rate": 10,
            "interest_type": "simple",
            "loan_date": "2024-03-01",
            "due_date": "2024-09-01",
            "contact": "0912345678",
            "paid": 999000000,
            "interest": 1250000,
            "remaining": 31250000,
            "progress": 40,
            "description": "Ghi chú về khoản vay"
        },
        {
            "id": 2,
            "type": "Cho vay",
            "lender": "Nguyễn Văn E",
            "amount": 20000000,
            "interest_rate": 10,
            "interest_type": "simple",
            "loan_date": "2024-03-01",
            "due_date": "2024-09-01",
            "contact": "0912345678",
            "paid": 20000000,
            "interest": 1250000,
            "remaining": 31250000,
            "progress": 40,
            "description": "Ghi chú về khoản vay"
        }
    ]
    lending = [lending for lending in lendings if lending['id'] == id][0]
    return render_template('editLend.html', lend=lending)
