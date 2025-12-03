from datetime import datetime
from ..extensions import db

class Owner(db.Model):
    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    city = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    dogs = db.relationship("Dog", backref="owner", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "city": self.city,
            "created_at": self.created_at.isoformat(),
        }
