class Account:
    def __init__(self,name='',balance = 0,type = '') :
        self.__name = name
        if balance < 0:
            self.__balance = 0
        else:
            self.__balance = balance
        self.__accountType = type

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,value):
        if value>=0:
            self.__balance = value
        else:
            return False
        
    @property
    def accountType(self):
        return self.__accountType
    @accountType.setter
    def accountType(self,value):
        self.__accountType = value

    def SetMoney(self,value):
        if value>=0:
            self.balance = value
        else:
            return False