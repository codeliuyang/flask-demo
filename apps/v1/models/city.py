from db_ext import db


class City(db.Model):
    __table__name = 'city'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35))
    country_code = db.Column(db.String(3))
    district = db.Column(db.String(20))
    population = db.Column(db.String(11))

    def __init__(self, id, name, country_code, district, population):
        self.id = id
        self.name = name
        self.country_code = country_code
        self.district = district
        self.population = population

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "country_code": self.country_code,
            "district": self.district
        }
