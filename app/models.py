from datetime import datetime
from .extensions import db

class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)

    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    category = db.Column(db.String)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)