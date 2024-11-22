
from . import report_bp
from .home_controller import home
@report_bp.route('/report')
def report_route():
    return home()