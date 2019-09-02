'''这个模块的写法是使用flask_restful进行开发
完全遵循RESTful里对于资源的概念
'''
from flask_restful import Resource
from apps.v1.models.city import City
from db_ext import db


class CityResource(Resource):

    def get(self):
        # return {"aa": "123"}
        first_city = db.session.query(City).first()
        return {"cityname": first_city.name}

    def put(self):
        # put操作方法
        return ""

    def post(self):
        # post操作
        return ""

    def delete(self):
        # delete操作
        return ""

