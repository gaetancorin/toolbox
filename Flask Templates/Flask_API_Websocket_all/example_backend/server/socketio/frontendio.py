"""Module containing SocketIO api definition used by the frontend"""
from example_backend import __version__
from example_backend.server.api import get_server
from example_backend.server.socketio.session import Session
from example_backend.server.utils.hi_man import HiMan
from flask_socketio import Namespace
import time


class FrontendIOSession(Session, Namespace):
    """Session created to interact with a connected frontend"""

    def __init__(self):
        """Init a frontend session"""
        Session.__init__(self)
        Namespace.__init__(self, namespace=f"/frontend/{self.session_id}")
        self.hi_man = HiMan(callback=self._send_hi)

    def on_connect(self):
        """Called when the frontend is connected"""
        print(f"[SOCKETIO]: Frontend connection with SessionId ({self.session_id})")
        self.send_backend_version()

    def send_backend_version(self):
        # time.sleep(5)
        # not work in Postman because wait on_connect is done to listen
        print("send backend version ")
        self.emit("backend_version", __version__)

    def on_hi(self, _):
        print(f"[SOCKETIO]: Receive 'Hi' to ({self.session_id})")
        self.hi_man.send_hi()

    def _send_hi(self, response):
        print(f"[SOCKETIO]: Respond 'Hi man !' to ({self.session_id})")
        self.emit("respond_hi", response)

    def on_hello(self, _):
        print(f"SOCKETIO: on_hello, so send world_world")
        self.emit("hello_world", "hello_world")

    def on_disconnect(self):
        """Function called when a client disconnects from the WebSocket"""
        print(f"SOCKETIO: Frontend disconnect with SessionId ({self.session_id})")
        self.close()
        get_server().socketio.server.namespace_handlers.pop(f"/frontend/{self.session_id}")

    def on_error(self, error):
        """Function called when an error involving WebSockets occurs"""
        print(f"SocketIO error : {error}")

    def send_error(self, error_id: str, message: str):
        """Sends an error message to be displayed on the frontend"""
        print(f"[SEND ERROR] Sending error message [{message}] to frontend")
        self.emit("server_error", {"id": error_id, "message": message})
