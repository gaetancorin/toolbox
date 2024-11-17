from example_backend.server.api import main_api
from flask import jsonify, make_response
from flask_restx import Resource

version = "0.1.0"

namespace2 = main_api.namespace("/", description="API return number version")


@namespace2.route("/version")
class Version(Resource):
    """Handle request on /version"""
    # example: 127.0.0.1:5001/api/version
    def get(self):
        """Return the backend version"""
        print(f"[API]: Send example-backend version {version}")
        return make_response(jsonify([f"examplebackend: {version}"]), 200)
