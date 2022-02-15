# RaspberryJarvis/__init__.py

from flask import Flask, render_template, request, Response
from flask_assets import Environment
from config import Config
import datetime, logging, os, sys
from flask_sqlalchemy import SQLAlchemy

#####################
## Uncomment to revert to old code
####################
# from home.home import home_bp
# from vision.vision import vision_bp

# app = Flask(__name__)

## Register Blueprints
# Puts the home blueprint
# app.register_blueprint(home_bp, template_folder="templates", static_folder="static")
# app.register_blueprint(
#     vision_bp, url_prefix="/vision", template_folder="templates", static_folder="static"
# )
# app.register_blueprint(
#     air_quality_bp,
#     url_prefix="/air_quality",
#     template_folder="templates",
#     static_folder="static",
# )
# from ddtrace import patch_all


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

        # Compile static assets
        # compile_static_assets(assets)

        return app


## Logging
logger = logging.getLogger("werkzeug")
handler = logging.FileHandler("app.log")
logger.addHandler(handler)
