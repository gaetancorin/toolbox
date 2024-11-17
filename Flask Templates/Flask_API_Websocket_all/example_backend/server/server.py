from engineio.payload import Payload
from example_backend.server.api import main_api
from example_backend.server.api.frontend import namespace as frontend_namespace
from example_backend.server.api.root import namespace2 as root_namespace
from example_backend.server.utils.json_encoder import JsonEncoder
from flask import Blueprint, Flask
from flask_socketio import SocketIO


class WebServer:
    """WebServer class, create a Flask app and run it in a Thread"""

    def __init__(self):
        """Initialize a Flask app"""
        self.app = Flask("backend", static_url_path="", static_folder="")
        self.app.json_encoder = JsonEncoder
        self.app.url_map.strict_slashes = False
        self.socketio = None
        self.init_socketio()
        self.init_rest_api()

    def init_socketio(self):
        """Init the socketIO server"""
        Payload.max_decode_packets = 500
        self.socketio = SocketIO(self.app, max_http_buffer_size=int(1e8), ping_timeout=10, cors_allowed_origins="*")
        print("Init socketio on Server")

    def init_rest_api(self):
        """Init the REST API server"""
        api_blueprint = Blueprint("api", __name__, url_prefix="/api")
        main_api.init_app(api_blueprint)
        main_api.add_namespace(frontend_namespace)
        main_api.add_namespace(root_namespace)
        self.app.register_blueprint(api_blueprint)
        print("Init rest api on Server")

    def start_server(self):
        """Start server and wait until server is started"""
        print("Start Server")
        self.socketio.run(self.app, host="0.0.0.0", port=5001, allow_unsafe_werkzeug=True)
