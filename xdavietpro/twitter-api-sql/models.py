# models.py
from wsgi import db

class Tweet(db.Model):
    __tablename__ = "tweets"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    created_at = db.Column(db.String())

    def __repr__(self):
        return '<id {}>'.format(self.id)
