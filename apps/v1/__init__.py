from flask import Blueprint
from flask_restful import Api
from apps.v1.api.city_resource import CityResource


def register_views(app):
    api = Api(app)
    api.add_resource(CityResource, '/city', endpoint='city')


def create_blueprint_v1():
    """
    注册蓝图->v1版本
    """
    bp_v1 = Blueprint('v1', __name__)
    register_views(bp_v1)
    return bp_v1