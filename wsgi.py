# from app import app
from RaspberryJarvis import init_app

app = init_app()

if __name__ == "__main__":
    app.run()  # host="0.0.0.0", debug=True, port=3000 <--- Uncomment to run
