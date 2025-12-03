from datetime import datetime
from ..extensions import db

class Dog(db.Model):
    __tablename__ = "dogs"

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("owners.id"), nullable=False)

    name = db.Column(db.String(64), nullable=False)
    age_years = db.Column(db.Float, nullable=False)
    breed = db.Column(db.String(64), nullable=False)
    size = db.Column(db.String(16), nullable=False)   # "small", "medium", "large"
    gender = db.Column(db.String(8), nullable=False)  # "male", "female"
    bio = db.Column(db.Text)

    city = db.Column(db.String(64))
    pincode = db.Column(db.String(16))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "name": self.name,
            "age_years": self.age_years,
            "breed": self.breed,
            "size": self.size,
            "gender": self.gender,
            "bio": self.bio,
            "city": self.city,
            "pincode": self.pincode,
            "created_at": self.created_at.isoformat(),
        }
