from flask_restx import fields
from backend import api

# User model
user_model = api.model('User', {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'role': fields.String,  # Enum stored as String in API model
    'phone': fields.String,
})

# Movie model
movie_model = api.model('Movie', {
    'id': fields.Integer,
    'title': fields.String,
    'image': fields.String,
    'language': fields.String,
    'genre': fields.String,
    'director': fields.String,
    'trailer': fields.String,
    'description': fields.String,
    'duration': fields.Integer,
    'start_date': fields.DateTime(dt_format='iso8601'),
    'end_date': fields.DateTime(dt_format='iso8601'),
})

# Theatre model
theatre_model = api.model('Theatre', {
    'id': fields.Integer,
    'name': fields.String,
    'city': fields.String,
    'ticket_price': fields.Float,
    'seats': fields.Raw,  # JSON field, raw representation
    'image': fields.String,
})

# Showtime model
showtime_model = api.model('Showtime', {
    'id': fields.Integer,
    'ticket_price': fields.Float,
    'start_date': fields.DateTime(dt_format='iso8601'),
    'end_date': fields.DateTime(dt_format='iso8601'),
    'movie_id': fields.Integer,  # Foreign key
    'theatre_id': fields.Integer,  # Foreign key
})

# Reservation model
reservation_model = api.model('Reservation', {
    'id': fields.Integer,
    'date': fields.DateTime(dt_format='iso8601'),
    'start_at': fields.DateTime(dt_format='iso8601'),
    'seats': fields.Raw,  # JSON field, raw representation
    'order_id': fields.String,
    'total': fields.Float,
    'showtime_id': fields.Integer,  # Foreign key
    'user_id': fields.Integer,  # Foreign key
})
