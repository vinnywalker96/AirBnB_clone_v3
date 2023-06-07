#!/usr/bin/python3
from api.v1.views import app_views
from flask import requests, abort, jsonify

@app_views.route('/status')
def get_views(app_views):
    view = [view for view in app_views if app_view not None]

    if len(view) == 0:
        abort(404)
    if not request.json:
        abort(400)
    return jsonify({"status": "ok"})
