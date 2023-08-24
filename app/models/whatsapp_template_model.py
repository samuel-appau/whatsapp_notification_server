import json
import uuid

import sqlalchemy as sa

from app.core.database import Base
from app.utils import GUID


class WhatsappTemplateModel(Base):
    __tablename__ = "templates"
    id = sa.Column(GUID, primary_key=True, default=uuid.uuid4)
    user_id = sa.Column(GUID, nullable=False, index=True)
    file_id = sa.Column(sa.String)
    _placeholders = sa.Column("placeholders", sa.String)
    created_by = sa.Column(GUID, nullable=False)
    created_at = sa.Column(
        sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()
    )
    updated_by = sa.Column(GUID, nullable=False)
    updated_at = sa.Column(
        sa.DateTime(timezone=True),
        nullable=False,
        server_default=sa.func.now(),
        onupdate=sa.func.now(),
    )
    is_deleted = sa.Column(sa.Boolean, nullable=False, default=False)
    deleted_by = sa.Column(GUID)
    deleted_at = sa.Column(sa.DateTime)

    @property
    def placeholders(self):
        return json.loads(self._placeholders) if self._placeholders else None

    @placeholders.setter
    def placeholders(self, value):
        self._placeholders = json.dumps(value)
