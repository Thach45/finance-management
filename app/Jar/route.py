
from . import jar_bp
from .jar_controller import home
@jar_bp.route('/jar')
def jar_route():
    return home()