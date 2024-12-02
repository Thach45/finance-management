from transaction import Transaction
from account import Account
from category import Category
from datetime import date

class Credit(Transaction):
    def __init__(self,id,name, account=Account(), category=Category(), money=0, transactionDate= date.today(),
                  note="", spender ="",phone="", dateDue= date.today(), rate = 0):
        super().__init__(id,account, category, money, transactionDate, note)
        self.__name = name
        self.__spender = spender
        self.__phone = phone
        self.__dateDue = dateDue
        self.__rate = rate
        self.__amountPaid = 0
        self.__interes = self.rate*self.money

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def spender(self):
        return self.__spender
    @spender.setter
    def spender(self, value):
        self.__spender = value

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
    def dateDue(self):
        return self.__dateDue
    @dateDue.setter
    def dateDue(self, value:date):
        self.__dateDue = value

    @property
    def rate(self):
        return self.__rate
    @rate.setter
    def rate(self, value:float):
        if value >= 0:
            self.__rate = value
        else:
            raise ValueError("Rate must be a positive value")
    @property
    def amountPaid(self):
        return self.__amountPaid
    @amountPaid.setter
    def amountPaid(self, value):
        self.__amountPaid = value
    
    @property
    def interes(self):
        return self.__interes
        
    

