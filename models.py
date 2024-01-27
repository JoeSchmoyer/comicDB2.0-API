from extensions import db

# Tables for database
class Comic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    publisher = db.Column(db.String(32))
    author = db.Column(db.String(32), nullable=False)
    artist = db.Column(db.String(32), nullable=False)
    publication_date = db.Column(db.String(40))
    completed = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<Comic {self.title}>'

