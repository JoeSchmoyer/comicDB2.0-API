# extensions.py
# Joseph Schmoyer
# Jan 27, 2024
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

# Instance for database and api
api = Api()
db = SQLAlchemy()
