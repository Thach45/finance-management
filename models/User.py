from Account import Account
import Category

class User():
    accounts = []
    categorys = []
    jars = []
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__phone = ""
        self.__password = ""
        # self.__account = []
        # self.__category = []

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
    def CreateAccount(self,name,money,accountType):
        account = Account()
        account.name = name
        account.money = money
        account.accountType = accountType
        self.accounts.append(account)
    def EditAccount(self,account,name,typeAccount):
        self.account.name = name
        self.account.typeAccount = typeAccount
    def RemoveAccount(self,account):
        self.accounts.remove(account)
    
        
 