from extensions import db
from app import app
from models import Comic

with app.app_context():
    db.drop_all()
    db.create_all()
    comic = Comic(title="testComic", author="testAuthor", artist="testArtist")
    db.session.add(comic)
    db.session.commit()
    print(Comic.query.all())