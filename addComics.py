# addComics.py
# Joseph Schmoyer
# Jan 27, 2024
from app import app, db
from models import Comic

if __name__ == '__main__':
    with app.app_context():
        comic1 = Comic(title = "Comic 1",
                       author = "John Smith",
                       artist = "Adam Smith")
        comic2 = Comic(title = "Comic 2",
                       author = "John Smith",
                       artist = "Sarah Conor")
        comic3 = Comic(title = "Comic 3",
                       author = "Jane Doe",
                       artist = "Adam Smith")
        comic4 = Comic(title = "Comic 4",
                       author = "J Doe",
                       artist = "A Smith")
        db.session.add(comic1)
        db.session.add(comic2)
        db.session.add(comic3)
        db.session.add(comic4)
        db.session.commit()
        print(Comic.query.all())