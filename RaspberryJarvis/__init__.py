# RaspberryJarvis/__init__.py

from flask import Flask, render_template, request, Response
from flask_assets import Environment
from config import Config
import datetime, logging, os, sys
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    # assets = Environment()
    # assets.init_app(app)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # adding configuration for using a sqlite database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite3.db"
    db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from .home import home
        from .air_quality import air_quality
        from .vision import vision

        # Create db
        db.create_all()  # Create database tables for our data models

        # Register Blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(air_quality.air_quality_bp)
        app.register_blueprint(vision.vision_bp)
        return app


## Logging
logger = logging.getLogger("werkzeug")
handler = logging.FileHandler("app.log")
logger.addHandler(handler)
