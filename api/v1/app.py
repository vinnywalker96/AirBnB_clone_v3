#!/usr/bin/python3
"""import libraries"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext(exeption):
    """close database session"""
    storage.close()

if __name__ == "__main__":
    # Get host and port from environment variables or use default values
    host = os.environ.get("HBNB_API_HOST")
    port = os.environ.get("HBNB_API_PORT")

    app.run(host=host, port=port, threaded=True)
