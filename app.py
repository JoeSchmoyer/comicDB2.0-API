# app.py
# Joseph Schmoyer
# Jan 27, 2024

from flask import Flask
from extensions import api, db
from resources import ns
# Creating the app
app = Flask(__name__)
#Establish database type
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '450333370bd0e313582615466fe97460a0b8355a067b46738a9a4c517dfc228d'

#Initalize api and database with the app
api.init_app(app)
db.init_app(app)

#add ns to api namespace list links api with resources
api.add_namespace(ns)

# Import the routes before running the application otherwise page won't display
from routes import *


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
