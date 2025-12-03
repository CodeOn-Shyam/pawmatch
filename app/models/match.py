from datetime import datetime
from ..extensions import db

class Match(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)
    dog_a_id = db.Column(db.Integer, db.ForeignKey("dogs.id"), nullable=False)
    dog_b_id = db.Column(db.Integer, db.ForeignKey("dogs.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            "id": self.id,
            "dog_a_id": self.dog_a_id,
            "dog_b_id": self.dog_b_id,
            "created_at": self.created_at.isoformat(),
            "is_active": self.is_active,
        }
