from flask import Blueprint
from db_ext import db
from apps.v1.models.city import City

city_api = Blueprint('city_api', __name__)

@city_api.route("/blueprint")
def get_city():
    city = db.session.query(City).first()
    return str(city.name) + " blue_print"
