from flask import Flask, Response
from flask_cors import CORS
from utils.logger import settingsColor
from database import db

# Imports we need
from routes import error, city, resident
from settings import settings
from database import database

app = Flask(__name__)
CORS(app)

# App configurations
settingsColor() # Colors to Logs (esay to understand whats happening in the terminal).
settings(app) # App General Configuration
database(app) # Initialize Database Configurations

# Tables Creation
@app.route("/create_tables", methods=['GET'])
def create_tables():
    db.create_all()
    return ("Sucess: tables created!")

# Routes
error.Error(app)
city.crud_city(app)
resident.crud_resident(app)

if __name__ == "__main__":
    app.run(host = '0.0.0.0',)