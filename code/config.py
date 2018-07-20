import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    #session配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    #数据库配置
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_SLOW_DB_QUERY_TIME = 2

    #邮件配置
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = "wenanguo1"    #os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = "wenanguo123456" #os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = '系统通知-Admin <wenanguo1@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')




    #其他配置
    JOBS_START = True  #是否启动作业
    LOGS_START = True  #是否启动日志

    DEBUG = False
    TESTING = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    JOBS_START = True
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              "mysql+pymysql://root:wenanguo@192.168.9.48:32767/pyfw"


class TestingConfig(Config):
    JOBS_START=False
    TESTING = True

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              "mysql+pymysql://root:wenanguo@192.168.9.48:32767/pyfw"

class ProductionConfig(Config):
    JOBS_START = True


    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              "mysql+pymysql://root:wenanguo@192.168.9.48:32767/pyfw"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
