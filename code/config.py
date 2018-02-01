import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = "wenanguo1"    #os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = "wenanguo123456" #os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = '系统通知-Admin <wenanguo1@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_SLOW_DB_QUERY_TIME = 2
    JOBS_START = True  #是否启动作业
    LOGS_START = True  #是否启动日志

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    JOBS_START = False
    DEBUG = True

    #SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    #                          "mysql+pymysql://root:Matrining81215@586f85cf61241.sh.cdb.myqcloud.com:3759/crpy"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              "mysql+pymysql://root:root@192.168.9.48:3306/pass"


class TestingConfig(Config):
    JOBS_START=False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              "mysql+pymysql://root:Matrining81215@586f85cf61241.sh.cdb.myqcloud.com:3759/crpy"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              "mysql+pymysql://root:Matrining81215@586f85cf61241.sh.cdb.myqcloud.com:3759/crpy"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
