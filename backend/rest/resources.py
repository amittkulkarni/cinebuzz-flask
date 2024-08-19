from flask import jsonify
from flask_restx import Resource
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

from backend import api, db
from backend.models import Movie, Reservation, Showtime, Theatre, User

from .api_models import movie_model, reservation_model, showtime_model, theatre_model, user_model


def role_required(required_role):
    def wrapper(func):
        @jwt_required()
        def decorator(*args, **kwargs):
            user_id = get_jwt_identity()
            user = User.query.get(user_id)
            if user.role != required_role:
                return {"message": "Access Forbidden"}, 403
            return func(*args, **kwargs)

        return decorator

    return wrapper


@api.route("/login")
class LoginResource(Resource):
    def post(self):
        user = User.query.filter_by(email=api.payload["email"]).first()
        if user and user.password == api.payload["password"]:
            access_token = create_access_token(identity=user.id, additional_claims={"role": user.role})
            return {"access_token": access_token, "role": user.role}, 200
        else:
            return {"message": "Invalid email or password"}, 401


@api.route("/register")
class RegisterResource(Resource):
    def post(self):
        if User.query.filter_by(email=api.payload["email"]).first():
            return {"message": "User already exists"}, 409
        user = User(
            name=api.payload["name"],
            email=api.payload["email"],
            password=api.payload["password"],
            role=api.payload["role"],
            phone=api.payload["phone"]
        )
        db.session.add(user)
        db.session.commit()
        return {"message": "User added successfully"}, 201


@api.route("/users")
class UserResource(Resource):
    @api.marshal_with(user_model)
    def get(self):
        user = User.query.filter_by(role="Customer").first()
        return user, 200


@api.route("/movies")
class MovieResource(Resource):
    @api.marshal_with(movie_model)
    def get(self):
        movie = Movie.query.all()
        return movie, 200

    @api.expect(movie_model)
    @role_required("Manager")
    def post(self):
        movie = Movie(
            title=api.payload["title"],
            image=api.payload["image"],
            language=api.payload["language"],
            genre=api.payload["genre"],
            director=api.payload["director"],
            description=api.payload["description"],
            duration=api.payload["duration"],
        )
        db.session.add(movie)
        db.session.commit()
        return jsonify({"message": "Movie added successfully"}), 201


@api.route("/movies/<int:id>")
class MovieResource(Resource):
    @api.marshal_with(movie_model)
    def get(self, id):
        movie = Movie.query.get_or_404(id)
        return movie, 200


@api.route("/theatres")
class TheatreResource(Resource):
    @api.marshal_with(theatre_model)
    def get(self):
        theatres = Theatre.query.all()
        return theatres, 200


@api.route("/movies/<int:id>/showtimes")
class ShowtimeResource(Resource):
    @api.marshal_with(showtime_model)
    def get(self, id):
        showtime = Showtime.query.filter_by(movie_id=id).all()
        return showtime, 200


@api.route("/reservations")
class ReservationResource(Resource):
    @api.marshal_with(reservation_model)
    def get(self):
        reservation = Reservation.query.all()
        return reservation, 200
