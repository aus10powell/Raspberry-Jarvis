from flask import Flask, render_template, request, Response
from vision.vision import vision_bp
import logging
import datetime
import sys
import os

from home.home import home_bp
from vision.vision import vision_bp

from time import sleep

PICTURE_DIR = os.path.join("static", "raspberry_pictures")


app = Flask(__name__)
app.register_blueprint(home_bp, template_folder="templates", static_folder="static")
app.register_blueprint(
    vision_bp, url_prefix="/vision", template_folder="templates", static_folder="static"
)


logger = logging.getLogger("werkzeug")
handler = logging.FileHandler("app.log")
logger.addHandler(handler)


if __name__ == "__main__":
    app.run()  # host="0.0.0.0", debug=True,port=5000
