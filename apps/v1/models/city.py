from db_ext import db


class City(db.Model):
    __table__name = 'resources'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
