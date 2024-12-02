from account import Account
from category import Category
from jar import Jar 
from transaction import Transaction
from loan import Loan
from datetime import date

class User:
    accounts = {'VCB':Account('VCB',100000,'NH'),
                'MoMo':Account('Momo',500000,'Vi dien tu')}
    categorys = {'An uong': Category(name = 'An uong',jar = Category.jar1,),
                 'Tiet kiem':Category(name = 'Tiet kiem',jar = Category.jar2),
                 'Vay':Category(name = 'Vay',jar = Category.jar2)}
    transactions = {}

    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__phone = ""
        self.__password = ""

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

    #Operation With Category
    def CreateCategory(self,nameCategory,moneyGoal=100000,jar=Category.jars[0],
                       purpose = Category.purposes[0]):
        category = Category(nameCategory,moneyGoal,jar,purpose)
        self.categorys.update({nameCategory:category})

    def SetMoneyCategory(self,namecategory,moneyGoal):
        if namecategory in self.categorys.keys():
            self.categorys[namecategory].SetMoneyGoal(moneyGoal)
        
    #Operation with Transaction
    def CreateTransaction(self,id,nameAccount,nameCategory,moneyTransaction,
                          dateTransaction=date.today(),note=''):
        transaction = Transaction(id,self.accounts[nameAccount],self.categorys[nameCategory],
                                  moneyTransaction,dateTransaction,note)
        self.transactions.update({id:transaction})
        self.categorys[nameCategory].money += moneyTransaction
        if self.categorys[nameCategory].purpose == Category.purposes[0]:    # 0 là chi tiêu
            self.accounts[nameAccount].money -= moneyTransaction
        elif self.categorys[nameCategory].purpose == Category.purposes[1]:  # 1 là chi tiêu
            self.accounts[nameAccount].money += moneyTransaction

    def RemoveTransaction(self, id):
        if id in self.transactions.keys():
            oldTransaction = self.transactions[id]
            oldNameCategory = oldTransaction.category.name
            oldNameAccount = oldTransaction.account.name
            self.categorys[oldNameCategory].money -= oldTransaction.money
            if self.categorys[oldNameCategory].purpose == Category.purposes[0]:    # 0 là chi tiêu
                self.accounts[oldNameAccount].money += oldTransaction.money
            elif self.categorys[oldNameCategory].purpose == Category.purposes[1]:  # 1 là chi tiêu
                self.accounts[oldNameAccount].money -= oldTransaction.money
            del self.transactions[id] 
    def EditTransaction(self,id,newNameAccount,newNameCategory,newMoneyTransaction,
                        newDateTransaction=date.today(),newNote=''):
        # xóa giao dịch trước
        self.RemoveTransaction(id)
        # tạo giao dịch mới
        self.CreateTransaction(id,newNameAccount,newNameCategory,newMoneyTransaction,
                               newDateTransaction,newNote)

    #Operation with Loan
    def CreateLoan(self,id,nameAccount,nameCategory,moneyTransaction,dateTransaction=date.today(),
                   note='', spender ="", dateDue= date.today(), rate = 0):
        transaction = Loan(id,self.accounts[nameAccount],self.categorys[nameCategory],
                                  moneyTransaction,dateTransaction,note,spender,dateDue,rate)
        self.transactions.update({id:transaction})
        self.categorys[nameCategory].money += moneyTransaction
        self.accounts[nameAccount].money += moneyTransaction

    def RemoveLoan(self, id):
        if id in self.transactions.keys():
            oldTransaction = self.transactions[id]
            self.accounts[oldTransaction.account.name] -= oldTransaction.money
            del self.transactions[id] 

    def EditLoan(self,id,newNameAccount,nameCategory,newMoneyTransaction,newDateTransaction=date.today(),
                   note='', spender ="", newDateDue= date.today(), newRate = 0):
        # xóa giao dịch trước
        self.RemoveLoan(id)
        # tạo giao dịch mới
        self.CreateLoan(id,id,self.accounts[newNameAccount],self.categorys[nameCategory],
                                  newMoneyTransaction,newDateTransaction,note,spender,newDateDue,newRate)

    # Operation with Account
    def CreateAccount(self,nameAccount,moneyAccount,accountType):
        if nameAccount in self.accounts.keys():
            return False
        account = Account(nameAccount,moneyAccount,accountType)
        self.accounts.update({nameAccount:account})
    def EditAccount(self,nameEditAccount,newNameAccount,moneyAccount,accountType):
        if nameEditAccount in self.accounts.keys():
            self.accounts[nameEditAccount].name = newNameAccount
            self.accounts[nameEditAccount].money = moneyAccount
            self.accounts[nameEditAccount].accountType = accountType
    def RemoveAccount(self,nameAccount):
        if nameAccount in self.accounts.keys():
            idTransactionRemove = [] 
            for id in self.transactions.keys():
                if self.transactions[id].account.name == nameAccount:
                    idTransactionRemove.append(id)
            for id in idTransactionRemove:
                    self.RemoveTransaction(id)
            del self.accounts[nameAccount]





# user1 = User()
# user1.CreateCategory('an uong',500000)
# user1.CreateCategory('di chuyen',purpose=Category.purposes[1])

# # user1.SetMoneyCategory('an uong',10)
# # for nameCategory in user1.categorys.keys():
# #     print(user1.categorys[nameCategory].purpose)

# user1.CreateAccount("VCB",100000,"NH")
# user1.CreateAccount("ACB",500000,"NH")

# for cate in user1.categorys.keys():
#     print(user1.categorys[cate].money)

# for acc in user1.accounts.keys():
#     print(user1.accounts[acc].money)

# user1.CreateTransaction(1,"VCB","an uong",50000,date.today(),'am thuc')
# user1.CreateTransaction(2,"ACB","di chuyen",100000,date.today(),'di dao')

# for cate in user1.categorys.keys():
#     print(user1.categorys[cate].money)

# for acc in user1.accounts.keys():
#     print(user1.accounts[acc].money)
    
# user1.RemoveAccount("ACB")

# for cate in user1.categorys.keys():
#     print(user1.categorys[cate].money)

# for acc in user1.accounts.keys():
#     print(user1.accounts[acc].money)