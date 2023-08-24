import uuid
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.enums import RegularExpression


class PlaceHolderSchema(BaseModel):
    key: str
    description: str
    is_sensitive: bool = Field(default=False)


class WhatsappTemplateSchema(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    sender_id: uuid.UUID
    placeholders: Optional[List[PlaceHolderSchema]]
    content: str
    created_by: uuid.UUID
    created_at: datetime
    updated_by: uuid.UUID
    updated_at: datetime
    is_deleted: bool
    deleted_by: Optional[uuid.UUID]
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True


class CreateTemplateSchema(BaseModel):
    placeholders: Optional[List[PlaceHolderSchema]]
    content: str
    whatsapp_id: str


class UpdateTemplateSchema(BaseModel):
    template_id: uuid.UUID
    placeholders: Optional[List[PlaceHolderSchema]]
    content: Optional[str]
    whatsapp_id: str
