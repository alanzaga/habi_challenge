from sqlalchemy import create_engine
from main.config import DATABASE_URI
from main.utils.singleton import singleton


@singleton
class Database:
    """
    Database connection class.
    """

    def __init__(self):
        self.engine = create_engine(DATABASE_URI)
        self.connection = self.engine.connect()

    def get_connection(self):
        """
        Database live connection
        """
        return self.connection
