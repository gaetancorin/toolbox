from example_backend import __version__
from example_backend.server.api import set_server as set_server_api
from example_backend.server.server import WebServer
from flask import make_response

version = __version__


def create_server() -> WebServer:
    """
    Returns a server with assigned routes to it
    :return: server
    """
    _server = WebServer()
    set_server_api(_server)

    @_server.app.route("/")
    def _index():
        """
        Route to the index page.
        :return: str
        """
        return make_response("Connecting on server", 200)

    @_server.app.after_request
    def _add_header(response):
        """
        Add 'Access-Control-Allow-Origin=*' header to a given response.
        :param response: Response to add header to.
        :return: response with header added.
        """
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "*"
        return response

    return _server


server = create_server()

if __name__ == "__main__":
    server.start_server()
