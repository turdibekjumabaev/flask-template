from flask import Flask, Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return "Hello, Flask Template!"

def init_routes(app: Flask):
    app.register_blueprint(main_bp)
