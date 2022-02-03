from flask import Flask
from app import routes
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config["JSON_SORT_KEYS"] = False
    routes.init_app(app)
    return app