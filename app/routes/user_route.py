from flask import Blueprint
from app.controllers import user_controler
bp = Blueprint("users",__name__,url_prefix='/users')

bp.get("")(user_controler.get_all)
bp.get("/<userId>")(user_controler.get_one)