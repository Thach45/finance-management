from flask import render_template, current_app, url_for, send_file
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import io
from models.models import UserModel

def home():
    user = UserModel()
    transactions = user.get_transactions()
    # total_income = sum([transaction['amount'] for transaction in transactions if transaction['type'] == 'income'])
    # total_expense = sum([transaction['amount'] for transaction in transactions if transaction['type'] == 'expense'])
    total_income = 0
    total_expense = 0
    distribution_category = {}
    for transaction in transactions:
        if transaction['type'] == 'income':
            total_income+=float(transaction['amount'])
        elif transaction['type'] == 'expense':
            total_expense+=float(transaction['amount'])
        if transaction['category'] not in distribution_category.keys():
            distribution_category.update({transaction['category']:int(transaction['amount'])})
        else:
            distribution_category[transaction['category']] += int(transaction['amount'])
    total_profit = total_income - total_expense
    
        

    categorys = list(distribution_category.keys())
    money_of_category = list(distribution_category.values())
    print(categorys)
    print(money_of_category)
    #Lưu biểu đồ
    color_hex_list = [
    "#FF9999", "#66B3FF", "#99FF99", "#FFCC99", "#C299FF", 
    "#FFB3E6", "#D3D3D3", "#FFA07A", "#40E0D0", "#FFD700", 
    "#ADFF2F", "#7B68EE", "#FF6347", "#00CED1", "#FFDAB9"]

    explode = [0.015]*len(categorys)

    fig,ax = plt.subplots()
    ax.pie(money_of_category,labels=categorys,autopct='%1.1f%%',
           colors=color_hex_list,explode=explode)
    ax.set(title = 'Cơ cấu chi phí theo danh mục')
    fig.savefig('pieCategory.png')

    return render_template('report.html',
                           total_income=total_income,
                           total_expense=total_expense,
                           total_profit=total_profit)
