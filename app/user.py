from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    nickname = db.Column(db.String(20), nullable=False)
    contact_no = db.Column(db.String(15))
    is_activated = db.Column(db.Boolean, nullable=False)
    start_date = db.Column(db.DateTime, server_default=db.func.now())
    note = db.relationship("Note", backref="user")

    def __init__(self, username, email, nickname, contact_no, id=None, is_activated=True):
        self.id = id
        self.username = username
        self.email = email
        self.nickname = nickname
        self.contact_no = contact_no
        self.is_activated = is_activated

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User %r>' % (self.username)

    def __eq__(self, other):
        return int(self.id) == int(other.id)
