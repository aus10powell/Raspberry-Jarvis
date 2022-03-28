# from flask import Flask, render_template, request, Response
# from vision.vision import vision_bp
# from air_quality.air_quality import air_quality_bp
# import datetime, logging, os, sys
# from flask_sqlalchemy import SQLAlchemy

# from home.home import home_bp
# from vision.vision import vision_bp

# from time import sleep

# PICTURE_DIR = os.path.join("static", "raspberry_pictures")

# db = SQLAlchemy()

# app = Flask(__name__)
# db.init_app(app)
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

# logger = logging.getLogger("werkzeug")
# handler = logging.FileHandler("app.log")
# logger.addHandler(handler)

# # Instructions to point browser to flask version testing
# # 1) put host="0.0.0.0", debug=True,port=3000 in app.run()
# # 2) run: python app.py
# # 3) point browser (on same network) to 10.0.0.16:3000
# if __name__ == "__main__":
#     app.run()  # host="0.0.0.0", debug=True,port=5000
