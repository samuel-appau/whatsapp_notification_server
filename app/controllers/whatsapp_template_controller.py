from datetime import datetime
from app.core.exceptions import AppException
from app.models import WhatsappTemplateModel
from app.repositories import WhatsappTemplateRepository
from config import settings


class WhatsappTemplateController:
    def __init__(self, whatsapp_template_repository: WhatsappTemplateRepository):
       ...