from Account import Account
from Category import Category
from Jar import Jar 

class User():
    accounts = {}
    categorys = {}
    
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
        if self.accounts[nameAccount] in self.accounts.keys():
            del self.accounts[nameAccount]

    #Operation With Category
    def CreateCategory(self,nameCategory,moneyGoal=100000,jar=Category.jars[0],purpose = Category.purposes[0]):
        category = Category(nameCategory,moneyGoal,jar,purpose)
        self.categorys.update({nameCategory:category})
    def SetMoneyCategory(self,namecategory,moneyGoal):
        if namecategory in self.categorys.keys():
            self.categorys[namecategory].SetMoneyGoal(moneyGoal)
        
    
# user1 = User()
# user1.CreateCategory('an uong',500000)
# user1.CreateCategory('di chuyen')
# user1.SetMoneyCategory('an uong',10)
# for nameCategory in user1.categorys.keys():
#     print(user1.categorys[nameCategory].purpose)

# user1 = User()
# user1.CreateAccount("VCB",10,"NH")
# user1.CreateAccount("ACB",50,"NH")
# user1.EditAccount('ACB','ABC',100,"vi dien tu")
# user1.RemoveAccount('VCB')
# for nameAccount in user1.accounts.keys():
#     user1.accounts[nameAccount].info()
