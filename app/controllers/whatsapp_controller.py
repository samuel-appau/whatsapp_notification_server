from datetime import datetime
from app.core.exceptions import AppException
from app.models import WhatsappModel
from app.repositories import WhatsappTemplateRepository
from config import settings


class WhatsappController:
    def __init__(self, whatsapp_template_repository: WhatsappTemplateRepository):
        ...
