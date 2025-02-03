from app import db


class Person(db.Method):
    _tablename_ = "mytable"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    job = db.Column(db.Text)