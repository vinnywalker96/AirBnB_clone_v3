#!/usr/bin/python3
"""Import Libraries"""
from api.v1.views import app_views
from flask import jsonify
from flask import abort
from flask import request, make_response
from models import storage
from models.user import User


@app_views.route('/users'/, methods=['GET'],
                 strict_slashes=False)
def get_users():
    """Get all users"""
    users = storage.all(User)
    user_list = [user.to_dict() for user in users.values()]
    return jsonify(user_list)


@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def get_user_by_id(user_id):
    """Get all users"""
    users = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(users.to_dict())
