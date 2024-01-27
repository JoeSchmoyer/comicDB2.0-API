# routes.py
# Joseph Schmoyer
# Jan 27, 2024
from flask import render_template
from app import app
from models import Comic

# Routes to do basic webpage (overwritten with api)
# Display all records


@app.route('/')
def index():
    comics = Comic.query.all()
    return render_template('index.html', comics=comics)
