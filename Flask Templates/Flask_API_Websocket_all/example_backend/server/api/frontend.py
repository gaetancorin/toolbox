from example_backend.server.api import main_api, get_server
from example_backend.server.socketio.frontendio import FrontendIOSession
from flask import jsonify
from flask_restx import Resource

namespace = main_api.namespace("session", description="API return unique session id for frontend Websocket")


@namespace.route("/id")
class SessionId(Resource):
    """Handle request on /sessionid"""
    # example: 127.0.0.1:5001/api/session/id
    def get(self):
        """Return a session ID be used by the frontend"""
        session = FrontendIOSession()
        get_server().socketio.on_namespace(session)
        # get_server().socketio.server.namespace_handlers.pop(f"/frontend/{session.session_id}")
        print(f"[API]: Generate SessionId ({session.session_id})")
        return jsonify({"session_id": session.session_id})
