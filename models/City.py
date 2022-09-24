from database import db
from sqlalchemy_serializer import SerializerMixin
        
class City(db.Model, SerializerMixin):
    __tablename__ = "city"

    id_city  = db.Column('id_city', db.Integer, autoincrement=True, primary_key=True)
    name = db.Column('Name', db.String(255))
    area = db.Column('Area', db.Float)
    residents = db.relationship('Resident', backref='city')

    def __init__(self, name, area):
        self.name = name
        self.area = area