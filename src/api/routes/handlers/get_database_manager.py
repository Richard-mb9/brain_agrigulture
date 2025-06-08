from fastapi import Request
from src.infra import DatabaseManager


def get_database_manager(request: Request) -> DatabaseManager:  # type: ignore
    db_manager = DatabaseManager()

    yield db_manager
    db_manager.close_session()
