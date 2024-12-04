from . import transaction_bp
from .transaction_controller import home, add_transaction, delete_transaction, edit_transaction
@transaction_bp.route('/transaction')
def transaction_route():
    return home()

@transaction_bp.route('/transaction/add', methods=['POST'])
def add_transaction_route():
    return add_transaction()

@transaction_bp.route('/transaction/delete/<string:id>', methods=['POST'])
def delete_transaction_route(id):
    return delete_transaction(id)

@transaction_bp.route('/transaction/edit/<string:transaction_id>', methods=['GET', 'POST'])
def edit_transaction_route(transaction_id):
    return edit_transaction(transaction_id)



