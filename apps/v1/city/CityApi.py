from flask_restful import Resource

from apps.v1.models.City import City
from db_ext import db


class City(Resource):
    def get(self):
        # return {"aa": "123"}
        first_city = db.session.query(City).first()
        return {"cityname": first_city.name}
