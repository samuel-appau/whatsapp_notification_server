from app.core.repository import SQLBaseRepository
from app.models import WhatsappTemplateModel


class WhatsappTemplateRepository(SQLBaseRepository):
    model = WhatsappTemplateModel
