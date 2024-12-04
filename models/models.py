from flask_pymongo import PyMongo
from flask import current_app
from flask import request
from bson.objectid import ObjectId
class UserModel:
    def __init__(self):
        self.mongo = current_app.config['MONGO']
    # Account
    def get_account(self, account_id={}):
        return self.mongo.db.accounts.find(account_id)

    def create_account(self, account_data):
        return self.mongo.db.accounts.insert_one(account_data)
    
    def update_account(self, account_id, account_data):
        return self.mongo.db.accounts.update_one({"_id": account_id}, {"$set": account_data})
    
    def delete_account(self, account_id):
        return self.mongo.db.accounts.delete_one({"_id": account_id})
    
    # Auth
    def get_auth(self, auth_data):
        return self.mongo.db.auth.find_one(auth_data)
    
    def create_auth(self, auth_data):
        return self.mongo.db.auth.insert_one(auth_data)
    
    # Transactions
    def get_transactions(self, account_id={}):
        return self.mongo.db.transaction.find(account_id)

    
    def create_transaction(self, transaction_data):
        return self.mongo.db.transaction.insert_one(transaction_data)
    
    def update_transaction(self, transaction_id, transaction_data):
        return self.mongo.db.transaction.update_one({"_id": ObjectId(transaction_id)}, {"$set": transaction_data})
    
    def delete_transaction(self, transaction_id):
        return self.mongo.db.transaction.delete_one({"_id":ObjectId(transaction_id)})
    
    # Loans
    def get_loans(self, loan_id={}):
        return self.mongo.db.loan.find(loan_id)
    
    def create_loan(self, loan_data):
        return self.mongo.db.loan.insert_one(loan_data)
    
    def update_loan(self, loan_id, loan_data):
        return self.mongo.db.loan.update_one({"_id": loan_id}, {"$set": loan_data})
    
    def delete_loan(self, loan_id):
        return self.mongo.db.loan.delete_one({"_id": loan_id})
    # Lendings
    def get_lendings(self, lending_id={}):
        return self.mongo.db.lendings.find(lending_id)
    
    def create_lending(self, lending_data):
        return self.mongo.db.lendings.insert_one(lending_data)
    
    def update_lending(self, lending_id, lending_data):
        return self.mongo.db.lendings.update_one({"_id": lending_id}, {"$set": lending_data})
    
    def delete_lending(self, lending_id):
        return self.mongo.db.lendings.delete_one({"_id": lending_id})
    
    # Jars
    def get_jars(self, jar_id={}):
        return self.mongo.db.jar.find(jar_id)
    def create_jar(self, jar_data):
        return self.mongo.db.jar.insert_one(jar_data)
    def delete_jar(self, jar_id):
        return self.mongo.db.jar.delete_many({"idJar": jar_id,
                                              "user_id": ObjectId(request.cookies.get('user_id'))})
    
    #total
    def get_total(self):
        return self.mongo.db.total.find_one({"user_id": ObjectId(request.cookies.get('user_id'))})
    def update_total(self, total_data):
        return self.mongo.db.total.update_one(
            {"user_id": ObjectId(request.cookies.get('user_id'))},
            {"$set": total_data},
            upsert=True
        )