# resources.py
# Joseph Schmoyer
# Jan 27, 2024
from flask_restx import Resource, Namespace
from api_models import comic_model, comic_import_model
from models import Comic
from extensions import db

#Create a namespace for the API
ns = Namespace("api")

#Add/View comics (No input parameters but may be a payload)
@ns.route("/Comic")
class Comic_API_Add_View(Resource):

    # Retrieve entire database
    @ns.marshal_list_with(comic_model)
    def get(self):
        return Comic.query.all()

    # Add a comic to the database
    @ns.expect(comic_import_model)
    def post(self):
        print(ns.payload)
        input_comic = Comic(title=ns.payload["title"],
                            publisher=ns.payload["publisher"],
                            author=ns.payload["author"],
                            artist=ns.payload["artist"],
                            publication_date=ns.payload["publication_date"],
                            completed=ns.payload["completed"])
        db.session.add(input_comic)
        db.session.commit()
        return {}, 201

# Edit/Remove comics (id input parameter required)
@ns.route("/Comic/<int:id>")
class Comic_Api_Edit_Remove(Resource):

    #Delete a comic from the database
    def delete(self, id):
        Comic.query.filter_by(id=id).delete()
        db.session.commit()
        return {}, 204
