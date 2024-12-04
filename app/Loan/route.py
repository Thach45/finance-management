
from . import loan_bp
from .loan_controller import home, edit_loan,add_loan, payment_loan, edit_loan_post, payment_loan_post,delete_loan
from .loan_controller import  add_lend,edit_lending,edit_lend_post,delete_lend
@loan_bp.route('/loan')
def loan_route():
    return home()

@loan_bp.route('/edit/loan/<string:id>', methods=['GET'])
def edit_loan_route(id):
    return edit_loan(id)

@loan_bp.route('/edit/lending/<string:id>', methods=['GET'])
def edit_lending_route(id):
    return edit_lending(id)

@loan_bp.route('/payment/loan/<string:id>', methods=['GET'])
def payment_loan_route(id):
    return payment_loan(id)

@loan_bp.route('/loan/create', methods=['POST'])
def add_loan_route():
    return add_loan()

@loan_bp.route('/edit/loan/<string:id>', methods=['POST'])
def edit_loan_post_route(id):
    return edit_loan_post(id)

@loan_bp.route('/lending/create', methods=['POST'])
def add_lend_route():
    return add_lend()

@loan_bp.route('/edit/lending/<string:id>', methods=['POST'])
def edit_lend_post_route(id):
    return edit_lend_post(id)

@loan_bp.route('/payment/loan/<string:id>', methods=['POST'])
def payment_loan_post_route(id):
    return payment_loan_post(id)

@loan_bp.route('/loan/delete/<string:id>', methods=['POST'])
def delete_loan_route(id):
    return delete_loan(id)

@loan_bp.route('/lending/delete/<string:id>', methods=['POST'])
def delete_lend_route(id):
    return delete_lend(id)
