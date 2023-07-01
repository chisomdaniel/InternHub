#!/usr/bin/python3
"""Importation of flask"""
from os import environ
from models import storage
from api.version1.views import app_views
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/version1/*": {"origins": "*"}})

@app.errorhandler(404)
def not_found(error):
    """
    404:
    description: Resource not found
    """
    return jsonify({"error": "Not found"}), 404

@app.teardown_appcontext
def close_database(error):
    """Closes Storage"""
    storage.close()

if __name__ == "__main__":
    host = environ.get('INTERNHUB_API_HOST')
    port = environ.get('INTERNHUB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)