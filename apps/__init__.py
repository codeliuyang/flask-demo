from apps.v1 import create_blueprint_v1
from apps.v1.api.city_api import city_api


def register_blueprints(app):
    # 注册版本号，以及蓝图模块
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')
    app.register_blueprint(city_api, url_prefix="/city")
