#!/usr/bin/python3
from api.v1.views import app_views
from models.state import State
from models import storage
from flask import jsonify 
from flask import abort

@app_views.route('/states', methods=['GET'])
def get_states():
    """retrieves states"""
    states = list(storage.all(State).values)
    return states

@app_views.route('/states/<state_id>', methods=['GET'])
def method_handler(state_id):
    """Handles requests"""
    id = storage.all(State).values()[0].id
    if state_id == id:
        return {}
    
