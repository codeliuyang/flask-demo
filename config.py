'''
多环境的配置文件如下
'''

import os
basedir = os.path.abspath(os.path.dirname(__file__))


# 基础配置类，所有环境皆通用的类
class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'some secret words')
    ITEMS_PER_PAGE = 10


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1qazxsw2@localhost:3306/pydb?charset=utf8mb4'
    # 打印SQL日志
    SQLALCHEMY_ECHO = True


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_ECHO = True


config = {
    'dev': DevelopmentConfig,
    'sit': TestingConfig,
    'default': DevelopmentConfig
}
