from flask import jsonify
from flask_restx import Resource

from backend import api
from backend.models import Movie, Reservation, Showtime, Theatre, User

from .api_models import movie_model, reservation_model, showtime_model, theatre_model, user_model

# ------------------------------------------------------------------------------------

# This is for testing purposes, not final. Will be completed later. Feel free to add.

# ------------------------------------------------------------------------------------


@api.route("/users", "/users/<int:id>")
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


@api.route("/movies/<int:id>")
class MovieResource(Resource):
    @api.marshal_with(movie_model)
    def get(self, id):
        movie = Movie.query.get_or_404(id)
        return movie, 200


@api.route("/theatres", "/theatres/<int:id>")
class TheatreResource(Resource):
    @api.marshal_with(theatre_model)
    def get(self):
        theatres = Theatre.query.all()
        return theatres, 200


@api.route("/showtimes", "/showtimes/<int:id>")
class ShowtimeResource(Resource):
    @api.marshal_with(showtime_model)
    def get(self):
        showtime = Showtime.query.all()
        return showtime, 200


@api.route("/reservations/<int:id>")
class ReservationResource(Resource):
    @api.marshal_with(reservation_model)
    def get(self):
        reservation = Reservation.query.all()
        return reservation, 200
