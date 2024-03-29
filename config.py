import os
from urllib import parse


class Config(object):
    SQL_CONIFG = {
        'type':  os.getenv('MYSQL_TYPE', 'mysql') ,
        'driver': os.getenv('DRIVER ', 'pymysql'),
        'username': os.getenv('DB_USER', ''),
        'password': parse.quote_plus(os.getenv('DB_PASSWORD', '')),
        'host': os.getenv('DB_HOST', ''),
        'port': os.getenv('DB_PORT', 3306),
        'database': os.getenv('DB_NAME', '')
    }
    con_str = '{type}+{driver}://{username}:{password}@{host}:{port}/{database}'
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL') or con_str.format(**SQL_CONIFG)
    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True


class ProductConfig(Config):
    pass


class DevelopConfig(Config):
    DEBUG = True


config_map = {
    'dev': Config,
    'product': ProductConfig
}








