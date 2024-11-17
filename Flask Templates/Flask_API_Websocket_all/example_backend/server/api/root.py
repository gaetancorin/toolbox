from example_backend import __version__
from example_backend.server.api import main_api
from flask import jsonify, make_response
from flask_restx import Resource

namespace2 = main_api.namespace("/", description="API return number version")


@namespace2.route("/version")
class Version(Resource):
    """Handle request on /version"""
    # example: 127.0.0.1:5001/api/version
    def get(self):
        """Return the backend version"""
        print(f"[API]: Send example-backend version {__version__}")
        return make_response(jsonify([f"examplebackend: {__version__}"]), 200)
