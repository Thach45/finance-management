from datetime import datetime
from calendar import monthrange

def get_loan_due_dates(loans):
    # Hàm để tính số ngày còn lại đến hạn trả nợ của từng khoản vay
    loan_due_dates = []

    current_date = datetime.now()
    current_year = current_date.year
    current_month = current_date.month

    for loan in loans:
        due_date_str = loan['due_date']  # Ngày đến hạn của khoản vay
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')

        # Kiểm tra nếu ngày đến hạn nằm trong tháng và năm hiện tại
        if due_date.year == current_year and due_date.month == current_month:
            # Tính số ngày còn lại hoặc quá hạn
            days_left = (due_date - current_date).days

            loan_due_dates.append({
                'loan_id': loan['_id'],  # ID khoản vay
                'amount_due': loan['amount'],  # Số tiền cần trả
                'days_left': days_left,  # Số ngày còn lại đến hạn
                'due_date': due_date_str  # Ngày đến hạn
            })

    # Sắp xếp danh sách các khoản vay theo số ngày còn lại đến hạn
    loan_due_dates.sort(key=lambda x: x['days_left'])

    # Trả về khoản vay có ngày đến hạn gần nhất trong tháng này (nếu có)
    return loan_due_dates[0] if loan_due_dates else None



def compare_loan_debt(loans):
    # Lấy ngày hiện tại
    current_date = datetime.now()
    current_year = current_date.year
    current_month = current_date.month

    # Tính tháng trước
    if current_month == 1:
        last_month = 12
        last_month_year = current_year - 1
    else:
        last_month = current_month - 1
        last_month_year = current_year

    # Lọc các khoản vay trong tháng hiện tại và tháng trước
    current_month_loans = []
    last_month_loans = []
    
    for loan in loans:
        due_date_str = loan['loan_date']
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')

        # Kiểm tra nếu ngày đến hạn nằm trong tháng hiện tại
        if due_date.year == current_year and due_date.month == current_month:
            current_month_loans.append(loan)

        # Kiểm tra nếu ngày đến hạn nằm trong tháng trước
        elif due_date.year == last_month_year and due_date.month == last_month:
            last_month_loans.append(loan)

    # Tính tổng nợ của tháng hiện tại
    current_month_debt = sum(float(loan['amount']) for loan in current_month_loans)

    # Tính tổng nợ của tháng trước
    last_month_debt = sum(float(loan['amount']) for loan in last_month_loans)

    if(last_month_debt != 0):
        # So sánh nợ tháng trước và tháng này
        compare = ((current_month_debt - last_month_debt)/last_month_debt)*100
    else:
        compare = float('inf')
    return compare

def compare_lend_debt(lendings):
    # Lấy ngày hiện tại
    current_date = datetime.now()
    current_year = current_date.year
    current_month = current_date.month

    # Tính tháng trước
    if current_month == 1:
        last_month = 12
        last_month_year = current_year - 1
    else:
        last_month = current_month - 1
        last_month_year = current_year

    # Lọc các khoản cho vay trong tháng hiện tại và tháng trước
    current_month_lendings = []
    last_month_lendings = []
    
    for lending in lendings:
        due_date_str = lending['loan_date']
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')

        # Kiểm tra nếu ngày đến hạn nằm trong tháng hiện tại
        if due_date.year == current_year and due_date.month == current_month:
            current_month_lendings.append(lending)

        # Kiểm tra nếu ngày đến hạn nằm trong tháng trước
        elif due_date.year == last_month_year and due_date.month == last_month:
            last_month_lendings.append(lending)

    # Tính tổng nợ của tháng hiện tại (cho vay)
    current_month_lending_debt = sum(float(lending['amount']) for lending in current_month_lendings)

    # Tính tổng nợ của tháng trước (cho vay)
    last_month_lending_debt = sum(float(lending['amount']) for lending in last_month_lendings)
    if last_month_lending_debt != 0:
        # So sánh nợ tháng trước và tháng này
        compare = ((current_month_lending_debt - last_month_lending_debt) / last_month_lending_debt) * 100
    else:
        compare = float('inf')
    return compare

def caculator_interest(data):
    principal = float(data['amount'])
    interest_rate = float(data['interest_rate'])
    interest_type = data['interestType']
    due_date = datetime.strptime(data['due_date'], '%Y-%m-%d')  # Ngày đến hạn, chuyển đổi từ chuỗi thành datetime
    current_date = datetime.strptime(data['loan_date'], '%Y-%m-%d') 
    date_gap = abs(due_date - current_date)
    if interest_type == 'simple':
        # Công thức tính lãi đơn: Lãi = Số tiền vay * Lãi suất * Thời gian (tính theo năm)
        time_in_years = date_gap.days / 365  # Thời gian tính theo năm
        interest = principal * (interest_rate / 100) * (time_in_years)  # Tính lãi đơn
        print(interest)
    elif interest_type == 'compound':
            # Công thức tính lãi kép: A = P * (1 + r/n)^(nt), trong đó n = 1 (lãi kép hàng năm)
        time_in_years = date_gap.days / 365  # Thời gian tính theo năm
        interest = principal * ((1 + interest_rate / 100) ** time_in_years - 1)  # Tính lãi kép
        
    print(interest_type)
    
    return interest

def updated_interest_Loan(loan,data):
    paid = loan['paid']  # Số tiền đã trả
    principal = float(loan['amount'])
    interest_rate = float(loan['interest_rate'])  # Lãi suất
    interest_type = loan['interestType']  # Loại lãi suất (lãi đơn hay lãi kép)
    due_date = datetime.strptime(loan['due_date'], '%Y-%m-%d')  # Ngày đến hạn, chuyển đổi từ chuỗi thành datetime
    current_date = datetime.strptime(data['date'], '%Y-%m-%d')  # Ngày thanh toán, chuyển đổi từ chuỗi thành datetime
    date_gap = abs(due_date - current_date)
    # Tính toán số tiền lãi cần trả dựa trên loại lãi suất (lãi đơn hay lãi kép)
    if interest_type == 'simple':
        # Công thức tính lãi đơn: Lãi = Số tiền vay * Lãi suất * Thời gian (tính theo năm)
        time_in_years = date_gap.days / 365  # Thời gian tính theo năm
        interest = principal * (interest_rate / 100) * time_in_years  # Tính lãi đơn
    elif interest_type == 'compound':
        # Công thức tính lãi kép: A = P * (1 + r/n)^(nt), trong đó n = 1 (lãi kép hàng năm)
        time_in_years = date_gap.days / 365  # Thời gian tính theo năm
        interest = principal * ((1 + interest_rate / 100) ** time_in_years - 1)  # Tính lãi kép
    
    # Tính tổng số tiền cần trả (gồm cả lãi)
    total_due = principal + interest  # Tổng số tiền cần trả (gồm cả lãi)
    total_paid = paid + float(data['amount'])  # Số tiền đã trả cộng thêm số tiền thanh toán hiện tại

    # Cập nhật số tiền còn lại cần phải trả
    remaining_balance = total_due - total_paid  # Số tiền còn lại

    # Chuẩn bị dữ liệu để cập nhật thông tin khoản vay
    updated_loan = {
        "paid": total_paid,  # Cập nhật số tiền đã trả
        "interest": interest,  # Cập nhật số tiền lãi
        "remaining": remaining_balance,  # Cập nhật số tiền còn lại cần trả
        "progress": (total_paid / total_due) * 100  # Tính tỷ lệ tiến độ thanh toán (%)
    }
    return updated_loan