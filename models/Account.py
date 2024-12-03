class Account:
    def __init__(self,name='',type = "",balance = 0) :
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
    def money(self):
        return self.__balance
    @money.setter
    def money(self,value):
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
            self.money = value
        else:
            return False