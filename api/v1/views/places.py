#!/usr/bin/python3
"""Import Libraries"""
from api.v1.views import app_views
from flask import jsonify
from flask import abort
from flask import request, make_response
from models import storage
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.user import User


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def get_place(city_id):
    """Get all Places"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    places = city.places
    return jsonify([place.to_dict() for place in places])


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_place_by_state(place_id):
    """Get all places"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """Delete a place"""
    place = storage.get(Place, city_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/cities/<city_id>/<place_id>', methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    """Creates a new city"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if 'user_id' not in data:
        abort(400, 'Missing user_id')
    user = storage.get(User, data['user_id'])
    if user is None:
        abort(404)
    if 'name' not in data:
        abort(400, 'Missing name')
    place = Place(**data)
    place.city_id = city_id
    storage.new(place)
    storage.save()
    return make_response(jsonify(place.to_dict()), 201)


@app_views.route('/places/<place_id>', methods=['PUT'],
                 strict_slashes=False)
def update_place(place_id):
    """Update place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    ignore_keys = [
            'id',
            'user_id',
            'city_id',
            'created_at',
            'updated-at',
            ]
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(place, key, value)
    storage.save()
    return make_response(jsonify(place.to_dict()), 200)
