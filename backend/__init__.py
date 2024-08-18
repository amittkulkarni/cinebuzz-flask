import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI", None)
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", None)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app, prefix="/api")
jwt = JWTManager(app)
CORS(app)


def create_tables():
    from backend.models import User

    db.create_all()
    if not User.query.filter_by(name="admin").first():
        admin = User(
            name="admin",
            email="admin@email.com",
            password="admin123",
            role="Admin",
        )
        db.session.add(admin)
        db.session.commit()


from backend.rest import resources
