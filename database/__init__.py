from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def database(app):
    db.init_app(app)
