from flask import Flask
from .config import Config
from .extensions import db, mongo
from .routes import owners_bp, dogs_bp, matches_bp, main_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    mongo.init_app(app)

    # frontend
    app.register_blueprint(main_bp)

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
