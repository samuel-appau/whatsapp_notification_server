import uuid
from pydantic import BaseModel


class DeliveryReportSchema(BaseModel):
    id: uuid.UUID
    whatsapp_id: uuid.UUID

    class Config:
        from_attributes = True
