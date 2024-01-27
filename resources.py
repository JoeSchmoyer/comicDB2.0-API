import locale
from datetime import datetime
from flask_restx import Resource, Namespace
from api_models import comic_model, comic_import_model
from models import Comic
from extensions import db
from datetime import datetime

ns = Namespace("api")


@ns.route("/Comic")
class Comic_API_Add_View(Resource):
    @ns.marshal_list_with(comic_model)
    def get(self):
        return Comic.query.all()

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


@ns.route("/Comic/<int:id>")
class Comic_Api_Edit_Remove(Resource):
    def delete(self, id):
        Comic.query.filter_by(id=id).delete()
        db.session.commit()
        return {}, 204
