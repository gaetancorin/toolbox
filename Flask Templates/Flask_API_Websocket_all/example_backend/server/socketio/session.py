import uuid


class Session:
    """Track a connected client (frontend and benches) session"""

    def __init__(self):
        """Init a session with a random UUID (uuid4) and adding it to the session list Sessions"""
        self._session_id = uuid.uuid4()

    @property
    def session_id(self) -> uuid.UUID:
        """Returns the session ID"""
        return self._session_id

    def close(self):
        """Closes the session"""
        del self
