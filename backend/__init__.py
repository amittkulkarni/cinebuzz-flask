from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://amit:amitamit@localhost:5432/cinedb'  # USE ENV VARIABLE
app.config['JWT_SECRET_KEY'] = 'secret'  # USE ENV VARIABLE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app, prefix='/api')
jwt = JWTManager(app)
CORS(app)


def create_tables():
    from backend.models import User
    db.create_all()
    if not User.query.filter_by(name='super_admin').first():
        super_admin = User(
            name='super_admin',
            email='super@email.com',
            password='super123',
            role='SuperAdmin'
        )
        db.session.add(super_admin)
        db.session.commit()


from backend import router
