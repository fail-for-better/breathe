from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager
# 当文件是被调用着时， __name__的值是模块名，即app
# 当文件是执行者时，__name__的值为 ‘__main__’

db = SQLAlchemy()
login = LoginManager()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config_map[config])
    db.init_app(app)
    login.init_app(app)

    @app.route('/<name>')
    def hello(name):
        return 'Hello, %s' % name
    return app

