from flask import Flask
from apps import register_blueprints
from db_ext import db

flask_app = Flask(__name__)

flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1qazxsw2@localhost:3306/world'


def init_app(app):
    register_blueprints(app)
    db.init_app(app)

init_app(flask_app)


if __name__ == '__main__':
    flask_app.run()
