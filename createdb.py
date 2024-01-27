from extensions import db
from app import app
from models import Comic

with app.app_context():
    #IF you want to clear original database
    #db.drop_all()
    db.create_all()
    comic = Comic(title="testComic", author="testAuthor", artist="testArtist")
    db.session.add(comic)
    db.session.commit()
    print(Comic.query.all())