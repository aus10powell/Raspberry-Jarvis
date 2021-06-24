from flask import Flask
from flask import render_template
from flask import request
from flask import Response
import logging
import datetime
import sys
import os

from picamera import PiCamera
from time import sleep

PICTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "data", "pictures"
)

logger = logging.getLogger("werkzeug")
handler = logging.FileHandler("app.log")
logger.addHandler(handler)


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PICTURE_DIR

def take_picture():
    """Receives click form html form and takes picture on Pi"""
    print("Camera button was clicked", file=sys.stderr)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/take_picture", methods=["POST", "GET"])
def take_picture():
    logging.info("page has been hit")
    if request.method == "POST":
        python_action = request.form["take_picture"]

        camera = PiCamera()
        camera.start_preview()
        sleep(3)
        pic_fname = "image_{}.jpg".format(
            datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        )
        camera.capture(
            os.path.join(
                PICTURE_DIR,
                pic_fname
            )
        )
        camera.stop_preview()

        logging.info("INFO Picture Taken")
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], pic_fname)
        return "Successfully took a picture" #render_template("show_picture.html",user_image=full_filename)#
    else:
        picture_status = None
        return render_template(
            "take_picture.html", title="Jarvis Home Monitoring System", picture_status=picture_status
        )


def gen(camera):
    while True:
        frame = PiCamera.get_frame()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/video_feed")
def video_feed():
    return Response(
        gen(PiCamera()), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(debug=True, host="10.0.0.16", port=5000)
