from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://amit:amitamit@localhost:5432/cinedb'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app, prefix='/api')
jwt = JWTManager(app)
CORS(app)


from backend import router, models