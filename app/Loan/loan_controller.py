from flask import render_template, current_app, url_for, redirect, request
from flask import jsonify
from datetime import datetime
from models.models import UserModel
from bson.objectid import ObjectId

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

def add_loan():
    loan_model = UserModel()
    data = request.form.to_dict()
    data['amount'] = int(data['amount'])
    data['createTime'] = datetime.now() # thời gian tạo 
    print(data)
    loan_model.create_loan(data)
    return redirect(url_for('loan.loan_route'))


def edit_loan():
    id = request.form.get('id')  # Lấy id từ form
    if not id:
        return redirect(url_for('loan.loan_route'))

    data = request.form.to_dict()  # Lấy dữ liệu cập nhật từ form
    loan_model = UserModel()


    idLoan = {"_id": ObjectId(id)}
    loan_model.update_loan(idLoan)  # Gọi phương thức update_loan
    return redirect(url_for('loan.loan_route'))



def edit_lending(id):
    loan_model = UserModel()
    idLending = {"_id": ObjectId(id)}
    lendings = list(loan_model.get_lendings(idLending))
    lending = [lending for lending in lendings if lending['_id'] == ObjectId(id)][0]
    # lending = {
    #     "id": 1,
    #     "type": "Cho vay",
    #     "lender": "Nguyễn Văn D",
    #     "amount": 10000000,
    #     "interest_rate": 10,
    #     "interest_type": "simple",
    #     "loan_date": "2024-03-01",
            # "due_date": "2024-09-01",
            # "contact": "0912345678",
    #     "paid": 999000000,
    #     "interest": 1250000,
    #     "remaining": 31250000,
    #     "progress": 40,
    #     "description": "Ghi chú về khoản vay"
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
    lending = [lending for lending in lendings if lending['id'] == id][0]
    return render_template('editLend.html', lend=lending)
