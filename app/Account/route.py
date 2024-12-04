
from . import account_bp
from .account_controller import home, add_account, delete_account, index_account, edit_account, transfer_account, filter_account
@account_bp.route('/account')
def account_route():
    return home()

@account_bp.route('/account/add/', methods=['POST'])
def add_account_route():
    return add_account()

@account_bp.route('/account/delete/<string:id>',methods=['POST'])
def delete_account_route(id):
    return delete_account(id)

@account_bp.route('/account/edit/<string:id>', methods=['GET'])
def edit_account_index(id):
    return index_account(id)

@account_bp.route('/account/edit/<string:id>', methods=['POST'])
def edit_account_route(id):
    return edit_account(id)

@account_bp.route('/account/transfer',methods=['POST'])
def tranfer_account_route():
    return transfer_account()

@account_bp.route('/account/filter',methods=['GET'])
def filter_route():
    return filter_account()