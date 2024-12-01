class Account:
    def __init__(self,id='',accountType = "") :
        self.__id = id
        self.__money = 0
        self.__accountType = accountType

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id = value

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
