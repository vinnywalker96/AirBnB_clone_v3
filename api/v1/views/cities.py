#!/usr/bin/python3
"""Import Libraries"""
from api.v1.views import app_views
from flask import jsonify
from flask import abort
from flask import request, make_response
from models import storage
from models.city import City
from models.state import State


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities_by_state(state_id):
    """Retrieves all cities"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_cities_by_id(city_id):
    """Retrieves all cities"""
    cities = storage.get(City, city_id)
    if cities is None:
        abort(404)
    return jsonify(cities.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_city_by_id(city_id):
    """Delete city by id"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.new(city)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def post_city(state_id):
    """Post a new city"""
    state = storage.get(State, state_id)
    cities = [city.to_dict() for city in state.cities]
    if state is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, 'Not s JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    
    city = City()
    city.name = data['name']
    city.state_id = state_id
    storage.new(city)
    storage.save()
    return make_response(jsonify({}), 200)

