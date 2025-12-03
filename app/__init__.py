from flask import Flask
from .config import Config
from .extensions import db, mongo, login_manager
from .routes import owners_bp, dogs_bp, matches_bp, main_bp
from .routes.auth import auth_bp  # we'll create this file next
from .models.owner import Owner

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # init extensions
    db.init_app(app)
    mongo.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"  # redirect here if not logged in

    @login_manager.user_loader
    def load_user(user_id):
        return Owner.query.get(int(user_id))

    # frontend
    app.register_blueprint(main_bp)

    # auth
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # APIs
    app.register_blueprint(owners_bp, url_prefix="/api/owners")
    app.register_blueprint(dogs_bp, url_prefix="/api/dogs")
    app.register_blueprint(matches_bp, url_prefix="/api/matches")

    @app.get("/health")
    def health():
        return {"status": "ok", "service": "pawmatch-backend"}, 200

    with app.app_context():
        db.create_all()

    return app
