from flask import render_template
from app import app
from models import Comic

# Routes to create website
# Display all records


@app.route('/')
def index():
    comics = Comic.query.all()
    return render_template('index.html', comics=comics)
