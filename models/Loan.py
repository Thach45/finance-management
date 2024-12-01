from Transaction import Transaction
from Account import Account
from Category import Category
from datetime import date

class Loan(Transaction):
    def __init__(self, account, transactionType, money=0, transactionDate= date.today(), note="", spender ="", dateDue= date.today(), rate = 0):
        super().__init__(account, transactionType, money, transactionDate, note)
        self.__spender = spender
        self.__dateDue = dateDue
        self.__rate = rate

    @property
    def spender(self):
        return self.__spender
    @spender.setter
    def spender(self, value):
        self.__spender = value

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
        
