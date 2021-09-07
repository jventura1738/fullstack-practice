# Justin Ventura
from flask import Flask


# Creates app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jenna sleeps on the floor'

    from .views import views
    from .auth import auth

    # Need this for views & auth to work on page:
    app.register_blueprint(views, url_prefix='/')  # No prefix.
    app.register_blueprint(auth, url_prefix='/')

    return app
