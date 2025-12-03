from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models.owner import Owner
from ..models.dog import Dog

dogs_bp = Blueprint("dogs", __name__)

@dogs_bp.post("/")
def create_dog():
    data = request.get_json() or {}

    owner_id = data.get("owner_id")
    if not owner_id:
        return {"error": "owner_id is required"}, 400

    owner = Owner.query.get(owner_id)
    if not owner:
        return {"error": "owner not found"}, 404

    required_fields = ["name", "age_years", "breed", "size", "gender"]
    missing = [f for f in required_fields if data.get(f) is None]
    if missing:
        return {"error": f"Missing fields: {', '.join(missing)}"}, 400

    dog = Dog(
        owner_id=owner_id,
        name=data["name"],
        age_years=data["age_years"],
        breed=data["breed"],
        size=data["size"],
        gender=data["gender"],
        bio=data.get("bio"),
        city=data.get("city", owner.city),
        pincode=data.get("pincode"),
    )

    db.session.add(dog)
    db.session.commit()

    return dog.to_dict(), 201


@dogs_bp.get("/")
def list_dogs():
    owner_id = request.args.get("owner_id", type=int)
    query = Dog.query
    if owner_id:
        query = query.filter_by(owner_id=owner_id)

    dogs = query.all()
    return jsonify([d.to_dict() for d in dogs]), 200
