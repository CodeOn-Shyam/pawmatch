from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models.owner import Owner

owners_bp = Blueprint("owners", __name__)

@owners_bp.post("/")
def create_owner():
    data = request.get_json() or {}
    name = data.get("name")
    email = data.get("email")
    city = data.get("city")

    if not (name and email):
        return {"error": "name and email are required"}, 400

    if Owner.query.filter_by(email=email).first():
        return {"error": "owner with this email already exists"}, 409

    owner = Owner(name=name, email=email, city=city)
    db.session.add(owner)
    db.session.commit()

    return owner.to_dict(), 201


@owners_bp.get("/")
def list_owners():
    owners = Owner.query.all()
    return jsonify([o.to_dict() for o in owners]), 200
