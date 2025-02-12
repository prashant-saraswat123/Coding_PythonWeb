from flask import Flask


#here we are importing our orm for database
from flask_sqlalchemy import SQLAlchemy

#lib responsible for data migration
from flask_migrate import Migrate


#instance of our databse
db = SQLAlchemy()


#method which return a flask app
def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    #config for our app to find database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./users.db'

    #integrating our app with database
    migrate = Migrate(app, db)
    db.init_app(app)

    from view import register_request
    register_request(app, db)

    migrate = Migrate(app, db)

    return app