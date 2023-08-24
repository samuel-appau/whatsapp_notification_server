from app.core.repository import SQLBaseRepository
from app.models import WhatsappDeliveryReportModel


class WhatsappDeliveryReportRepository(SQLBaseRepository):
    model = WhatsappDeliveryReportModel
