from fastapi import FastAPI
from .views import (
    whatsapp_account_base_url,
    whatsapp_account_router,
    whatsapp_base_url,
    whatsapp_template_base_url,
    whatsapp_template_router,
    whatsapp_router,
)


def init_api_vi(app: FastAPI):
    app.include_router(
        router=whatsapp_account_router,
        tags=["Account"],
        prefix=whatsapp_account_base_url,
    )
    app.include_router(
        router=whatsapp_router, tags=["Whatsapp Message"], prefix=whatsapp_base_url
    )
    app.include_router(
        router=whatsapp_template_router,
        tags=["Template"],
        prefix=whatsapp_template_base_url,
    )
