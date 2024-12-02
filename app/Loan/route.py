
from . import loan_bp
from .loan_controller import home, edit_loan, edit_lending,create_loan
@loan_bp.route('/loan')
def loan_route():
    return home()

@loan_bp.route('/edit/loan/<string:id>', methods=['GET'])
def edit_loan_route(id):
    return edit_loan(id)

@loan_bp.route('/edit/lending/<string:id>', methods=['GET'])
def edit_lending_route(id):
    return edit_lending(id)

@loan_bp.route('/loan/create', methods=['POST'])
def create_loan_route():
    return create_loan()