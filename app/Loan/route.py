
from . import loan_bp
from .home_controller import home
@loan_bp.route('/loan')
def loan_route():
    return home()