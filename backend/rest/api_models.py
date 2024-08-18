from flask_restx import fields

from backend import api

# User model
user_model = api.model(
    "User",
    {
        "id": fields.Integer(required=True),
        "name": fields.String(required=True),
        "email": fields.String(required=True),
        "role": fields.String(required=True),
        "phone": fields.String,
    },
)

# Movie model
movie_model = api.model(
    "Movie",
    {
        "id": fields.Integer,
        "title": fields.String(required=True),
        "image": fields.String(required=True),
        "language": fields.String(required=True),
        "genre": fields.String(required=True),
        "director": fields.String(required=True),
        "description": fields.String,
        "duration": fields.Integer(required=True),
    },
)

# Theatre model
theatre_model = api.model(
    "Theatre",
    {
        "id": fields.Integer,
        "name": fields.String(required=True),
        "seats": fields.Raw(required=True),
    },
)

# Showtime model
showtime_model = api.model(
    "Showtime",
    {
        "id": fields.Integer,
        "ticket_price": fields.Float(required=True),
        "start_time": fields.DateTime(dt_format="iso8601", required=True),
        "end_time": fields.DateTime(dt_format="iso8601", required=True),
        "movie_id": fields.Integer,  # Foreign key
        "theatre_id": fields.Integer,  # Foreign key
    },
)

# Reservation model
reservation_model = api.model(
    "Reservation",
    {
        "id": fields.Integer,
        "date": fields.DateTime(dt_format="iso8601", required=True),
        "seats": fields.Raw(required=True),
        "order_id": fields.String(required=True),
        "total_price": fields.Float(required=True),
        "showtime_id": fields.Integer,  # Foreign key
        "user_id": fields.Integer,  # Foreign key
    },
)
