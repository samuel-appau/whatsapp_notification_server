from fastapi import APIRouter


whatsapp_account_router = APIRouter()
whatsapp_account_base_url = "/api/v1/whatsapp/account"


@whatsapp_account_router.get("")
def get_all_whatsapp_account():
    result = {}
    return result


@whatsapp_account_router.post("")
def register_whatsapp_account():
    result = {}
    return result


@whatsapp_account_router.post("")
def verify_whatsapp_account():
    result = {}
    return result
