import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))
    DEBUG = False
    CSRF_ENABLED = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'production': ProductionConfig
}
