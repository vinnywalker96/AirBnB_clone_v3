#!/usr/bin/python3
"""Import Libraries for Users"""
from api.v1.views import app_views
from flask import jsonify
from flask import abort
from flask import request
from flask import make_response
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'],
                strict_slashes=False)
def get_users():
    """Get all Users"""
    users = storage.all(User)
    user_list = [user.to_dict() for user in users.value()]
    return jsonify(user_list)
