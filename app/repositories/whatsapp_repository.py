from app.core.repository import SQLBaseRepository
from app.models import WhatsappModel


class WhatsappRepository(SQLBaseRepository):
    model = WhatsappModel
