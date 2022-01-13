from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

image_folder = "static"

app = Flask(__name__)
app.config.from_object(Config)
app.config["UPLOAD_FOLDER"] = image_folder
bootstrap = Bootstrap(app)

from app import routes
