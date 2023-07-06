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
    jobs = storage.all(Internship)
    key = f"Internship.{job_id}"

    job = jobs.get(key, None)
    if not job:
        abort(404, "Invalid id specified")
    return jsonify(job.to_dict())


@app_views.route('/jobs/<job_id>', methods=['DELETE'], strict_slashes=False)
def del_job(job_id):
    """Deletes a job if no longer needed or not available"""
    positions = storage.all(Internship)
    key = f"Internship.{job_id}"

    position = positions.get(key, None)
    if not position:
        abort(404, "Invalid id specified")

    position.delete()
    return jsonify({}), 200


@app_views.route('/jobs', methods=['POST'], strict_slashes=False)
def post_jobs():
    """ Submits an application """
    if not request.get_json():
        abort(400, description="Not a JSON")
        
    data = request.get_json()
    insta = Internship(**data)

    return jsonify(insta.to_dict()), 201


@app_views.route('/jobs/<job_id>', methods=['PUT'], strict_slashes=False)
def update_job(job_id):
    """ Updates the application form"""
    positions = storage.all(Internship)
    key = f"Internship.{job_id}"

    position = positions.get(key, None)
    if not position:
        abort(404, "Invalid id specified")
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    
    keys_ignore = ['id', 'updated_at', 'created_at', '__class__', '_sa_instance_state']

    for k, v in data.items():
        if k not in keys_ignore:
            setattr(position, k, v)

    position.save()
    return jsonify(position.to_dict()), 201