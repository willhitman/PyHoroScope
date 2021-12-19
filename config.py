from distutils.debug import DEBUG
from email.policy import default
from msilib.schema import Class
from decouple import config


class Config(object):
    SECRET_KEY = config('SECRET_KEY', default = 'guess-me')
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True


class ProductionConfig(Config):
    DEBUG = False
    MAIL_DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

# created a config class and defined various attributes inside it
# created various different child(sub classes as per each stage in development) that inherit the config class. 

