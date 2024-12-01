
from . import auth_bp
from .auth_controller import home, login, register, register_post
@auth_bp.route('/')
def auth_route():
    return home()

@auth_bp.route('/register', methods=['GET'])
def register_route():
    return register()


@auth_bp.route('/register', methods=['POST'])
def register_post_route():
    return register_post()


@auth_bp.route('/login', methods=['POST'])
def login_route():
    return login()