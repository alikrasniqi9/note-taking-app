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

    q = request.args.get('q')

    if q:
        notes = Note.query.filter(
            Note.title.contains(q) |
            Note.content.contains(q)
        ).order_by(Note.created_at.desc()).all()

    else:
        notes = Note.query.order_by(Note.created_at.desc()).all()

    return render_template('index.html',notes=notes)

@notes_bp.route('/get/<int:id>')
def get_note(id):
    note = Note.query.get_or_404(id)
    notes = Note.query.order_by(Note.created_at.desc()).all()

    return render_template('index.html',notes=notes,selected_note=note)

@notes_bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    note = Note.query.get_or_404(id)

    db.session.delete(note)
    db.session.commit()

    return redirect(url_for('notes.index'))

@notes_bp.route('/create', methods=['POST'])
def create():
    category = request.form.get('category')

    note = Note(
        title='New Note',
        content='Freshly created note..',
        category=category
    )

    db.session.add(note)
    db.session.commit()

    return redirect(url_for('notes.get_note', id=note.id))

@notes_bp.route('/update/<int:id>', methods=['POST'])
def update(id):
    note = Note.query.get_or_404(id)
    title = request.form.get('title')
    content = request.form.get('content')
    category = request.form.get('category')

    note.title = title
    note.content = content
    note.category = category

    db.session.commit()

    return redirect(url_for('notes.get_note',id=note.id))

@notes_bp.route('/category/<category>')
def category(category):
    notes = Note.query.filter_by(
        category=category
    ).order_by(
        Note.created_at.desc()
    ).all()

    return render_template('index.html', notes=notes)





