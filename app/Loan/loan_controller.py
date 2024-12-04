from flask import render_template, current_app, url_for, redirect, request
from flask import jsonify
from datetime import datetime
from models.models import UserModel
from bson.objectid import ObjectId
from helper.TopLoan import get_loan_due_dates,compare_loan_debt,compare_lend_debt,caculator_interest,updated_interest_Loan
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
    #         "interestType": "simple",
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
    account = list(UserModel().get_account())

    total_loan = sum(float(loan['amount']) for loan in loans)
    total_lending = sum(float(lending['amount']) for lending in lendings)

    due_date = get_loan_due_dates(loans)
    amount_due = float(due_date['amount_due'])
    day_left = due_date['days_left']
    compare_loan = compare_loan_debt(loans)
    compare_lend = compare_lend_debt(lendings)
    
    return render_template('loan.html',
                           loans=loans,
                           lendings=lendings,
                           total_loan=total_loan,
                           total_lending=total_lending,
                           accounts=account,
                           amount_due = amount_due,
                           day_left = day_left,
                           compareloan=compare_loan,
                           comparelend=compare_lend
                           )

def add_loan():
    loan_model = UserModel()
    data = request.form.to_dict()
    data['paid'] = 0
    data['createTime'] = datetime.now() # thời gian tạo 
    principal = float(data['amount'])
    interest = caculator_interest(data)
    data['interest'] = interest    
    total_due = principal + interest
    data['remaining'] = total_due
    data["progress"] = (data['paid']/total_due)* 100  # Tính tỷ lệ tiến độ thanh toán (%)
    loan_model.create_loan(data)
    return redirect(url_for('loan.loan_route'))


def edit_loan(id):
    loan_model = UserModel()
    idLoan = {"_id": ObjectId(id)}
    loans = list(loan_model.get_loans(idLoan))
    
    loan = [loan for loan in loans if loan['_id'] == ObjectId(id)][0]
    return render_template('editLoan.html', loan=loan)

def delete_loan(id):
    loan_model = UserModel()
    loan_id = ObjectId(id)
    if id:
        loan_model.delete_loan(loan_id)
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
    return render_template('editLend.html', lend=lending)

def payment_loan(id):
    loan_model = UserModel()
    idLoan = {"_id": ObjectId(id)}
    account = UserModel().get_account()
    loans = list(loan_model.get_loans(idLoan))
    loan = [loan for loan in loans if loan['_id'] == ObjectId(id)][0]
    return render_template('paymentLoan.html', loan=loan, accounts=account)

def payment_loan_post(id):
    loan_model = UserModel()  # Khởi tạo đối tượng model của khoản vay
    data = request.form.to_dict()  # Lấy dữ liệu từ form gửi lên (dưới dạng dictionary)

    # Lấy thông tin khoản vay từ database dựa trên ID
    loan = list(loan_model.get_loans({"_id": ObjectId(id)}))

    if loan:
        loan = loan[0] 
        updated_loan = updated_interest_Loan(loan,data)
        # Cập nhật thông tin khoản vay vào database
    loan_model.update_loan(ObjectId(id), updated_loan)

    # Chuyển hướng về trang danh sách khoản vay
    return redirect(url_for('loan.loan_route'))



def edit_loan_post(id):
    loan_model = UserModel()
    data = request.form.to_dict()
    loan = list(loan_model.get_loans({"_id": ObjectId(id)}))
    loan = loan[0]
    data['paid'] = loan['paid']
    data['createTime'] = datetime.now() # thời gian tạo 
    interest =  caculator_interest(data)
    data['interest'] = interest
    total_due = (float(data['amount'])- data['paid'] ) + interest
    data['remaining'] = total_due
    data["progress"] = (data['paid']/float(data['amount']))* 100  # Tính tỷ lệ tiến độ thanh toán (%)
    loan_model.update_loan(ObjectId(id), data)
    return redirect(url_for('loan.loan_route'))

def add_lend():
    lend_model = UserModel()
    data = request.form.to_dict()
    data['paid'] = 0
    data['createTime'] = datetime.now() # thời gian tạo 
    principal = float(data['amount'])
    interest = caculator_interest(data)
    data['interest'] = interest    
    total_due = principal + interest
    data['remaining'] = total_due
    data["progress"] = (data['paid']/total_due)* 100  # Tính tỷ lệ tiến độ thanh toán (%)
    lend_model.create_lending(data)
    return redirect(url_for('loan.loan_route'))

def edit_lend_post(id):
    lend_model = UserModel()
    data = request.form.to_dict()
    lend = list(lend_model.get_lendings({"_id": ObjectId(id)}))
    lend = lend[0]
    data['paid'] = lend['paid']
    data['createTime'] = datetime.now() # thời gian tạo 
    interest =  caculator_interest(data)
    data['interest'] = interest
    total_due = (float(data['amount'])- data['paid'] ) + interest
    data['remaining'] = total_due
    data["progress"] = (data['paid']/float(data['amount']))* 100  # Tính tỷ lệ tiến độ thanh toán (%)
    lend_model.update_lending(ObjectId(id), data)
    return redirect(url_for('loan.loan_route'))
def delete_lend(id):
    lend_model = UserModel()
    lend_id = ObjectId(id)
    if id:
        lend_model.delete_lending(lend_id)
    return redirect(url_for('loan.loan_route'))
