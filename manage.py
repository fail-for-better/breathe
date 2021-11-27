from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from flask_script import Manager, Server, Command

from app import create_app, db


app = create_app('dev')
manager = Manager(app)
migrate = Migrate(app, db)
login = LoginManager()
manager.add_command('db', MigrateCommand)


manager.add_command('runserver', Server(
    host='0.0.0.0', port=8000, use_debugger=True
))

@app.route('/')
def test():
    return "wangbo"


# if __name__ == '__main__':
#     app.run(debug=True)

