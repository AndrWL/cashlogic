from decimal import Decimal
from unittest import result
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class Account(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, hide_input_in_errors=True)

    id: str
    send_id: str
    currency_code: int
    cashback_type: str | None = None
    balance: int
    credit_limit: int
    masked_pan: list[str]
    type: str
    iban: str

class ClientInfo(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, hide_input_in_errors=True)

    client_id: str
    name: str
    web_hook_url: str
    permissions: str
    accounts: list[Account]    


def format_amount(kopecks: int) -> str:
    value = Decimal(kopecks)
    value /= 100
    return f"{value:.2f}"

print(format_amount(100011))