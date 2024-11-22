
from . import dashboard_bp
from .home_controller import home
@dashboard_bp.route('/dashboard')
def dashboard_route():
    return home()