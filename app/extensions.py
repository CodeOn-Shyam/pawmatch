from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_login import LoginManager

db = SQLAlchemy()
mongo = PyMongo()
login_manager = LoginManager()
