Welcome

This is my API project to solve the Cities and Residents homework.

The API was build in Python using Flask as Framework, SQLAlchemy as ORM and MySQL as Database, this is the structure that i use to build.

crud-api-homework/
         database/
            __init__.py
        models/
            Tables.py
        routes/
            city.py
	resident.py
	error.py
       settings/
            __init__.py
       tests/
            tests.py
       utils/
            databaseFunctions.py
	logger.py
	response_api.py
       app.py
       dependencies.txt
       readme.txt
       CRUD API - Requests.postman_collection.json

Tthere, we split the code into 6 main parts:

The models are the data descriptor of my application, the database model.
The routes are the URIs to my application, where we define our resources and actions.
The database are the definitions for my database engine SQLAlchemy.
The settings are the definitions for my APP and Database as well.
The utils are modules that define application logic or interact with other services or the db layer.
The tests are the unit tests to my application.

Postman documentation:
https://documenter.getpostman.com/view/17990352/2s7YYsdQ5q

To start the API you need to follow this steps.

1º Step - Create the Environment
python -m venv env
or
python3 -m venv env


2º Step - Activate the Environment
.\env\Scripts\activate.bat

if you want to exit is just type 
deactivate
in to the console.


3º Step - Upgrade pip and Install the dependencies
python -m pip install --upgrade pip
or
python3 -m pip install --upgrade pip

python -m pip install -r dependencies.txt
or
python3 -m pip install -r dependencies.txt


4º Step - Start the API
python app.py
or
python3 app.py


5º Step - Need to go to settings/__init__.py to set up for database configurations
MAKE SURE TO CREATE THE SCHEMA ON THE DATABASE!
I was using the XAMPP + phpMyAdmin for this, so by default is going like this.

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:@localhost/address_card


6º Step - Create the tables for the application

For creating the tables just use the API_IP/create_tables as a get request and its done.


7º Step - Is ready to use the routes

Just go creating, reading, updating or deleting cities and there residents.
