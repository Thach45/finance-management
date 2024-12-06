from flask import render_template, current_app, url_for, send_file, request, redirect
from flask import jsonify
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import io
from io import BytesIO
import csv
from io import StringIO

import os
from bson.objectid import ObjectId
from models.models import UserModel

def home():
    transaction_model = list(UserModel().get_transactions({"user_id": ObjectId(request.cookies.get('user_id'))}))
    total_income = sum(transaction["amount"] for transaction in transaction_model if transaction["type"] == "income")
    total_expense = sum(transaction["amount"] for transaction in transaction_model if transaction["type"] == "expense")

    monthly_revenue = {}
    for transaction in transaction_model:
        if transaction["type"] == "income":
            date = transaction["date"]
            month = date.strftime("%Y-%m")
            monthly_revenue[month] = monthly_revenue.get(month, 0) + transaction["amount"]

    return render_template('report.html',
                           total_income=total_income,
                           total_expense=total_expense,
                            monthly_revenue=monthly_revenue
                           )

def download_report():
    # Lấy danh sách giao dịch từ database
    transaction_model = list(UserModel().get_transactions({"user_id": ObjectId(request.cookies.get('user_id'))}))
    
    # Định nghĩa header cho file CSV
    header = ['_id', 'user_id', 'date', 'type', 'account', 'category', 'description', 'amount']
    
    # Tạo thư mục 'downloads' nếu chưa tồn tại
    download_folder = os.path.join(os.getcwd(), 'downloads')
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    # Tạo đường dẫn cho file CSV
    file_path = os.path.join(download_folder, 'transactions.csv')
    
    # Mở file CSV để ghi dữ liệu
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        
        # Ghi tiêu đề vào file CSV
        writer.writeheader()
        
        # Ghi dữ liệu vào file CSV
        for transaction in transaction_model:
            # Chuyển đổi ObjectId thành chuỗi
            transaction['_id'] = str(transaction['_id'])
            
            # Nếu category hoặc description là None, thay thế thành chuỗi rỗng
            transaction['category'] = transaction.get('category', '') or ''
            transaction['description'] = transaction.get('description', '') or ''
            
            # Ghi dữ liệu vào file CSV
            writer.writerow(transaction)
    
    # Trả về file CSV cho người dùng tải về
    return send_file(file_path, as_attachment=True, download_name='transactions.csv')