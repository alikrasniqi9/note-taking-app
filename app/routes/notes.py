from flask import Blueprint, render_template, request, redirect
from app.models import Note
from app.extensions import db


notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/')
def index():
    return render_template('index.html')

@notes_bp.route("/test")
def test():
    note = Note(title="Test", content="Hello world")
    db.session.add(note)
    db.session.commit()
    return "Saved!"