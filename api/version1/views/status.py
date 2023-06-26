from flask import jsonify, Blueprint
from api.version1.views import app_views

"""Checks the status of the site"""
@app_views.route('/status')
def status():
    return jsonify({"status": "OK"})