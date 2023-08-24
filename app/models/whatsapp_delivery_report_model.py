import uuid

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

from app.core.database import Base
from app.utils import GUID


class WhatsappDeliveryReportModel(Base):
    __tablename__ = "delivery_reports"
    id = sa.Column(GUID, primary_key=True, default=uuid.uuid4)
    whatsapp_id = sa.Column(GUID, nullable=False, index=True)
    provider = sa.Column(sa.String)
    total_recipients = sa.Column(
        sa.Integer, nullable=False, default=0, server_default="0"
    )
    comment = sa.Column(JSONB)
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
