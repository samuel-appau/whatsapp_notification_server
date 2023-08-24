from app.core.exceptions import AppException
from app.enums import RegularExpression

def validate_phone_number(phone_number: str):
    # reminder: split regex into local and international format
    split_regex = RegularExpression.phone_number.value.split("|")
    # reminder: check if phone number is in local format
    local_format = re.fullmatch("|".join(split_regex[:2]), phone_number)
    # reminder: check if phone number is in international format
    international_format = re.fullmatch("|".join(split_regex[2:]), phone_number)
    if not local_format and not international_format:
        raise AppException.ValidationException(
            error_message="invalid phone number format"
        )
    # reminder: convert local format to international format
    if local_format:
        phone_number = re.sub(r"^0", "+233", phone_number)
    return phone_number


def remove_none_fields(data: dict):
    data = {key: value for key, value in data.items() if value is not None}
    return data


def validate_optional_fields(optional_fields: list, data):
    optional = False
    for field in optional_fields:
        if getattr(data, field, None):
            optional = True
    if not optional:
        raise AppException.ValidationException(
            error_message="optional field must be set"
        )
    return data
