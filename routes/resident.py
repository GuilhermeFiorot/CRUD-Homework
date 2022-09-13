from flask import request
from utils.response_api import ResponseJsonApi
from models.Tables import Resident, City
from utils.logger import getLoggerAplication
from utils.databaseFunctions import create, update, delete

log = getLoggerAplication("CRUD - Resident")

def crud_resident(app):
    @app.route("/resident", methods=['POST'])
    def create_resident():
        log.debug("Creating a new resident")
        response = request.get_json()
        if not response:
            return ResponseJsonApi({"Error": "Body is missing arguments {firstName, lastName, placeBirth, dateBirth, email, residentPlace}."}, 400)
        if('firstName' not in response):
            return ResponseJsonApi({"Error": "Body is missing argument {firstName}."}, 400)
        if('lastName' not in response):
            return ResponseJsonApi({"Error": "Body is missing argument {lastName}."}, 400)
        if('placeBirth' not in response):
            return ResponseJsonApi({"Error": "Body is missing argument {placeBirth}."}, 400)
        if('dateBirth' not in response):
            return ResponseJsonApi({"Error": "Body is missing argument {dateBirth}."}, 400)
        if('email' not in response):
            return ResponseJsonApi({"Error": "Body is missing argument {email}."}, 400)
        if('residentPlace' not in response):
            return ResponseJsonApi({"Error": "Body is missing argument {area}."}, 400)
        if('residentPlace' in response):
            city_object = City.query.filter_by(name=response["residentPlace"]).first()
            if city_object == None:
                return ResponseJsonApi("Error: error creating resident, argument residentPlace need to be registred in City!", 400)
        
        resident_object = Resident(firstName = response['firstName'],lastName = response['lastName'], placeBirth = response['placeBirth'], dateBirth = response['dateBirth'], email = response['email'], id_city = city_object.id_city)
        
        if create(resident_object):
            log.debug("Sucess: new resident created!")
            return ResponseJsonApi("Sucess: resident created!", 201)
        else:
            log.debug("Error: error creating resident!")
            return ResponseJsonApi("Error: error creating resident!", 400)
    
    @app.route("/resident", methods=['GET'])
    def read_resident():
        log.debug("Reading informationg about all the residents")
        resident_object = Resident.query.all()
        resident_serial = [value.to_json() for value in resident_object]
        
        return ResponseJsonApi(resident_serial, 200)
    
    @app.route("/resident/<int:id>", methods=['GET'])
    def read_id_resident(id):
        log.debug("Reading informationg about the resident")
        resident_object = Resident.query.filter_by(id_resident=id).all()
        resident_serial = [value.to_json() for value in resident_object]
        
        return ResponseJsonApi(resident_serial, 200)
    
    @app.route("/resident/<int:id>", methods=['PUT'])
    def update_resident(id):
        log.debug("Updating information about the resident")
        resident_object = Resident.query.filter_by(id_resident=id).first()
        response = request.get_json()
        if('firstName' in response):
            resident_object.firstName = response['firstName']
        if('lastName' in response):
            resident_object.lastName = response['lastName']
        if('placeBirth' in response):
            resident_object.placeBirth = response['placeBirth']
        if('dateBirth' in response):
            resident_object.dateBirth = response['dateBirth']
        if('email' in response):
            resident_object.email = response['email']
                
        if update(resident_object):
            log.debug("Sucess: resident updated!")
            return ResponseJsonApi("Sucess: resident updated!", 200)
        else:
            log.debug("Error: failed to update resident!")
            return ResponseJsonApi("Error: failed to update resident!", 400)
            
    @app.route("/resident/<int:id>", methods=['DELETE'])
    def delete_resident(id):
        log.debug("Deleting information about the resident")
        resident_object = Resident.query.filter_by(id_resident=id).first()
        if delete(resident_object):
            log.debug("Sucess: city deleted!")
            return ResponseJsonApi("Sucess: resident deleted!", 200)
        else:
            log.debug("Error: deleting city!")
            return ResponseJsonApi("Error: error deleting resident!", 400)