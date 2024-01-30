# api_models.py
# Joseph Schmoyer
# Jan 27, 2024

from flask_restx import fields
from extensions import api

#Output model for comic
comic_model = api.model("Comic", {
    "id": fields.Integer,
    "title": fields.String,
    "publisher": fields.String,
    "author": fields.String,
    "artist": fields.String,
    "publication_date": fields.String,
    "completed": fields.Boolean
})

#Input model for comic
comic_import_model = api.model("ComicInput", {
    "title": fields.String,
    "publisher": fields.String,
    "author": fields.String,
    "artist": fields.String,
    "publication_date": fields.String,
    "completed": fields.Boolean
})
