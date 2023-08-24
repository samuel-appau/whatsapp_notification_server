import abc
from typing import List, TypedDict


class WhatsappAttribute(TypedDict):
    sender: str
    recipient: str
    # recipients: List[str]
    message: str


class WhatsappServiceInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            (hasattr(subclass, "send"))
            and callable(subclass.send)
            and hasattr(subclass, "client")
        )

    @property
    def client(self):
        raise NotImplementedError

    @abc.abstractmethod
    def send(self, whatsapp_attribute: WhatsappAttribute):
        raise NotImplementedError
