
from . import report_bp
from .home_controller import home, download_report
@report_bp.route('/report')
def report_route():
    return home()
@report_bp.route('/report/download')
def download():
    return download_report()