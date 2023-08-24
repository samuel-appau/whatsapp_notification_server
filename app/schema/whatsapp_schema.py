import uuid
from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel, model_validator, validator
from app.utils import (
    remove_none_fields,
    validate_optional_fields,
    validate_phone_number,
)
from .dynamic_schema import FieldAttribute, new_field

class WhatsappSchema(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    sender: str
    recipient: str
    message: str
    is_scheduled: Optional[bool]
    scheduled_date: Optional[datetime]
    delivery_report: Any
    created_by: uuid.UUID
    created_at: datetime

    _phone_validator = validator("recipient", allow_reuse=True)(validate_phone_number)

    @model_validator(mode="before")
    def additional_fields(cls, values):  # noqa
        new_field(
            orm_object=values,
            field_attr=[
                FieldAttribute(
                    field="delivery_report", properties=[], method="get_delivery_report"
                ),
            ],
        )
        return values
    class Config:
        orm_mode = True


class SendWhatsappSchema(BaseModel):
    sender: str
    recipient: str
    message: str
    is_scheduled: Optional[bool]
    scheduled_date: Optional[datetime]

    _phone_validator = validator("recipient", allow_reuse=True)(validate_phone_number)

    @model_validator(mode="after")
    def optional_fields(cls, values):  # noqa
        validate_optional_fields(
            optional_fields=["is_scheduled", "scheduled_at"], data=values
        )
        return values



class WhatsappTemplateSchema(BaseModel):
    sender: Optional[str]
    recipient: str
    is_scheduled: Optional[bool]
    scheduled_date: Optional[datetime]
    template_id: uuid.UUID
    keywords: Optional[dict]

    _phone_validator = validator("recipient", allow_reuse=True)(validate_phone_number)
    
    @model_validator(mode="after")
    def optional_fields(cls, values):  # noqa
        validate_optional_fields(
            optional_fields=["is_scheduled","scheduled_date","keywords"], data=values
        )
        return values

