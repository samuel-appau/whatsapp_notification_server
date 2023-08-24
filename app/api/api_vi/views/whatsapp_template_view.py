import uuid

import pinject
from fastapi import APIRouter, Depends, status

from app.controllers import WhatsappTemplateController
from app.repositories import WhatsappTemplateRepository
from app.schema import (
    CreateTemplateSchema,
    WhatsappTemplateSchema,
    UpdateTemplateSchema,
)
from app.utils import Page, Params

whatsapp_template_router = APIRouter()
whatsapp_template_base_url = "/api/v1/whatsapp/template"

obj_graph = pinject.new_object_graph(
    modules=None,
    classes=[WhatsappTemplateController, WhatsappTemplateRepository],
)
whatsapp_template_controller: WhatsappTemplateController = obj_graph.provide(
    WhatsappTemplateController
)


current_user = {"id": uuid.uuid4()}


@whatsapp_template_router.post(
    "", response_model=WhatsappTemplateSchema, status_code=status.HTTP_201_CREATED
)
def create_template(payload: CreateTemplateSchema) -> WhatsappTemplateSchema:
    result = whatsapp_template_controller.create_template(
        auth_user=current_user, obj_data=payload.dict()
    )
    return result


@whatsapp_template_router.get("", response_model=Page[WhatsappTemplateSchema])
def get_all_templates(
    pagination: Params = Depends(),
) -> Page[WhatsappTemplateSchema]:  # noqa
    result = whatsapp_template_controller.get_all_templates(pagination=pagination)
    return result


@whatsapp_template_router.get("/{id}", response_model=WhatsappTemplateSchema)
def get_template(id: uuid.UUID) -> WhatsappTemplateSchema:
    result = whatsapp_template_controller.get_template(
        auth_user=current_user, obj_id=str(id)
    )
    return result


@whatsapp_template_router.put("", response_model=WhatsappTemplateSchema)
def update_template(payload: UpdateTemplateSchema) -> WhatsappTemplateSchema:
    result = whatsapp_template_controller.update_template(
        auth_user=current_user, obj_data=payload.dict()
    )
    return result


@whatsapp_template_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_template(id: uuid.UUID) -> None:
    result = whatsapp_template_controller.delete_template(  # noqa
        auth_user=current_user, obj_id=str(id)
    )
    return result
