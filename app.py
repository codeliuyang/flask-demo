from flask import Flask, Response
from apps import register_blueprints
from db_ext import db
from config import config
from log_config import log_format
import json

flask_app = Flask(__name__)

# 如果单独设置环境参数，则如下设置
# flask_app.config["SQLALCHEMY_ECHO"] = True # 设置SQL日志是否打印

# 获取相应环境的配置类
flask_app.config.from_object(config['dev'])


def init_app(app):
    register_blueprints(app)
    db.init_app(app)


# 初始化app时进行的动作
init_app(flask_app)


# 全局异常处理
@flask_app.errorhandler(Exception)
def handle_exception():
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    # replace the body with JSON
    return Response(json.dumps({
        "code": "1",
        "name": "2",
        "description": "3",
    }), mimetype="application/json")


'''默认最简单的启动脚本是flask_app.run()
如果想要信任其他的访问，则为flask_app.run(host='0.0.0.0')
'''
if __name__ == '__main__':
    # 配置日志
    log_format(flask_app)
    # flask_app.run()
    flask_app.run(host='0.0.0.0')
