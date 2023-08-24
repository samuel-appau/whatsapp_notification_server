from app import api
from fastapi.responses import RedirectResponse
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi_pagination import add_pagination
from sqlalchemy.exc import DBAPIError
from config import settings
from logging.config import dictConfig
from pathlib import Path
from fastapi.exceptions import RequestValidationError
from fastapi_pagination import add_pagination
from app.core.exceptions import  AppExceptionCase, app_exception_handler
from app.core.log import log_config
from app.services import RedisService


APP_ROOT = Path(__file__).parent.parent

dictConfig(log_config())


def create_app():
    app = FastAPI(
        title="Sample Whatsapp Notification Server",
        description="A simple cloaked notification server ",
        version="0.0.1",
    )
    register_api_routers(app)
    register_middlewares(app)
    register_extensions(app)
    return app


def register_api_routers(app: FastAPI):
    api.init_api_vi(app)

    @app.get("/", include_in_schema=False)
    def index():
        return RedirectResponse("/docs")

    return None


def register_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins.split("|"),
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return None


def register_extensions(app: FastAPI):
    add_pagination(app)

    @app.exception_handler(HTTPException)
    def handle_http_exception(request, exc):
        return app_exception_handler.http_exception_handler(exc)

    @app.exception_handler(DBAPIError)
    def handle_db_exception(request, exc):
        return app_exception_handler.db_exception_handler(exc)

    @app.exception_handler(AppExceptionCase)
    def handle_app_exceptions(request, exc):
        return app_exception_handler.app_exception_handler(exc)

    @app.exception_handler(RequestValidationError)
    def handle_validation_exceptions(request, exc):
        return app_exception_handler.validation_exception_handler(exc)

    return None
