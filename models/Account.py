class Account:
    def __init__(self,name='',money = 0,accountType = "") :
        self.__name = name
        if money < 0:
            self.__money = 0
        else:
            self.__money = money
        self.__accountType = accountType

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,value):
        if value>0:
            self.__money = value
        else:
            return False
        
    @property
    def accountType(self):
        return self.__accountType
    @accountType.setter
    def accountType(self,value):
        self.__accountType = value

    def SetMoney(self,value):
        if value>0:
            self.money = value
        else:
            return False
    
    # def info(self):
    #     print(f"ten tk:{self.name}, sodu: {self.money}, loai:{self.accountType}")
