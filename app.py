from flask import Flask, render_template, request, Response
from vision.vision import vision_bp
import logging
import datetime
import sys
import os


from time import sleep

PICTURE_DIR = os.path.join("static", "raspberry_pictures")

logger = logging.getLogger("werkzeug")
handler = logging.FileHandler("app.log")
logger.addHandler(handler)


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = PICTURE_DIR


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/take_picture", methods=["POST", "GET"])
# def take_picture():
#     if request.method == "POST":
#         python_action = request.form["take_picture"]
#         pic_fname = "image_{}.jpg".format(
#             datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
#         )

#         # Take a picture
#         with PiCamera() as camera:
#             sleep(1)
#             camera.capture(os.path.join(PICTURE_DIR, pic_fname))

#         logging.info("INFO Picture Taken")
#         picture_status = "Picture Taken"
#         return render_template(
#             "take_picture.html", picture_status=picture_status, fname=pic_fname
#         )
#     else:
#         picture_status = None
#         return render_template(
#             "take_picture.html",
#             title="Jarvis Home Monitoring System",
#             picture_status=picture_status,
#         )


# @app.route("/display_pictures")
# def display_pictures():
#     image_names = os.listdir(app.config["UPLOAD_FOLDER"])
#     print(image_names)
#     full_filename = os.path.join(
#         app.config["UPLOAD_FOLDER"], "image_20210625-120144.jpg"
#     )
#     return render_template(
#         "display_picture.html", image_names=image_names, user_image=full_filename
#     )


# def gen(camera):
#     while True:
#         frame = PiCamera.get_frame()
#         yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


# @app.route("/video_feed")
# def video_feed():
#     return Response(
#         gen(PiCamera()), mimetype="multipart/x-mixed-replace; boundary=frame"
#     )


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True)
app.register_blueprint(vision_bp, url_prefix='/vision')