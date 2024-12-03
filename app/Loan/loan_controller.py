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

    total_loan = sum(loan['amount'] for loan in loans)
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
    data['amount'] = int(data['amount'])
    data['createTime'] = datetime.now() # thời gian tạo 
    print(data)
    loan_model.create_loan(data)
    return redirect(url_for('loan.loan_route'))


def edit_loan(id):
    loan_model = UserModel()
    idLoan = {"_id": ObjectId(id)}
    loans = list(loan_model.get_loans(idLoan))
    loan = [loan for loan in loans if loan['_id'] == ObjectId(id)][0]
    return render_template('editLoan.html', loan=loan)



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
    loan_model = UserModel()
    data = request.form.to_dict()
    # data sẽ trả về một dict như vậy hãy 
    # {
    # "account_id": "67432265b877ca925af835da",
    # "amount": "1000",
    # "borrower": "Nguyen Hoang Thach",
    # "date": "2024-12-02",
    # "discription": ""
    # }
    loan = list(loan_model.get_loans({"_id": ObjectId(id)}))
    #giờ ô tính toán cái lãi suất tiền phải trả rồi sửa xuống cái dict dưới rồi lưu vào database
    # [{'_id': ObjectId('67432d84b877ca925af835e2'),
    #    'type': 'Vay kinh doanh',
    #      'borrower': 'Nguyễn Văn C',
    #        'status': 'Chưa đến hạn',
    #          'amount': 20000000,
    #            'interest_rate': 10,
    #              'interest_type': 'simple',
    #                'loan_date': '2024-03-01',
    #                  'due_date': '2024-09-01', 
    #                  'description': 'Ghi chú về khoản vay',
    #                    'contact': '0912345678',
    #                      'paid': 20000000, 
    #                      'interest': 1250000, 
    #                      'remaining': 31250000,
    #                        'progress': 40}]
    return redirect(url_for('loan.loan_route'))

def edit_loan_post(id):
    loan_model = UserModel()
    data = request.form.to_dict()
    data['amount'] = int(data['amount'])
    data['createTime'] = datetime.now() # thời gian tạo 
    loan_model.update_loan(ObjectId(id), data)
    return redirect(url_for('loan.loan_route'))