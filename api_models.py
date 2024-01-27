from flask_restx import fields
from extensions import api

comic_model = api.model("Comic", {
    "id": fields.Integer,
    "title": fields.String,
    "publisher": fields.String,
    "author": fields.String,
    "artist": fields.String,
    "publication_date": fields.Date,
    "completed": fields.Boolean
})

comic_import_model = api.model("ComicInput", {
    "title": fields.String,
    "publisher": fields.String,
    "author": fields.String,
    "artist": fields.String,
    "publication_date": fields.String,
    "completed": fields.Boolean
})
