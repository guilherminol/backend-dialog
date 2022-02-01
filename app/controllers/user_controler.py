from flask import jsonify, request
from http import HTTPStatus
from app.models.user_model import User

def get_all():
    User.check_database()
    all_users = User.get_all()
    if not all_users:
        User.add_data()
    user_keys = ['id','name','age','eyeColor','company','email','profilePic']
    all_users = [dict(zip(user_keys,user))for user in all_users]
    return jsonify(all_users)
    