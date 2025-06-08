from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

from src.config import HOST_DB, PASSWORD_DB, USER_DB, PORT_DB, NAME_DB


class DatabaseManager:
    """class to manage database connection"""

    def __init__(self):
        self.url_db = (
            f"postgresql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{NAME_DB}"
        )
        self.engine = create_engine(self.url_db, pool_size=25, max_overflow=10)
        self.session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.get_engine())
        )
        self.metadata = MetaData()

    def get_engine(self):
        return self.engine

    def get_session(self):
        return self.session

    def close_session(self):
        self.session.close()

    def get_url_db(self):
        return self.url_db
