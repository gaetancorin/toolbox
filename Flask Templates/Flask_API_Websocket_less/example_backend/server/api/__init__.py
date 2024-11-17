from flask_restx import Api

main_api = Api(version="1.0", title="Backend API")


SERVER = None

def set_server(server):
    """Set the global SERVER"""
    global SERVER  # pylint: disable=global-statement
    SERVER = server


def get_server():
    """Return the global SERVER"""
    return SERVER
