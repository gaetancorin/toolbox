from flask import url_for
from flask_restx import Api


# class MainApi(Api):
#     """Handle request on /"""
#
#     @property
#     def specs_url(self):
#         """
#         The Swagger specifications absolute url (ie. `swagger.json`)
#         :rtype: str
#         """
#         return url_for(self.endpoint("specs"), _external=False)
#
#
main_api = Api(version="1.0", title="Fute Rest API")


SERVER = None


def set_server(server):
    """Set the global SERVER"""
    global SERVER  # pylint: disable=global-statement
    SERVER = server


def get_server():
    """Return the global SERVER"""
    return SERVER
