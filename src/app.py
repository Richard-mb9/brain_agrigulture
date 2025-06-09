from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from src.commons.errors import APIError
from src.infra.mappers import import_mappers
from src.api.routes import (
    create_routes,
)

URL_PREFIX = ""
API_DOC = f"{URL_PREFIX}/doc/api"
API_DOC_REDOC = f"{URL_PREFIX}/doc/redoc"
API_DOC_JSON = f"{URL_PREFIX}/doc/api.json"
API_VERSION = "V1.0.0"


def create_app():
    import_mappers()

    app = FastAPI(
        title="Brain Agriculture - API",
        description="API for manutencao payments",
        openapi_url=API_DOC_JSON,
        redoc_url=API_DOC_REDOC,
        docs_url=API_DOC,
        version=API_VERSION,
    )
    app.openapi_version = "3.0.2"
    app = create_routes(app, URL_PREFIX)
    return app


app = create_app()


@app.exception_handler(APIError)
def http_exception_handler(request: Request, error: APIError):
    return JSONResponse(
        content={"detail": error.message}, status_code=error.status_code
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    response = {}
    for error in errors:
        key = error["loc"][1]
        response[key] = error["msg"]
    return JSONResponse(
        status_code=HTTPStatus.BAD_REQUEST,
        content={"detail": response},
    )


@app.middleware("http")
async def transaction(request: Request, call_next):
    response = await call_next(request)
    return response
