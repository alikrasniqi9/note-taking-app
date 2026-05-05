from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Note
from app.extensions import db


notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        content = request.form.get('content')
        title = request.form.get('title')

        if content:
            note = Note(
                title=title if title else 'I pa ftyr/pa titull',
                content=content
            )

            db.session.add(note)
            db.session.commit()

        return redirect(url_for('notes.index'))

    notes = Note.query.order_by(Note.created_at.desc()).all()

    return render_template('index.html',notes=notes)