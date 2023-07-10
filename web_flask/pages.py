#!/usr/bin/python3
'''Flask application for our internship post pages'''
from flask import Flask, render_template, abort
from models import storage
from models.internship import Internship
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/internship/*": {"origins": "*"}})


@app.route('/search_page.html', strict_slashes=False)
@app.route('/', strict_slashes=False)
def search_page():
    '''return the search page'''
    return render_template('search_page.html')


@app.route('/post.html', strict_slashes=False)
def post():
    '''returns the page to post a job'''
    return render_template('post.html')


@app.route('/internship/<post_id>', strict_slashes=False)
def post_page(post_id):
    '''return the page for the individual job posts.'''
    internships = storage.all("Internship")

    key = f"Internship.{post_id}"
    internship = internships.get(key, None)

    if internship is None:
        abort(404, 'page not found')

    return render_template('internship_page.html', info=internship)


@app.teardown_appcontext
def teardown_db(exception):
    '''close the database on teardown'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')
