from account import Account 
from category import Category
from datetime import date


class Transaction:
    def __init__(self,id, account=Account(), category=Category(),
                  money=0, transactionDate=date.today(), note =""):
        self.__account = account
        self.__category = category
        self.__money = money
        self.__transactionDate = transactionDate
        self.__note =note
        self.__id = id

    @property
    def account(self):
        return self.__account
    @account.setter
    def account(self, value:Account):
        self.__account = value

    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, value:Category):
        self.__category= value

    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, value):
        if value > 0:
            self.__money = value
        else:
            raise ValueError("Money must be a positive value")

    @property
    def transactionDate(self):
        return self.__transactionDate
    @transactionDate.setter
    def transactionDate(self, value:date):
        self.__transactionDate = value

    @property 
    def note(self):
        return self.__note
    @note.setter
    def note(self, value):
        self.__note = value