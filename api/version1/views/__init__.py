from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/version1')
from api.version1.views.status import *
from api.version1.views.internhub import *