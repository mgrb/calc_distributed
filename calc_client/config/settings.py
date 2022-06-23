class BaseConfig():
    API_PREFIX = '/api'
    TESTING = False
    DEBUG = False


class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://cer_cft_timer:Qwert123@localhost:5432/cer_cft'
    CELERY_BROKER = 'pyamqp://cer_user:Qwert123@localhost//'
    RESULT_BECKEND = 'rpc://cer_user:Qwert123@localhost//'


class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_password@db-postgres:5432/flask-deploy'
    CELERY_BROKER = 'pyamqp://rabbit_user:rabbit_password@broker-rabbitmq//'
    RESULT_BECKEND = 'rpc://rabbit_user:rabbit_password@broker-rabbitmq//'


class TestConfig(BaseConfig):
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True
    # make celery execute tasks synchronously in the same process
    CELERY_ALWAYS_EAGER = True
