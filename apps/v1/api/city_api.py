'''
以下为使用常规的API形式进行开发
'''
from flask import Blueprint
from db_ext import db
from apps.v1.models.city import City

# 声明为蓝图
city_api = Blueprint('city_api', __name__)


# 某个API开发
@city_api.route("/<city_id>", methods=['GET'])
def get_city_by_id(city_id):
    print("you need to query city_id =", str(city_id))
    city = City.query.filter_by(id=city_id).first()
    return "query success" + str(city.id)


@city_api.route("/<city_id>", methods=['DELETE'])
def delete_city_by_id(city_id):
    print("you will delete, city_id =", str(city_id))
    city = City.query.filter_by(id=city_id).first()
    db.session.delete(city)
    db.session.commit()
    return "delete success"


@city_api.route("/<city_id>", methods=['PUT'])
def update_city_by_id(city_id):
    city = City.query.filter_by(id=city_id).first()
    city.name = '上海'
    db.session.commit()
    return "update success"


@city_api.route("", methods=['POST'])
def add_city():
    city = City(99887766, '上海', 'PVG', 'CHINA', '12')
    db.session.add(city)
    db.session.commit()
    return "add success"
