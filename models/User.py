# from account import Account
# from category import Category
# from jar import Jar 
# from transaction import Transaction
# from credit import Credit
# from datetime import date

# class User:
#     # accounts = {'VCB':Account('VCB',100000,'NH'),
#     #             'MoMo':Account('Momo',500000,'Vi dien tu')}
#     # categorys = {'Ăn uống': Category(name = 'Ăn uống',jar = Category.jar1,purpose=Category.purposeSpend), #purpose 1: chi tiêu
#     #              'Tiết Kiệm':Category(name = 'Tiết Kiệm',jar = Category.jar2),  
#     #              'Vay':Category(name = 'Vay',jar = Category.jar1,purpose=Category.purposeIncome),    #purpose 2: thu nhập
#     #              'Cho Vay':Category(name = 'Cho Vay',jar = Category.jar1,purpose=Category.purposeSpend),
#     #              'Trả nợ': Category(name = 'Trả nợ',jar = Category.jar1),
#     #              'Thu nợ':Category(name = 'Thu nợ',jar = Category.jar1,purpose=Category.purposeIncome)}
    
#     transactions = {}
#     loans = {}
#     lends = {}

    

#     def __init__(self):
#         self.__id = ""
#         self.__name = ""
#         self.__phone = ""
#         self.__password = ""
#         #self.__idTransaction = len(self.transactions)
#         # self.__idLoan = len(self.loans)
#         # self.__idLend = len(self.lends)

#     @property
#     def id(self):
#         return self.__id

#     @id.setter
#     def id(self, value):
#         if len(value) == 6:
#             self.__id = value
#         return False

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, value):
#         self.__name = value

#     @property
#     def phone(self):
#         return self.__phone

#     @phone.setter
#     def phone(self, value):
#         if len(value) == 10 and value.isdigit():
#             self.__phone = value
#         else: 
#             return False

#     @property
#     def password(self):
#         return self.__password
#     @password.setter
#     def password(self, value):
#         self.__password = value

#     # #Operation With Category
#     # def CreateCategory(self,nameCategory,moneyGoal=100000,jar=Category.jars[0],
#     #                    purpose = Category.purposeSpend):
#     #     category = Category(nameCategory,moneyGoal,jar,purpose)
#     #     self.categorys.update({nameCategory:category})

#     # def SetMoneyCategory(self,namecategory,moneyGoal):
#     #     if namecategory in self.categorys.keys():
#     #         self.categorys[namecategory].SetMoneyGoal(moneyGoal)
        
#     # #Operation with Transaction
#     # # phan biet Transaction dựa trên id
#     # def CreateTransaction(self,idTransaction,nameAccount,nameCategory,moneyTransaction,
#     #                       dateTransaction=date.today(),note=''):
#     #     #Việc thêm giao dịch thực hiện khi: mục đích là thu nhập hoặc số tiền trong tài khoản lớn hơn số tiền giao dich
#     #     if self.categorys[nameCategory].purpose == Category.purposeIncome or self.accounts[nameAccount].money > moneyTransaction:
#     #         transaction = Transaction(self.__idTransaction,self.accounts[nameAccount],self.categorys[nameCategory],
#     #                                 moneyTransaction,dateTransaction,note)
#     #         self.transactions.update({idTransaction:transaction})
#     #         self.categorys[nameCategory].money += moneyTransaction
#     #         if self.categorys[nameCategory].purpose == Category.purposeSpend:    # 0 là chi tiêu
#     #             self.accounts[nameAccount].money -= moneyTransaction
#     #         elif self.categorys[nameCategory].purpose == Category.purposeIncome:  # 1 là thu nhập
#     #             self.accounts[nameAccount].money += moneyTransaction
#     #     else:
#     #         return False

#     # def RemoveTransaction(self, idTransaction):
#     #     # nếu id giao dịch là hợp lệ thì thực hiện
#     #     if idTransaction in self.transactions.keys():
#     #         oldTransaction = self.transactions[idTransaction]
#     #         oldNameCategory = oldTransaction.category.name
#     #         oldNameAccount = oldTransaction.account.name
#     #         self.categorys[oldNameCategory].money -= oldTransaction.money
#     #         if self.categorys[oldNameCategory].purpose == Category.purposes[0]:    # 0 là chi tiêu
#     #             self.accounts[oldNameAccount].money += oldTransaction.money
#     #         elif self.categorys[oldNameCategory].purpose == Category.purposes[1]:  # 1 là chi tiêu
#     #             self.accounts[oldNameAccount].money -= oldTransaction.money
#     #         del self.transactions[idTransaction] 
#     #     else: 
#     #         return False
        
#     # def EditTransaction(self,idTransaction,newNameAccount,newNameCategory,newMoneyTransaction,
#     #                     newDateTransaction=date.today(),newNote=''):
#     #     # xóa giao dịch trước
#     #     self.RemoveTransaction(idTransaction)
#     #     # tạo giao dịch mới
#     #     self.CreateTransaction(newNameAccount,newNameCategory,newMoneyTransaction,
#     #                            newDateTransaction,newNote)

#     # #Operation with Loan
#     # def CreateLoan(self,nameLoand,nameAccount,nameCategory='Vay',moneyTransaction=0,dateTransaction=date.today(),
#     #                note='', spender ="",phone="", dateDue= date.today(), rate = 0):
#     #     self.__idLoan +=1
#     #     loan = Credit(self.__idLoan,nameLoand,self.accounts[nameAccount],self.categorys[nameCategory],
#     #                               moneyTransaction,dateTransaction,note,spender,phone,dateDue,rate)
#     #     self.loans.update({self.__idLoan:loan})
#     #     # self.categorys[nameCategory].money += moneyTransaction
#     #     # self.accounts[nameAccount].money += moneyTransaction
#     #     self.CreateTransaction(nameAccount,nameCategory,moneyTransaction,dateTransaction,note=f'Vay cua {spender}')

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
        
#     # def PayDebt(self, idloand,moneyPay,accountPay,category = "Trả nợ",datePay=date.today,note=""):
#     #     # nếu số tiền trong tài khoản lớn hơn số tiền trả nợ thì mới thực hiện giao dịch
#     #     if self.accounts[accountPay].money >= moneyPay:
#     #         self.loans[idloand].amountPaid += moneyPay
#     #         self.CreateTransaction(nameAccount=accountPay,nameCategory=category,moneyTransaction=moneyPay,
#     #                                dateTransaction=datePay, note=note)
#     #     else:
#     #         return False

#     # #Operation with Lend
#     # def CreateLend(self,nameLend,nameAccount,nameCategory="Cho Vay",moneyTransaction=0,dateTransaction=date.today(),
#     #                note='', spender ="",phone="", dateDue= date.today(), rate = 0):
#     #     #nếu số tiền trong tài khoản lớn hơn số tiền cho vay thì mới thực hiện giao dịch cho vay
#     #     if self.accounts[nameAccount].money >= moneyTransaction:
#     #         self.__idLend+=1
#     #         lend = Credit(self.__idLend,nameLend,self.accounts[nameAccount],self.categorys[nameCategory],
#     #                                 moneyTransaction,dateTransaction,note,spender,phone,dateDue,rate)
#     #         self.lends.update({self.__idLend:lend})
#     #         # self.categorys[nameCategory].money += moneyTransaction
#     #         # self.accounts[nameAccount].money -= moneyTransaction
#     #         self.CreateTransaction(nameAccount,nameCategory,moneyTransaction,dateTransaction,note=f'cho {spender} vay')

#     # def RemoveLend(self, idLend):
#     #     # if idLend in self.loans.keys():
#     #     oldLend = self.lends[idLend]
#     #     # Trường hợp xóa khoản cho vay do nhập sai
#     #     if oldLend.amountPaid == 0:
#     #         self.accounts[oldLend.account.name] += oldLend.money
#     #         del self.lends[idLend] 
#     #     # Trường hợp xóa khoản vay mà ko thu hồi được tiền còn lại
#     #     else:
#     #         del self.lends[idLend]

#     # def EditLend(self,idLend,newNameLend,newNameAccount,nameCategory='Cho Vay',newMoneyTransaction=0,newDateTransaction=date.today(),
#     #                note='', spender ="",phone="", newDateDue= date.today(), newRate = 0):
#     #     # xóa giao dịch trước
#     #     self.RemoveLend(idLend)
#     #     # tạo giao dịch mới
#     #     self.CreateLend(idLend,newNameLend,self.accounts[newNameAccount],self.categorys[nameCategory],
#     #                               newMoneyTransaction,newDateTransaction,note,spender,phone,newDateDue,newRate)
        
#     # def DebtColection(self, idLend,idTransaction,moneyPay,accountPay,category = "Thu nợ",datePay=date.today,note=""):
#     #     if idLend in self.lends.keys():
#     #         self.lends[idLend].amountPaid += moneyPay
#     #         self.CreateTransaction(idTransaction,nameAccount=accountPay,nameCategory=category,moneyTransaction=moneyPay,
#     #                                dateTransaction=datePay, note=note)
#     #     else:
#     #         return False

#     # # Operation with Account
#     # def get_account(self,account_id ={}):
#     #     User.accountss = self.mongo.db.accounts.find(account_id)

#     # def CreateAccount(self,idAccount,nameAccount,moneyAccount,accountType):   
#     #     if idAccount in self.accounts.keys():
#     #         return False
#     #     account = Account(nameAccount,moneyAccount,accountType)
#     #     self.accounts.update({idAccount:account})

#     # # chon tai khoan edit: theo ten tai khoan, neu theo id thì sửa lại
#     # def EditAccount(self,idAccount,nameEditAccount,newNameAccount,moneyAccount,accountType):
#     #     if idAccount in self.accounts.keys():
#     #         self.accounts[idAccount].name = newNameAccount
#     #         self.accounts[idAccount].money = moneyAccount
#     #         self.accounts[idAccount].accountType = accountType

#     # # sử dụng tên tài khoản để phân biệt giưa các tài khoản
#     # def RemoveAccount(self,idAccount,nameAccount):
#     #     if idAccount in self.accounts.keys():
#     #         idTransactionRemove = [] 
#     #         for id in self.loans.keys():
#     #             if self.loans[id].account.name == idAccount:
#     #                 idTransactionRemove.append(id)
#     #         for id in idTransactionRemove:
#     #                 self.RemoveTransaction(id)
#     #         del self.accounts[idAccount]

#     # def TransferAccount(self,idSourceAccount,idDestinationAccount,money,note):
#     #     if self.accounts[idSourceAccount].money >= money :
#     #         self.accounts[idSourceAccount].money -= money
#     #         self.accounts[idDestinationAccount].money += money
#     #     else:
#     #         return False


# # user1 = User()
# # user1.CreateCategory('Ăn uống',500000)
# # user1.CreateCategory('di chuyen',purpose=Category.purposes[1])

# # # user1.SetMoneyCategory('Ăn uống',10)
# # # for nameCategory in user1.categorys.keys():
# # #     print(user1.categorys[nameCategory].purpose)

# # user1.CreateAccount("VCB",100000,"NH")
# # user1.CreateAccount("ACB",500000,"NH")

# # for cate in user1.categorys.keys():
# #     print(user1.categorys[cate].money)

# # for acc in user1.accounts.keys():
# #     print(user1.accounts[acc].money)

# # user1.CreateTransaction(1,"VCB","Ăn uống",50000,date.today(),'am thuc')
# # user1.CreateTransaction(2,"ACB","di chuyen",100000,date.today(),'di dao')

# # for cate in user1.categorys.keys():
# #     print(user1.categorys[cate].money)

# # for acc in user1.accounts.keys():
# #     print(user1.accounts[acc].money)
    
        
 