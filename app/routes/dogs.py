from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from ..extensions import db
from ..models.dog import Dog

dogs_bp = Blueprint("dogs", __name__)

@dogs_bp.post("/")
@login_required
def create_dog_api():
    data = request.get_json() or {}

    name = data.get("name")
    age_years = data.get("age_years")
    breed = data.get("breed")
    size = data.get("size")
    gender = data.get("gender")
    bio = data.get("bio")
    city = data.get("city") or current_user.city
    pincode = data.get("pincode")

    if not (name and age_years is not None and breed and size and gender):
        return {"error": "Missing required fields"}, 400

    dog = Dog(
        owner_id=current_user.id,
        name=name,
        age_years=age_years,
        breed=breed,
        size=size,
        gender=gender,
        bio=bio,
        city=city,
        pincode=pincode,
    )
    db.session.add(dog)
    db.session.commit()

    return dog.to_dict(), 201
