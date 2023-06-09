#!/usr/bin/python3
"""import libraries"""
from api.v1.views import app_views
from models.amenity import Amenity
from models import storage
from flask import jsonify
from flask import abort, request, make_response


@app_views.route('/amenities', methods=['GET'],
                 strict_slashes=False)
def get_amenity():
    """Get all amenities"""
    amenities = storage.all(Amenity)
    amenity_list = [amenity.to_dict() 
                    for amenity in amenities.values()]
    return jsonify(amenity_list)


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenities(amenity_id):
    """Get all amenities"""
    amenities = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity_list = [amenity.to_dict() 
                    for amenity in amenities.value()]
    return jsonify(amenity_list)
