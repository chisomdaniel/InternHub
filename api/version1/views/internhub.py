from flask import jsonify, request, abort
from api.version1.views import app_views
from models.internship import Internship
from models import storage

"""APPLICATION MANAGEMENT APIs"""
@app_views.route('/jobs', methods=['POST'], strict_slashes=False)
def post_jobs():
    """ Submits an application """
    if not request.get_json():
        abort(400, description="Not a JSON")
        
    data = request.get_json()
    insta = Internship(**data)
    insta.save()
    return jsonify(insta.to_dict()), 201

@app_views.route('/update/<update_id>', methods=['PUT'], strict_slashes=False)
def update_job(update_id):
    """ Updates the application form"""
    interns = storage.get(Internship, update_id)
    if not interns:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    keys_ignore = ['id', 'created_at', 'updated_at']

    for k, v in interns.items():
        if k not in keys_ignore:
            setattr(interns, k, v)
    storage.save()
    return jsonify(interns.to_dict()), 201
        