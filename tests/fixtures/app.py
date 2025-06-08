# pylint: disable=W0102
# pylint: disable=W0221
# pylint: disable=W0613


from http import HTTPStatus
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.testclient import TestClient
import pytest

from src.app import create_app
from src.commons.errors import APIError


class Client(TestClient):
    """Client to test the api"""

    def __init__(self, app: FastAPI):
        super().__init__(app)

    def get(self, url: str, headers: dict = {}, params: dict = {}):
        return super().get(url=url, headers=headers, params=params)

    def post(self, url: str, data: dict = {}, headers: dict = {}, params: dict = {}):
        return super().post(url=url, data=data, headers=headers, params=params)

    def put(self, url: str, data: dict = {}, headers: dict = {}, params: dict = {}):
        return super().put(url=url, data=data, headers=headers, params=params)

    def delete(self, url: str, headers: dict = {}, params: dict = {}):
        return super().delete(url=url, headers=headers, params=params)


@pytest.fixture(scope="session")
def client():
    app = create_app()

    @app.exception_handler(APIError)
    def http_exception_handler(request: Request, error: APIError):
        return JSONResponse(
            content={"detail": error.message}, status_code=error.status_code
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        errors = exc.errors()
        response = {}
        for error in errors:
            key = error["loc"][1]
            response[key] = error["msg"]
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={"detail": response},
        )

    # config.main(argv=["--raiseerr", "upgrade", "head"])
    yield Client(app)
