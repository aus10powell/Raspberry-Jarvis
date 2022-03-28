# RaspberryJarvis/__init__.py

from flask import Flask, render_template, request, Response
from flask_assets import Environment
from config import Config
import datetime, logging, os, sys
from flask_sqlalchemy import SQLAlchemy


def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        # Import parts of our application
        from .home import home
        from .air_quality import air_quality
        from .vision import vision

        # Register Blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(air_quality.air_quality_bp)
        app.register_blueprint(vision.vision_bp)
        return app


## Logging
logger = logging.getLogger("werkzeug")
handler = logging.FileHandler("app.log")
logger.addHandler(handler)
