import re
from typing import List, NamedTuple

from pydantic import create_model

from app.core.exceptions import AppException
from app.enums import RegularExpression


def phone_validator(cls, v, values, **kwargs):
    if not re.match(RegularExpression.phone_number.value, v):
        raise AppException.ValidationException(error_message="invalid email format")
    return v


def generate_dynamic_schema(base_schema, **fields):
    """
    Generate a dynamic Pydantic schema based on a base schema and additional fields.

    :param base_schema: The base schema to inherit from.
    :type base_schema: type(BaseModel)
    :param **fields: Additional fields to include in the schema.
    :type **fields: Any
    :return: The dynamically generated schema.
    :rtype: type(BaseModel)
    """
    schema = create_model("CustomSchema", **fields, __base__=base_schema)
    return schema


class FieldAttribute(NamedTuple):
    """
    Represents a field attribute.
    :param method: The name of the method associated with the field attribute.
    :type method: Union[str, None]
    :param fields: List of fields associated with the attribute.
    :type fields: List
    """

    method: str
    field: str
    properties: List[str]


def new_field(field_attr: List[FieldAttribute], orm_object):
    for attr in field_attr:
        setattr(orm_object, attr.field, getattr(orm_object, attr.method)())
    return orm_object


def new_properties(field_attr: List[FieldAttribute], orm_object):
    for attr in field_attr:
        return_value = getattr(orm_object, attr.method)()
        for prop in attr.properties:
            setattr(orm_object, prop, getattr(return_value, prop))
    return orm_object


def exclude_fields(fields: List[str]):
    """
    Generate a dictionary with field names as keys and exclusion flag set to True.

    :param fields: The list of field names to exclude.
    :type fields: List[str]
    :return: A dictionary with field names as keys and exclusion flag set to True.
    :rtype: Dict[str, Dict[str, bool]]
    """
    return {field: {"exclude": True} for field in fields}
