class Jar:
    """chiec lo"""
    def __init__(self,name=''):
        self.__name = name
        self.__money = 0
        self.__moneyGoal = 1000000

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
        if(value < 0):
            return False
        else:
            self.__money = value

    @property
    def moneyGoal(self):
        return self.__moneyGoal
    
    def SetMoneyGoal(self,value):
        if value>0:
            self.__moneyGoal = value
        else: 
            return False
        