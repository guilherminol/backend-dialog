from flask import Flask,Blueprint
from app.routes.user_route import bp as bp_user
bp_api = Blueprint("api",__name__)

def init_app(app:Flask):
    bp_api.register_blueprint(bp_user)
    app.register_blueprint(bp_api)