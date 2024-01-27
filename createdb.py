# createdb.py
# Joseph Schmoyer
# Jan 27, 2024
from extensions import db
from app import app
from models import Comic

with app.app_context():
    #IF you want to clear original database
    #db.drop_all()
    db.create_all()
    #Create an inital test comic
    comic = Comic(title="testComic", author="testAuthor", artist="testArtist")
    db.session.add(comic)
    db.session.commit()
    #print database entries
    print(Comic.query.all())