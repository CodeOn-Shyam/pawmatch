from flask import Blueprint, request, jsonify
from ..models.dog import Dog

matches_bp = Blueprint("matches", __name__)

@matches_bp.get("/recommendations")
def recommendations():
    dog_id = request.args.get("dog_id", type=int)
    if not dog_id:
        return {"error": "dog_id query param required"}, 400

    dog = Dog.query.get(dog_id)
    if not dog:
        return {"error": "dog not found"}, 404

    # basic: same city, different dog
    candidates = (Dog.query
                  .filter(Dog.id != dog.id, Dog.city == dog.city)
                  .all())

    recs = [c.to_dict() for c in candidates]
    return jsonify(recs), 200
