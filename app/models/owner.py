from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from ..extensions import db

class Owner(UserMixin, db.Model):
    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    city = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    password_hash = db.Column(db.String(255), nullable=True)

    dogs = db.relationship("Dog", backref="owner", lazy=True)

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "city": self.city,
            "created_at": self.created_at.isoformat(),
        }
