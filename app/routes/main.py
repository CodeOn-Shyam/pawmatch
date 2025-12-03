from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions import db
from ..models.owner import Owner
from ..models.dog import Dog

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    owners = Owner.query.all()
    dogs = Dog.query.all()
    return render_template("home.html", owners=owners, dogs=dogs)


@main_bp.route("/owners/new", methods=["GET", "POST"])
def new_owner():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        city = request.form.get("city")

        if not (name and email):
            flash("Name and email are required", "error")
            return redirect(url_for("main.new_owner"))

        if Owner.query.filter_by(email=email).first():
            flash("Owner with this email already exists", "error")
            return redirect(url_for("main.new_owner"))

        owner = Owner(name=name, email=email, city=city)
        db.session.add(owner)
        db.session.commit()
        flash("Owner created successfully!", "success")
        return redirect(url_for("main.home"))

    return render_template("owners_new.html")


@main_bp.route("/dogs/new", methods=["GET", "POST"])
def new_dog():
    owners = Owner.query.all()
    if request.method == "POST":
        owner_id = request.form.get("owner_id")
        name = request.form.get("name")
        age_years = request.form.get("age_years", type=float)
        breed = request.form.get("breed")
        size = request.form.get("size")
        gender = request.form.get("gender")
        bio = request.form.get("bio")
        city = request.form.get("city")
        pincode = request.form.get("pincode")

        if not owner_id:
            flash("Owner is required", "error")
            return redirect(url_for("main.new_dog"))

        if not (name and age_years is not None and breed and size and gender):
            flash("Please fill all required fields", "error")
            return redirect(url_for("main.new_dog"))

        dog = Dog(
            owner_id=owner_id,
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
        flash("Dog profile created!", "success")
        return redirect(url_for("main.home"))

    return render_template("dogs_new.html", owners=owners)


@main_bp.route("/dogs/<int:dog_id>/recommendations")
def dog_recommendations(dog_id):
    dog = Dog.query.get_or_404(dog_id)
    candidates = (Dog.query
                  .filter(Dog.id != dog.id, Dog.city == dog.city)
                  .all())
    return render_template(
        "dogs_recommendations.html",
        dog=dog,
        candidates=candidates
    )
