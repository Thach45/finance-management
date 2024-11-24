
from . import account_bp
from .account_controller import home, add_account
@account_bp.route('/account')
def account_route():
    return home()

@account_bp.route('/account/add', methods=['POST'])
def add_account_route():
    return add_account()