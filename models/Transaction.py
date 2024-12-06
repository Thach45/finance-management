from account import Account 
from category import Category
from datetime import date


class Transaction:
    def __init__(self,id=0, date=date.today(),type='',account="",category="",
                   description ="",amount=0):
        self.__id = id
        self.__date = date
        self.__type = type
        self.__account = account
        self.__category = category
        self.__amount = amount
        self.__description =description
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value:id):
        self.__id = value

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, value:date):
        self.__date = value

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, value:type):
        self.__type = value

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
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, value):
        if value > 0:
            self.__amount = value
        else:
            raise ValueError("Money must be a positive value")

    @property 
    def description(self):
        return self.__description
    @description.setter
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
