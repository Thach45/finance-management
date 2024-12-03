from flask import render_template, current_app, url_for
from flask import jsonify
from models.user import User

user1 = User()
user1.get_account()
for account in user1.accountss:
    print(account['name'])
def home():
    pass
