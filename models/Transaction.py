from Account import Account 
from Category import Category
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

    # def to_dict(self):
    #     return {
    #         "id": self.__id,
    #         "account": self.__account.name,  # Giả sử Account có thuộc tính name
    #         "category": self.__category.name,  # Giả sử Category có thuộc tính name
    #         "money": self.__money,
    #         "transactionDate": self.__transactionDate.strftime('%d/%m/%Y'),
    #         "note": self.__note
    # }

    # def __str__(self):
    #     return f"Transaction(ID: {self.__id}, Account: {self.__account.name}, " \
    #         f"Category: {self.__category.name}, Money: {self.__money}, " \
    #         f"Date: {self.__transactionDate}, Note: {self.__note})"
    
    # @staticmethod
    # def create_transaction(data):
    #     return Transaction(
    #         id=data["id"],
    #         account=data["account"],
    #         category=data["category"],
    #         money=data["money"],
    #         transactionDate=data["transactionDate"],
    #         note=data["note"]
    #     )
