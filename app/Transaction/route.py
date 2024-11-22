
from . import transaction_bp
from .home_controller import home
@transaction_bp.route('/transaction')
def transaction_route():
    return home()