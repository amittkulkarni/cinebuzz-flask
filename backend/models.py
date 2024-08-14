from datetime import datetime
from backend import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.Enum("Admin", "Customer", "Manager", name="role"), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    reservations = db.relationship("Reservation", backref="user", lazy=True)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=True)
    language = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    duration = db.Column(db.Integer, nullable=False)
    showtimes = db.relationship("Showtime", backref="movie", lazy=True)


class Theatre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    seats = db.Column(db.JSON, nullable=False)  # Stored as JSON for flexible seat arrangement
    showtimes = db.relationship("Showtime", backref="theatre", lazy=True)


class Showtime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_price = db.Column(db.Float, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)
    theatre_id = db.Column(db.Integer, db.ForeignKey("theatre.id"), nullable=False)
    reservations = db.relationship("Reservation", backref="showtime", lazy=True)


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    seats = db.Column(db.JSON, nullable=False)  # Stored as JSON for seat details
    order_id = db.Column(db.String(100), unique=True, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    showtime_id = db.Column(db.Integer, db.ForeignKey("showtime.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
