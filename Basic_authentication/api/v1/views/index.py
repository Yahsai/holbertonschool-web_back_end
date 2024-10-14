#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from flask import Blueprint

# Creamos el Blueprint para app_views
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

@app_views.route('/status/', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized/', methods=['GET'], strict_slashes=False)
def unauthorized() -> None:
    """
    This path was made to test
    the 401 error + Flask.
    """
    abort(401)


@app_views.route('/forbidden/', methods=['GET'], strict_slashes=False)
def forbidden():
    """
    This path was made to test
    the 403 error + Flask.
    """
    abort(403)
