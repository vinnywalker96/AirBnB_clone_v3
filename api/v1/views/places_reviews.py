#!/usr/bin/python3
"""Import Libraries"""
from api.v1.views import app_views
from flask import jsonify, abort
from flask import make_response
from flask import request
from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review

@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews(place_id):
    """ Get all Reviews"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    reviews = [review.to_dict() for review in place.reviews]
    return jsonify(reviews)



@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review(review_id):
    """Get review by id"""
    reviews = storage.get(Review, review_id)
    if reviews is None:
        abort(404)
    return jsonify(reviews.to_dict())
