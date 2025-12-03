from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from ..extensions import db
from ..models.owner import Owner
from ..models.dog import Dog

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    # If logged in: show "your dogs" + other dogs
    if current_user.is_authenticated:
        my_dogs = Dog.query.filter_by(owner_id=current_user.id).all()
        other_dogs = Dog.query.filter(Dog.owner_id != current_user.id).all()
        return render_template(
            "home.html",
            my_dogs=my_dogs,
            other_dogs=other_dogs,
            is_logged_in=True
        )
    else:
        # Not logged in: show all dogs (browse-only)
        all_dogs = Dog.query.all()
        return render_template(
            "home.html",
            all_dogs=all_dogs,
            is_logged_in=False
        )


@main_bp.route("/dogs/new", methods=["GET", "POST"])
@login_required
def new_dog():
    if request.method == "POST":
        # owner is the logged-in user
        owner_id = current_user.id

        name = request.form.get("name")
        age_years = request.form.get("age_years", type=float)
        breed = request.form.get("breed")
        size = request.form.get("size")
        gender = request.form.get("gender")
        bio = request.form.get("bio")
        city = request.form.get("city") or current_user.city
        pincode = request.form.get("pincode")

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

    # GET: show form
    return render_template("dogs_new.html")


@main_bp.route("/dogs/<int:dog_id>/recommendations")
@login_required
def dog_recommendations(dog_id):
    dog = Dog.query.get_or_404(dog_id)

    # Optional: only allow owner to see their own dog's matches
    if dog.owner_id != current_user.id:
        flash("You can only view matches for your own dogs.", "error")
        return redirect(url_for("main.home"))

    candidates = (Dog.query
                  .filter(Dog.id != dog.id, Dog.city == dog.city)
                  .all())

    return render_template(
        "dogs_recommendations.html",
        dog=dog,
        candidates=candidates
    )
