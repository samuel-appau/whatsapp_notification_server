import uuid

import pinject
from fastapi import APIRouter, Depends

from app.controllers import WhatsappController, WhatsappTemplateController
from app.repositories import (
    WhatsappDeliveryReportRepository,
    WhatsappRepository,
    WhatsappTemplateRepository,
)
from app.schema import SendWhatsappSchema, WhatsappSchema, WhatsappTemplateSchema
from app.utils import Page, Params

whatsapp_router = APIRouter()
whatsapp_base_url = "/api/v1/whatsapp"

obj_graph = pinject.new_object_graph(
    modules=None,
    classes=[
        WhatsappController,
        WhatsappRepository,
        WhatsappDeliveryReportRepository,
        WhatsappTemplateController,
        WhatsappTemplateRepository,
    ],
)
whatsapp_controller: WhatsappController = obj_graph.provide(WhatsappController)

current_user = {"id": uuid.uuid4()}


@whatsapp_router.post("/")
def send_whatsapp(payload: SendWhatsappSchema) -> dict:
    result = whatsapp_controller.send_whatsapp(
        auth_user=current_user, obj_data=payload.dict()
    )
    return result


@whatsapp_router.get("/", response_model=Page[WhatsappSchema])
def get_all_whatsapp(pagination: Params = Depends()) -> Page[WhatsappSchema]:  # noqa
    result = whatsapp_controller.get_all_whatsapp(
        auth_user=current_user, pagination=pagination
    )
    return result


@whatsapp_router.get("/{id}", response_model=WhatsappSchema)
def get_whatsapp(id: uuid.UUID) -> WhatsappSchema:
    result = whatsapp_controller.get_whatsapp(auth_user=current_user, obj_id=str(id))
    return result


@whatsapp_router.post("/template")
def send_whatsapp_with_template(payload: WhatsappTemplateSchema):
    result = whatsapp_controller.send_whatsapp_with_template(
        auth_user=current_user, obj_data=payload.dict()
    )
    return result
