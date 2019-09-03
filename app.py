from flask import Flask
from apps import register_blueprints
from db_ext import db

flask_app = Flask(__name__)

# 设置Database的URL，写明charset，建议为utf8mb4
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1qazxsw2@localhost:3306/pydb?charset=utf8mb4'
# 设置Database的SQL打印
flask_app.config["SQLALCHEMY_ECHO"] = True


def init_app(app):
    register_blueprints(app)
    db.init_app(app)


# 初始化app时进行的动作
init_app(flask_app)


'''默认最简单的启动脚本是flask_app.run()
如果想要信任其他的访问，则为flask_app.run(host='0.0.0.0')
'''
if __name__ == '__main__':
    # flask_app.run()
    flask_app.run(host='0.0.0.0', debug=True)

