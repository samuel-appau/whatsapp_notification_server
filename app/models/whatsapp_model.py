import uuid

import sqlalchemy as sa

from app.core.database import Base, get_db_session
from app.utils import GUID

from .whatsapp_delivery_report_model import WhatsappDeliveryReportModel


class WhatsappModel(Base):
    __tablename__ = "whatsapp"
    id = sa.Column(GUID, primary_key=True, default=uuid.uuid4)
    user_id = sa.Column(GUID, nullable=False, index=True)
    sender = sa.Column(sa.String, nullable=False, index=True)
    sender_name = sa.Column(sa.String, nullable=False, index=True, server_default="")
    recipient = sa.Column(sa.String, nullable=False, index=True)
    subject = sa.Column(sa.String, nullable=False)
    html_body = sa.Column(sa.String, nullable=False)
    text_body = sa.Column(sa.String)
    is_scheduled = sa.Column(sa.Boolean, default=False)
    scheduled_date = sa.Column(sa.DateTime(timezone=True))
    created_by = sa.Column(GUID, nullable=False)
    created_at = sa.Column(
        sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()
    )

    def get_delivery_report(self) -> WhatsappDeliveryReportModel:
        with get_db_session() as db_session:
            result = (
                db_session.query(WhatsappDeliveryReportModel)
                .filter(WhatsappDeliveryReportModel.whatsapp_id == self.id)
                .first()
            )
        return result
