from app.core.repository import SQLBaseRepository
from app.models import WhatsappAccountModel


class WhatsappAccountRepository(SQLBaseRepository):
    model = WhatsappAccountModel
