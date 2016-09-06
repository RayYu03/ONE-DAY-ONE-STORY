import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Stay away from me'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = '994'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'onedayonesto@163.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'notforyou911'
    FLASKY_MAIL_SUBJECT_PREFIX = '[ONE DAY ONE STORY]'
    FLASKY_MAIL_SENDER = 'ONE-DAY-ONE-STORY Admin <onedayonesto@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') or 'onedayonesto@163.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
