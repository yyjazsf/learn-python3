from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=True)
    sex = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username
