from transaction import Transaction
from account import Account
from category import Category
from datetime import date

class Credit():
    def __init__(self,id,type,crediter,amount,interest_rate,interes_type,credit_date,
                 due_date,contact,paid,interest,remaining,progress,description):
        self.__type = id
        self.__type = type
        self.__crediter = crediter
        self.__amount = amount
        self.__interest_rate = interest_rate
        self.__interest_type = interes_type
        self.__due_date = credit_date
        self.__due_date = due_date
        self.__contact = contact
        self.__progress = paid
        self.__interest = interest
        self.__remaining = remaining
        self.__progress = progress
        self.__description = description

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id = value

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self,value):
        self.__type = value

    @property
    def crediter(self):
        return self.__crediter
    @crediter.setter
    def crediter(self,value):
        self.__crediter = value

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self,value):
        if value >= 0:
            self.__amount = value
        return False

    @property
    def interest_rate(self):
        return self.__interest_rate
    @interest_rate.setter
    def interest_rate(self,value):
        if value >= 0:
            self.__interest_rate = value
        else:
            return False
    @property
    def interest_type(self):
        return self.__interest_type
    @interest_type.setter
    def interest_type(self,value):
        self.__interest_type = value

    @property
    def credit_date(self):
        return self.__credit_date
    @credit_date.setter
    def credit_date(self,value):
        self.__credit_date = value

    @property
    def due_date(self):
        return self.__due_date
    @due_date.setter
    def due_date(self,value):
        self.__due_date = value

    @property
    def contact(self):
        return self.__contact
    @contact.setter
    def contact(self,value):
        self.__contact = value

    @property
    def paid(self):
        return self.__paid
    @paid.setter
    def paid(self,value):
        if value >=0 :
            self.__paid = value
        else:
            return False

    @property
    def interest(self):
        return self.__interest
    @interest.setter
    def interest(self,value):
        if value>=0 :
            self.__interest = value
        else: 
            return False

    @property
    def remaining(self):
        return self.__remaining
    @remaining.setter
    def remaining(self,value):
        if value>=0 :
            self.__remaining = value
        else:
            return False

    @property
    def progress(self):
        return self.__progress
    @progress.setter
    def progress(self,value):
        if value>=0 :
            self.__progress = value
        else:
            return False

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self,value):
        self.__description = value

    

