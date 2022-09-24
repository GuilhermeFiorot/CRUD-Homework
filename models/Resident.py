from database import db
from sqlalchemy_serializer import SerializerMixin

class Resident(db.Model, SerializerMixin):
    __tablename__ = "resident"

    id_resident  = db.Column('id_resident', db.Integer, autoincrement=True, primary_key=True)
    firstName = db.Column('firstName', db.String(255))
    lastName = db.Column('lastName', db.String(255))
    placeBirth = db.Column('placeBirth', db.String(255))
    dateBirth = db.Column('dateBirth', db.Date)
    email = db.Column('email', db.String(255))
    id_city = db.Column(db.Integer, db.ForeignKey('city.id_city'), nullable=False)
    
    def __init__(self, firstName, lastName, placeBirth, dateBirth, email, id_city):
        self.firstName = firstName
        self.lastName = lastName
        self.placeBirth = placeBirth
        self.dateBirth = dateBirth
        self.email = email
        self.id_city = id_city
    
    def to_json(self):
        return {"id_resident": self.id_resident, 
                "firstName": self.firstName, 
                "lastName": self.lastName, 
                "placeBirth": self.placeBirth,
                "dateBirth": str(self.dateBirth),
                "email": self.email,
                "id_city": self.id_city
                }