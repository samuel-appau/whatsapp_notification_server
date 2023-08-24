import enum


class WhatsappDeliveryStatuEnum(enum.Enum):
    """
    Enumeration representing the status of whatsapp.

    :ivar sent_to_provider: sent_to_provider whatsapp status.
    :vartype sent_to_provider: str
    :ivar sent_to_user: sent_to_user whatsapp status.
    :vartype sent_to_user : str
    :ivar not_sent_to_provider : not_sent_to_provider whatsapp status.
    :vartype not_sent_to_provider: str
    :ivar not_sent_to_user: not_sent_to_user whatsapp status.
    :vartype not_sent_to_user: str
    """

    sent_to_provider = "sent_to_provider"
    sent_to_user = "sent_to_user"
    not_sent_to_provider = "not_sent_to_provider"
    not_sent_to_user = "not_sent_to_user"


class RegularExpression(enum.Enum):
    phone_number = r"(((02)[03467]|(05)[045679])\d{7}$)|((\+233)((2)[03467]|(5)[045679])\d{7}$)" 
    placeholder = r"^(\d|\w)+$"
