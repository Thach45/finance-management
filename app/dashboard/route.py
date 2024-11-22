
from . import home_bp
from .home_controller import home
@home_bp.route('/home')
def home_route():
    return home()