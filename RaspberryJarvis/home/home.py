from flask import Blueprint, render_template
from picamera import PiCamera

home_bp = Blueprint(
    "home_bp", __name__, static_folder="static", template_folder="templates"
)


@home_bp.route("/home")
@home_bp.route("/")
def home():
    return render_template("home.html")


@home_bp.route("/about")
def about():
    return render_template("about.html")
