from typing import List, NamedTuple


class ResponseSchema(NamedTuple):
    type: object
    properties: List[str]


USER_SERVICE_APIKEY_VERIFICATION = ResponseSchema(type=dict, properties=["id", "type"])
