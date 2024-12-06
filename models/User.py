from flask import render_template, current_app, url_for
from flask import jsonify
from account import Account
from category import Category
from jar import Jar 
from transaction import Transaction
from credit import Credit
from datetime import date
from models import UserModel
from flask_pymongo import PyMongo
from flask import current_app

class User:
    accounts = {0:Account('VCB',100000,'NH'),
                1:Account('Momo',500000,'Vi dien tu'),
                2:Account('tiền mặt',100000,'tien mat')}
    
    categorys = {'Ăn uống': Category(name = 'Ăn uống',jar = Category.jar1,purpose=Category.purposeSpend), #purpose 1: chi tiêu
                 'Lương': Category(name = 'Lương',jar = Category.jar1,purpose=Category.purposeIncome),
                 'Tiết Kiệm':Category(name = 'Tiết Kiệm',jar = Category.jar2),  
                 'Vay':Category(name = 'Vay',jar = Category.jar1,purpose=Category.purposeIncome),    #purpose 2: thu nhập
                 'Cho Vay':Category(name = 'Cho Vay',jar = Category.jar1,purpose=Category.purposeSpend),
                 'Trả nợ': Category(name = 'Trả nợ',jar = Category.jar1),
                 'Thu nợ':Category(name = 'Thu nợ',jar = Category.jar1,purpose=Category.purposeIncome),
                 'chuyển khoản':Category(name='Chuyển khoản',jar=Category.jar1,purpose=Category.purposeTransferAcc)}
    
    transactions ={0:Transaction(0,date.today(),Category.purposeSpend,'VCB','Ăn uống','',100000),
                   1:Transaction(1,date.today(),Category.purposeSpend,'tiền mặt','Ăn uống','',50000)}

    credits = {0:Credit(id=0,amount=500000,credit_date=date.today(),type='',account='',category='Vay',name_credit='Vay mua nha',interest_rate=0,interes_type='',
                 due_date=date.today(),crediter='',contact='',description=''),
               1:Credit(id=1,amount=100000,credit_date=date.today(),type='',account='',category='Cho Vay',name_credit='Cho Hoa vay',interest_rate=0,interes_type='',
                 due_date=date.today(),crediter='',contact='',description='')}
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__phone = ""
        self.__password = ""
        self.__id_transaction = len(self.transactions)
        

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if len(value) == 6:
            self.__id = value
        return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if len(value) == 10 and value.isdigit():
            self.__phone = value
        else: 
            return False

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def id_transaction(self):
        return self.__id_transaction

    #Operation With Category
    def CreateCategory(self,nameCategory,moneyGoal=100000,jar=Category.jars[0],
                       purpose = Category.purposeSpend):
        if nameCategory not in self.categorys.keys():
            category = Category(nameCategory,moneyGoal,jar,purpose)
            self.categorys.update({nameCategory:category})
        else: 
            print('Đã tồn tại')

    def SetMoneyCategory(self,namecategory,moneyGoal):
        if namecategory in self.categorys.keys():
            self.categorys[namecategory].SetMoneyGoal(moneyGoal)
    
    def infoCategory(self):
        print('----------------------Category----------------------------')
        for category in self.categorys.values():
            print(f'{category.name}, loại: {category.purpose}, lọ: {category.jar}, số tiền mục tiêu: {category.moneyGoal}, số tiền đã dùng: {category.money}')
        print('----------------------------------------------------------')
    #Operation with Transaction
    # phan biet Transaction dựa trên id
    def CreateTransaction(self,idTransaction,nameAccount,nameCategory,moneyTransaction,typeTransaction='',
                          dateTransaction=date.today(),note=''):
        #Việc thêm giao dịch thực hiện khi: mục đích là thu nhập hoặc số tiền trong tài khoản lớn hơn số tiền giao dich
        for id in self.accounts.keys():
            if self.accounts[id].name == nameAccount:
                idAcc = id
        if typeTransaction == Category.purposeIncome or self.accounts[idAcc].balance >= moneyTransaction:
            transaction = Transaction(id=idTransaction,date=dateTransaction,type=typeTransaction,account=nameAccount,
                                      category=nameCategory,description=note,amount=moneyTransaction)                    
            self.transactions.update({idTransaction:transaction})
            self.__id_transaction += 1
            self.categorys[nameCategory].money += moneyTransaction
            if typeTransaction == Category.purposeSpend:    
                self.accounts[idAcc].balance -= moneyTransaction
            elif typeTransaction == Category.purposeIncome:  
                self.accounts[idAcc].balance += moneyTransaction
        else:
            print("lỗi giao dịch")
            return False

    def RemoveTransaction(self, idTransaction):
        # nếu id giao dịch là hợp lệ thì thực hiện
        if idTransaction in self.transactions.keys():
            oldTransaction = self.transactions[idTransaction]
            oldNamCategory = oldTransaction.category
            oldTypeTransaction = oldTransaction.type
            oldNameAcc = oldTransaction.account
            for id in  self.accounts.keys():
                if self.accounts[id].name == oldNameAcc:
                    idAcc = id
            if oldTypeTransaction == Category.purposeSpend: 
                self.categorys[oldTransaction] -= oldTransaction.amount
                self.accounts[idAcc].balance += oldTransaction.amount
                del self.transactions[idTransaction]
            elif oldTypeTransaction == Category.purposeIncome:
                if self.accounts[idAcc].balance >= oldTransaction.amount: 
                    self.categorys[oldNamCategory].money -= oldTransaction.amount
                    self.accounts[idAcc].balance -= oldTransaction.amount
                    del self.transactions[idTransaction] 
                else:
                    print('lỗi ràng buộc số tiền')
                    return False
            else:
                pass
        else: 
            return False
        
    def EditTransaction(self,idTransaction,nameAccount,nameCategory,moneyTransaction,typeTransaction='',
                          dateTransaction=date.today(),note=''):
        # xóa giao dịch trước
        if(self.RemoveTransaction(idTransaction)!=False):
            # tạo giao dịch mới
            self.CreateTransaction(idTransaction,nameAccount,nameCategory,moneyTransaction,typeTransaction,
                               dateTransaction,note)
    
    def infoTransaction(self):
        print('----------------------Transaction----------------------------')
        for transaction in self.transactions.values():
            print(f'danh mục: {transaction.category}, tài khoản: {transaction.account}, số tiền: {transaction.amount}, note: {transaction.description}')
        print('-------------------------------------------------------------')

    #Operation with Loan
    def CreateCredit(self,id=0,amount=0,credit_date=date.today(),type='',account='',category='',name_credit='',interest_rate=0,interes_type='',
                    due_date=date.today(),crediter='',contact='',description=''):
        credit = Credit(id=id,amount=amount,credit_date=credit_date,type=type,account=account,category=category,
                    name_credit=name_credit,interest_rate=interest_rate,interes_type=interes_type,
                    due_date=due_date,crediter=crediter,contact=contact,description=description)
        credit.updateProgressCredit()
        self.credits.update({id:credit})
        self.CreateTransaction(idTransaction=id,nameAccount=account,nameCategory=category,moneyTransaction=amount,
                                dateTransaction=credit_date,note=description)
        
    def infoCredit(self):
        print('----------------------Credit------------------------------')
        amount_payable = 0
        amount_receivable = 0
        for credit in self.credits.values():
            credit.updateProgressCredit()
            credit.info()
            if credit.category =='Vay':
                amount_payable += credit.remaining
            elif credit.category =='Cho Vay':
                amount_receivable += credit.remaining
        print(f"Tổng số tiền cần trả: {amount_payable}, Tổng số tiền cần thu:{amount_receivable}")
        print('----------------------------------------------------------')

#     # def RemoveLoan(self, idLoan):
#     #     oldLoan = self.loans[idLoan]
#     #     # nếu muốn xóa khoản vay thì số nợ phải được thanh toán xong, 
#     #     # nếu chưa xong tài khoản tự động trừ tiền tương ứng với số nợ còn lại
#     #     # trường hợp 1: khoản vay tạo bị sai và chưa có bất kỳ giao dịch trả nợ nào
#     #     if oldLoan.amountPaid == 0:
#     #         self.PayDebt(idLoan,moneyPay=(oldLoan.money-oldLoan.amountPaid),category="Trả nợ",
#     #                         datePay=date.today(),note="Thanh toan xong khoan vay")
#     #         # sau khi thanh toán thành công thì có thể xóa khoản vay
#     #         if oldLoan.money == oldLoan.amountPaid:
#     #             del self.loans[idLoan]
#     #         else:
#     #             return False
#     #     # trường hợp 2: khoản vay đã có hiệu lực nhưng muốn xóa khoản vay này => khác nhau chỗ tiền lãi suất
#     #     else:
#     #         self.PayDebt(idLoan,moneyPay=(oldLoan.money + oldLoan.interes - oldLoan.amountPaid),category="Trả nợ",
#     #                         datePay=date.today(),note="Thanh toan xong khoan vay")
#     #         # sau khi thanh toán thành công thì có thể xóa khoản vay
#     #         if oldLoan.money == oldLoan.amountPaid:
#     #             del self.loans[idLoan]
#     #         else:
#     #             return False


#     # def EditLoan(self,idLoan,newNameLoan,newNameAccount,nameCategory='Vay',newMoneyTransaction=0,newDateTransaction=date.today(),
#     #                note='', spender ="",phone="", newDateDue= date.today(), newRate = 0):
#     #     # xóa giao dịch trước
#     #     if self.RemoveLoan(idLoan) != False:
#     #         # tạo giao dịch mới
#     #         self.CreateLoan(newNameLoan,self.accounts[newNameAccount],self.categorys[nameCategory],
#     #                                 newMoneyTransaction,newDateTransaction,note,spender,phone,newDateDue,newRate)
        
    def PayDebt(self, id_credit,moneyPay,accountPay,category = "Trả nợ",datePay=date.today,note=""):
        if self.CreateTransaction(self.id_transaction,nameAccount=accountPay,nameCategory=category,moneyTransaction=moneyPay,
                                  typeTransaction=self.categorys[category].purpose,dateTransaction=datePay,note=note) != False:
            self.credits[id_credit].paid += moneyPay
            self.credits[id_credit].updateProgressCredit()

    # Operation with Account
    def CreateAccount(self,idAccount,nameAccount,moneyAccount,accountType):   
        if idAccount in self.accounts.keys():
            return False
        account = Account(nameAccount,moneyAccount,accountType)
        self.accounts.update({idAccount:account})

    # chon tai khoan edit: theo ten tai khoan, neu theo id thì sửa lại
    def EditAccount(self,idAccount,newNameAccount,moneyAccount,accountType):
        if idAccount in self.accounts.keys():
            self.accounts[idAccount].name = newNameAccount
            self.accounts[idAccount].balance = moneyAccount
            self.accounts[idAccount].accountType = accountType
        

    # sử dụng tên tài khoản để phân biệt giưa các tài khoản
    def RemoveAccount(self,idAccount):
        if idAccount in self.accounts.keys():
            del self.accounts[idAccount]

    # Good
    def TransferAccount(self,idSourceAccount,idDestinationAccount,money,note):
        if self.accounts[idSourceAccount].balance >= money :
            self.accounts[idSourceAccount].balance -= money
            self.accounts[idDestinationAccount].balance += money
        else:
            return False
    
    def infoAccount(self):
        print('----------------------------------------------------------')
        for acc in self.accounts.values():
            print(f'tên: {acc.name}, số dư:{acc.balance}')
        print('----------------------------------------------------------')    

    


user1 = User()

user1.CreateAccount(10,'ACB',10,'NH')
user1.EditAccount(1,'zalopay',10,'vi dien tu')
user1.CreateTransaction(user1.id_transaction,'VCB','Lương',5000000,typeTransaction=Category.purposeIncome,
                        dateTransaction=date.today(),note="")
user1.CreateTransaction(15,'VCB','Lương',1000000,typeTransaction=Category.purposeIncome,
                        dateTransaction=date.today(),note="")

user1.EditTransaction(15,'VCB','Ăn uống',1000000,typeTransaction=Category.purposeSpend,
                        dateTransaction=date.today(),note="")

user1.CreateCategory('Giải trí',jar=Category.jar4,purpose=Category.purposeSpend)
user1.CreateCredit(user1.id_transaction,amount=100000,category='Vay',name_credit='Vay mua xe',account='VCB')
user1.PayDebt(0,200000,'VCB','Trả nợ',date.today())
user1.PayDebt(1,50000,'VCB','Thu nợ',date.today())
user1.infoTransaction()
user1.infoCredit()

 