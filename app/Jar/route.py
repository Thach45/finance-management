
from . import jar_bp
from .jar_controller import home, delete
@jar_bp.route('/jar')
def jar_route():
    return home()

@jar_bp.route('/jar/delete/<string:id>')
def add_jar_route(id):
    return delete(id)