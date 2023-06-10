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


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def get_place(city_id):
    """Get all Places"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    places = [place.to_dict() for place in city.places]
    return jsonify(places)
