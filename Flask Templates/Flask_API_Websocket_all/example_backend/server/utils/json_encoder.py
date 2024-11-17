from bson import ObjectId
from flask.json import JSONEncoder


class JsonEncoder(JSONEncoder):
    """Custom JsonEncoder to use instead of the one included with Flask"""

    def default(self, o):
        """Called when converting an object to JSON (dict)"""
        if hasattr(o, "to_dict"):
            return o.to_dict()
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)
