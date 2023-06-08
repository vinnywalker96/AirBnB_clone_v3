#!/usr/bin/python3
from api.v1.views import app_views
from models.state import State
from models import storage
from models.city import City
from flask import jsonify 
from flask import abort, request, make_response


@app_views.route('/states/', methods=['GET'])
def get_states():
    """retrieves states"""
    states = storage.all(State)
    states_list = [state.to_dict() for state in states.values()]
    return jsonify(states_list)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """get State filter by id"""
    states = storage.all(State)
    state_list = [state.to_dict() for state in states.values()]
    for filter  in state_list:
        if state_id == filter['id']:
            state = storage.get(State, filter['id'])
            return state.to_dict()
        else:
            abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Delete state object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    
    return make_response(jsonify({}), 200)


