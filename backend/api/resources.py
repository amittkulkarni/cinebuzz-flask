from api_models import movie_model, reservation_model, showtime_model, theatre_model, user_model
from flask_restx import Resource

from backend import api
from backend.models import Movie, Reservation, Showtime, Theatre, User

# ------------------------------------------------------------------------------------

# This is for testing purposes, not final. Will be completed later. Feel free to add.

# ------------------------------------------------------------------------------------


@api.route("/users", "/users/<int:id>")
class UserResource(Resource):
    @api.marshal_with(user_model)
    def get(self):
        user = User.query.filter_by(role="Customer").first()
        return user


@api.route("/movies", "/movies/<int:id>")
class MovieResource(Resource):
    @api.marshal_with(movie_model)
    def get(self):
        movie = Movie.query.all()
        return movie


@api.route("/theatres", "/theatres/<int:id>")
class TheatreResource(Resource):
    @api.marshal_with(theatre_model)
    def get(self):
        theatre = Theatre.query.all()
        return theatre


@api.route("/showtimes", "/showtimes/<int:id>")
class ShowtimeResource(Resource):
    @api.marshal_with(showtime_model)
    def get(self):
        showtime = Showtime.query.all()
        return showtime


@api.route("/reservations/<int:id>")
class ReservationResource(Resource):
    @api.marshal_with(reservation_model)
    def get(self):
        reservation = Reservation.query.all()
        return reservation
