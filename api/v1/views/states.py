#!/usr/bin/python3
from api.v1.views import app_views
from models.state import State
from models import storage
from flask import jsonify

@app_views.route('/states', methods=['GET'])
def get_states():
    """retrieves states"""
    states = list(storage.all(State).values())[0].id
    data = list(storage.get(State, states).to_dict())
    return jsonify(data)


