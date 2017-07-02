from config import config
from flask import Flask
from flask_bootstrap import Bootstrap


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    _register_blueprint(app)
    _decorate_app(app)

    return app


def _register_blueprint(app):
    from app.blueprints.home_blueprint import home_blueprint

    app.register_blueprint(home_blueprint)


def _decorate_app(app):
    bootstrap = Bootstrap()
    bootstrap.init_app(app)
