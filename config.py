import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    CSRF_ENABLE = bool(os.getenv("CSRF_ENABLE"))
    SQLALCHEMY_TRACK_MODIFICATIONS = bool(os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS"))


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = bool(os.getenv("DEBUG"))
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') \
                              or "postgresql://postgres:qwerty@localhost:5432/test"


class TestingConfig(Config):
    TESTING = bool(os.getenv("DEBUG"))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///auth/test.db'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///auth/develop.db'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
