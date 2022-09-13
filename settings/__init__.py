def settings(app):

    # APP Configurations
    app.config['DEBUG'] = True

    # Database Configurations
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:@localhost/address_card'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    #app.config["SQLALCHEMY_ECHO"] = True