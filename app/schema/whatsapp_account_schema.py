import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AccountSchema(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    phone_number: str
    sender_name: Optional[str]
    is_default: bool
    created_by: uuid.UUID
    created_at: datetime
    updated_by: uuid.UUID
    updated_at: datetime
    is_deleted: bool
    deleted_by: Optional[uuid.UUID]
    deleted_at: Optional[datetime]

    class Config:
        from_attributes = True
