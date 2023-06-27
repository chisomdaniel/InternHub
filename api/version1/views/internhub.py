from flask import jsonify, request, abort
from api.version1.views import app_views
from models.internship import Internship
from models import storage

"""APPLICATION MANAGEMENT APIs"""
@app_views.route('/jobs', methods=['GET'], strict_slashes=False)
def get_jobs():
    """ Gets all posted jobs"""
    jobs = storage.all(Internship).values()
    job_list = []
    for job in jobs:
        job_list.append(job.to_dict())
    return jsonify(job_list)
@app_views.route('/jobs/<job_id>', methods=['GET'], strict_slashes=False)
def single_job(job_id):
    """Retrieves a single job"""
    job = storage.get(Internship, job_id)
    if not job:
        abort(404)
    return jsonify(job.to_dict())
@app_views.route('/jobs/<job_id>', methods=['DELETE'], strict_slashes=False)
def del_job(job_id):
    """Deletes a job if no longer needed or not available"""
    job = storage.get(Internship, job_id)
    if not job:
        abort(404)
    storage.delete(job)
    storage.save()
    return jsonify({}), 200
@app_views.route('/jobs', methods=['POST'], strict_slashes=False)
def post_jobs():
    """ Submits an application """
    if not request.get_json():
        abort(400, description="Not a JSON")
        
    data = request.get_json()
    insta = Internship(**data)
    insta.save()
    return jsonify(insta.to_dict()), 201

@app_views.route('/jobs/<update_id>', methods=['PUT'], strict_slashes=False)
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
        