from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from ..extensions import db
from ..models.owner import Owner

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        city = request.form.get("city")
        password = request.form.get("password")

        if not (name and email and password):
            flash("Name, email and password are required", "error")
            return redirect(url_for("auth.register"))

        if Owner.query.filter_by(email=email).first():
            flash("An account with this email already exists", "error")
            return redirect(url_for("auth.register"))

        owner = Owner(name=name, email=email, city=city)
        owner.set_password(password)
        db.session.add(owner)
        db.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        owner = Owner.query.filter_by(email=email).first()
        if owner and owner.check_password(password):
            login_user(owner)
            flash("Logged in successfully!", "success")
            next_page = request.args.get("next") or url_for("main.home")
            return redirect(next_page)
        else:
            flash("Invalid email or password", "error")
            return redirect(url_for("auth.login"))

    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("main.home"))
