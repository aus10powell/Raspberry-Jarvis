from flask import Blueprint, render_template
from picamera import PiCamera

vision_bp = Blueprint(
    "vision_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="assets",
)


@vision_bp.route("/take_picture", methods=["POST", "GET"])
def take_picture():
    if request.method == "POST":
        python_action = request.form["take_picture"]
        pic_fname = "image_{}.jpg".format(
            datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
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
    image_names = os.listdir(app.config["UPLOAD_FOLDER"])
    print(image_names)
    full_filename = os.path.join(
        app.config["UPLOAD_FOLDER"], "image_20210625-120144.jpg"
    )
    return render_template(
        "display_picture.html", image_names=image_names, user_image=full_filename
    )
