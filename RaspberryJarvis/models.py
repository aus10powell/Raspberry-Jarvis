"""Data models."""
from . import db


class AirQuality(db.Model):
    """Data model for air quality readings."""

    __tablename__ = "flaskdb-air-quality"
    id = db.Column(db.Integer, primary_key=True)
    pm25 = db.Column(db.Float(64), index=False, unique=False, nullable=False)
    pm10 = db.Column(db.Float(64), index=False, unique=False, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)

    def __repr__(self):
        return "<User {}>".format(self.username)
