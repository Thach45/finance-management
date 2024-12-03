from flask import render_template, current_app, url_for, redirect, request
from flask import jsonify
from datetime import datetime
from models.models import UserModel
from bson.objectid import ObjectId

def home():
    
    loan_model = UserModel()
    loans = list(loan_model.get_loans())
    lendings = list(loan_model.get_lendings())
    account = list(UserModel().get_account())

    total_loan = sum(int(loan['amount']) for loan in loans)
    total_lending = sum(lending['amount'] for lending in lendings)
    return render_template('loan.html',
                           loans=loans,
                           lendings=lendings,
                           total_loan=total_loan,
                           total_lending=total_lending,
                           accounts=account
                           )

def add_loan():
    loan_model = UserModel()
    data = request.form.to_dict()
    data['paid'] = 0
    data['createTime'] = datetime.now() # thời gian tạo 
    data['amount'] = int(data['amount'])
    principal = int(data['amount'])  # Số tiền vay ban đầu
    interest_rate = float(data['interest_rate'])
    interest_type = data['interestType']
    due_date = datetime.strptime(data['due_date'], '%Y-%m-%d')  # Ngày đến hạn, chuyển đổi từ chuỗi thành datetime
    current_date = datetime.strptime(data['loan_date'], '%Y-%m-%d') 
    if interest_type == 'simple':
        # Công thức tính lãi đơn: Lãi = Số tiền vay * Lãi suất * Thời gian (tính theo năm)
        time_in_years = (due_date - current_date).days / 365  # Thời gian tính theo năm
        interest = principal * (interest_rate / 100) * (time_in_years)  # Tính lãi đơn
    elif interest_type == 'compound':
            # Công thức tính lãi kép: A = P * (1 + r/n)^(nt), trong đó n = 1 (lãi kép hàng năm)
        time_in_years = (due_date - current_date).days / 365  # Thời gian tính theo năm
        interest = principal * ((1 + interest_rate / 100) ** (time_in_years - 1))  # Tính lãi kép
    data['interest'] = interest    
    total_due = principal + interest
    data['remaining'] = total_due
    data["progress"] = (data['paid']/total_due)* 100  # Tính tỷ lệ tiến độ thanh toán (%)

    loan_transaction = {
        "account": data['account'],
        "type": "income",
        "amount": data['amount'],
        "category": "Vay",
        "description": "Vay tiền",
        "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    UserModel().create_transaction(loan_transaction)
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
        
        # Trích xuất các thông tin cần thiết từ khoản vay
        principal = int(loan['amount'])  # Số tiền vay ban đầu
        interest_rate = float(loan['interest_rate'])  # Lãi suất
        interest_type = loan['interestType']  # Loại lãi suất (lãi đơn hay lãi kép)
        paid = loan['paid']  # Số tiền đã trả
        remaining = loan['remaining']  # Số tiền còn lại cần trả
        due_date = datetime.strptime(loan['due_date'], '%Y-%m-%d')  # Ngày đến hạn, chuyển đổi từ chuỗi thành datetime
        current_date = datetime.strptime(data['date'], '%Y-%m-%d')  # Ngày thanh toán, chuyển đổi từ chuỗi thành datetime
        
        # Tính toán số tiền lãi cần trả dựa trên loại lãi suất (lãi đơn hay lãi kép)
        if interest_type == 'simple':
            # Công thức tính lãi đơn: Lãi = Số tiền vay * Lãi suất * Thời gian (tính theo năm)
            time_in_years = (due_date - current_date).days / 365  # Thời gian tính theo năm
            interest = principal * (interest_rate / 100) * time_in_years  # Tính lãi đơn
        elif interest_type == 'compound':
            # Công thức tính lãi kép: A = P * (1 + r/n)^(nt), trong đó n = 1 (lãi kép hàng năm)
            time_in_years = (due_date - current_date).days / 365  # Thời gian tính theo năm
            interest = principal * ((1 + interest_rate / 100) ** time_in_years - 1)  # Tính lãi kép
        
        # Tính tổng số tiền cần trả (gồm cả lãi)
        total_due = principal + interest  # Tổng số tiền cần trả (gồm cả lãi)
        total_paid = paid + float(data['amount'])  # Số tiền đã trả cộng thêm số tiền thanh toán hiện tại

        # Cập nhật số tiền còn lại cần phải trả
        remaining_balance = total_due - total_paid  # Số tiền còn lại

        # Chuẩn bị dữ liệu để cập nhật thông tin khoản vay
        updated_loan = {
            "paid": total_paid,  # Cập nhật số tiền đã trả
            "interest": interest,  # Cập nhật số tiền lãi
            "remaining": remaining_balance,  # Cập nhật số tiền còn lại cần trả
            "progress": (total_paid / total_due) * 100  # Tính tỷ lệ tiến độ thanh toán (%)
        }
        payment_transaction = {
            "account": data['account_id'],
            "type": "expense",
            "amount": data['amount'],
            "category": "Trả nợ",
            "description": "Trả nợ khoản vay",
            "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        }
        UserModel().create_transaction(payment_transaction)

        # Cập nhật thông tin khoản vay vào database
    loan_model.update_loan(ObjectId(id), updated_loan)

    # Chuyển hướng về trang danh sách khoản vay
    return redirect(url_for('loan.loan_route'))



def edit_loan_post(id):
    loan_model = UserModel()
    data = request.form.to_dict()
    data['amount'] = int(data['amount'])
    data['createTime'] = datetime.now() # thời gian tạo 
    loan_model.update_loan(ObjectId(id), data)
    
    return redirect(url_for('loan.loan_route'))

def add_lend():
    loan_model = UserModel()
    data = request.form.to_dict()
    data['amount'] = int(data['amount'])
    data['createTime'] = datetime.now() # thời gian tạo 
    lend_transaction = {
        "account": data['account'],
        "type": "expense",
        "amount": data['amount'],
        "category": "Cho vay",
        "description": "Cho vay tiền",
        "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    UserModel().create_transaction(lend_transaction)
    loan_model.create_lending(data)
    return redirect(url_for('loan.loan_route'))

def edit_lend_post(id):
    loan_model = UserModel()
    data = request.form.to_dict()
    data['amount'] = int(data['amount'])
    data['createTime'] = datetime.now() # thời gian tạo 
    loan_model.update_lending(ObjectId(id), data)
    return redirect(url_for('loan.loan_route'))

def delete_lend(id):
    lend_model = UserModel()
    lend_id = ObjectId(id)
    if id:
        lend_model.delete_lending(lend_id)
    return redirect(url_for('loan.loan_route'))