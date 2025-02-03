from flask import Flask


#here we are importing our orm for database
from flask_sqlalchemy import SQLAlchemy

#lib responsible for data migration
from flask_migrate import Migrate


#instance of our databse
db = SQLAlchemy()


#method which return a flask rapp
def create_app():
    flask_app = Flask(__name__)
    #config for our app to find database
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./users.db'

    #integrating our app with database
    migrate = Migrate(flask_app, db)
    db.init_app(flask_app)

    return flask_app