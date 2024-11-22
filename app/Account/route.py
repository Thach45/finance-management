
from . import account_bp
from .home_controller import home
@account_bp.route('/account')
def account_route():
    return home()