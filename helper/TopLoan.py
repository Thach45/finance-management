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
