import requests
from requests.exceptions import RequestException

from app.core.exceptions import AppException
from app.core.service_interfaces import WhatsappAttribute, WhatsappServiceInterface
from app.enums import WhatsappDeliveryStatuEnum
from config import settings


class SmsProviderMnotify(SMSServiceInterface):
    client = "Mnotify"

    def __init__(self):
        self.api_key = settings.mnotify_api_key

    def send(self, sms_attribute: SmsAttribute):
        recipient = sms_attribute.get("recipient")
        recipients = sms_attribute.get("recipients")
        if not recipient and not recipients:
            return SmsDeliveryStatuEnum.not_sent_to_provider, "no recipient found", 0
        return self.single_recipient(
            sender=sms_attribute.get("sender"),
            recipient=recipient if recipient else recipients[0],
            message=sms_attribute.get("message"),
        )

    def single_recipient(self, sender: str, recipient: str, message: str):
        endpoint = f"https://apps.mnotify.net/smsapi?key={self.api_key}&to={recipient}&msg={message}&sender_id={sender}"  # noqa
        try:
            return self._make_request(endpoint=endpoint, total_recipients=1)
        except RequestException as exc:
            raise AppException.OperationError(
                error_message=(SmsDeliveryStatuEnum.not_sent_to_provider, exc, 1),
                context=f"{self.client} exception: {exc}",
            )

    # noinspection PyMethodMayBeStatic
    def _make_request(self, endpoint: str, total_recipients: int):
        response = requests.get(url=endpoint)
        response_data = response.json()
        if response_data.get("code") != "1000":
            raise AppException.OperationError(
                error_message=(
                    SmsDeliveryStatuEnum.sent_to_provider,
                    response_data,
                    total_recipients,
                ),
                context=response_data,
            )
        return SmsDeliveryStatuEnum.sent_to_provider, response_data, total_recipients

    # noinspection PyMethodMayBeStatic
    def send_in_batches(self, recipients: list, size: int):
        for _ in range(0, len(recipients), size):
            batch = recipients[_ : size + _]
            yield batch
