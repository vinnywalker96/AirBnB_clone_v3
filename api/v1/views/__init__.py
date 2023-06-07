#!/usr/bin/python3
from flask import Blueprint

app_views = Blueprint('/api/v1', __name__,
                      template_folder='v1/views/__init__.py')

