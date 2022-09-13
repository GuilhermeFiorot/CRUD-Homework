from flask import request
from utils.response_api import ResponseJsonApi
from models.Tables import City
from utils.logger import getLoggerAplication
from utils.databaseFunctions import create, update, delete

log = getLoggerAplication("CRUD - City")

def crud_city(app):
    @app.route("/city", methods=['POST'])
    def create_city():
        log.debug("Creating a new city...")
        response = request.get_json()
        if not response:
            return ResponseJsonApi({"Error": "Body is missing arguments {name, area}."}, 400)
        if('name' not in response):
            return ResponseJsonApi({"Error": "Body is missing argument {name}."}, 400)
        if('area' not in response):
            return ResponseJsonApi({"Error": "Body is missing argument {area}."}, 400)
         
        city_object = City(name = response["name"], area = response["area"])
        
        if create(city_object):
            log.debug("Sucess: new city created!")
            return ResponseJsonApi("Sucess: city created!", 201)
        else:
            return ResponseJsonApi("Error: error creating city!", 400)
    
    @app.route("/city", methods=['GET'])
    def read_city():
        log.debug("Reading informationg about all the citys...")
        city_object = City.query.all()
        city_serial = [value.to_dict() for value in city_object]
        
        return ResponseJsonApi(city_serial, 200)
    
    @app.route("/city/<int:id>", methods=['GET'])
    def read_id_city(id):
        log.debug("Reading informationg about the city...")
        city_object = City.query.filter_by(id_city=id).all()
        city_serial = [value.to_dict() for value in city_object]
        
        return ResponseJsonApi(city_serial, 200)
    
    @app.route("/city/<int:id>", methods=['PUT'])
    def update_city(id):
        log.debug("Updating informations about the city...")
        city_object = City.query.filter_by(id_city=id).first()
        response = request.get_json()
        if not response:
            return ResponseJsonApi({"error": "Erro doesn't have body."}, 400)
        if('name' in response):
            city_object.name = response['name']
        if('area' in response):
            city_object.area = response['area']
        
        if update(city_object):
            log.debug("Sucess: city updated!")
            return ResponseJsonApi("Sucess: city updated!", 200)
        else:
            log.debug("Error: updating city!")
            return ResponseJsonApi("Error: error updating city!", 400)
        
    @app.route("/city/<int:id>", methods=['DELETE'])
    def delete_city(id):
        log.debug("Deleting information about the City...")
        city_object = City.query.filter_by(id_city=id).first()
        if delete(city_object):
            log.debug("Sucess: city deleted!")
            return ResponseJsonApi("Sucess: city deleted!", 200)
        else:
            log.debug("Error: deleting city!")
            return ResponseJsonApi("Error: error deleting city!", 400)