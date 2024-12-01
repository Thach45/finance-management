
from . import transaction_bp
from .transaction_controller import home, edit_transaction
@transaction_bp.route('/transaction')
def transaction_route():
    return home()

@transaction_bp.route('/transaction/edit/<string:transaction_id>', methods=['GET'])
def edit_transaction_route(transaction_id):
    return edit_transaction(transaction_id)

# @transaction_bp.route('/transaction/edit', methods=['POST'])
# # def edit_transaction_post_route():
# #     return edit_transaction_post()