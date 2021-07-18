from flask import Blueprint, render_template, request
from picamera import PiCamera
import os, sys
import logging
import datetime
from time import sleep

from bokeh import plotting
from bokeh import resources
from bokeh import embed
from bokeh.util import string

vision_bp = Blueprint(
    "vision_bp", __name__, template_folder="templates", static_folder="static"
)


PICTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "static", "raspberry_pictures"
)


@vision_bp.route("/bokeh")
def bokeh():

    # init a basic bar chart:
    # http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars
    fig = plotting.figure(plot_width=600, plot_height=600)
    fig.vbar(
        x=[1, 2, 3, 4], width=0.5, bottom=0, top=[1.7, 2.2, 4.6, 3.9], color="navy"
    )

    # grab the static resources
    js_resources = resources.INLINE.render_js()
    css_resources = resources.INLINE.render_css()

    # render template
    script, div = embed.components(fig)
    html = render_template(
        "bokeh.html",
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return html.encode("utf8")


@vision_bp.route("/take_picture", methods=["POST", "GET"])
def take_picture():
    if request.method == "POST":
        python_action = request.form["take_picture"]
        pic_fname = "image_{}.jpg".format(
            datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        )
        print(
            "Hello world! {}".format(os.path.dirname(os.path.realpath(__file__))),
            file=sys.stderr,
        )
        # Take a picture
        with PiCamera() as camera:
            sleep(1)
            camera.capture(os.path.join(PICTURE_DIR, pic_fname))

        logging.info("INFO Picture Taken")
        picture_status = "Picture Taken"
        return render_template(
            "take_picture.html", picture_status=picture_status, fname=pic_fname
        )
    else:
        picture_status = None
        return render_template(
            "take_picture.html",
            title="Jarvis Home Monitoring System",
            picture_status=picture_status,
        )


@vision_bp.route("/display_pictures")
def display_pictures():
    image_names = os.listdir(PICTURE_DIR)
    return render_template("display_picture.html", image_names=image_names)
