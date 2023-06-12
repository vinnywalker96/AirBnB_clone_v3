#!/usr/bin/python3
"""Import libraries"""
from flask import abort, jsonify
from flask import make_response
from models import  storage
from models.place import Place
from models.amenity import Amenity
from api.v1.views import app_views

@app_views.route('/places/<place_id>/amenities', methods=['GET'])
def get_place_amenities(place_id):
    """get a place by amenity"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenities = place.amenities
    return jsonify([amenity.to_dict() for amenity in amenities])


@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['DELETE'])
def delete_place_amenity(place_id, amenity_id):
    """Deletes an amenity"""
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if not place or not amenity:
        abort(404)

    if amenity not in place.amenities:
        abort(404)

    place.amenities.remove(amenity)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                  methods=['POST'])
def link_place_amenity(place_id, amenity_id):
    """Creates a link """
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if not place or not amenity:
        abort(404)

    if amenity in place.amenities:
        return jsonify(amenity.to_dict()), 200

    place.amenities.append(amenity)
    storage.save()
    return make_response(jsonify(amenity.to_dict()), 201)

