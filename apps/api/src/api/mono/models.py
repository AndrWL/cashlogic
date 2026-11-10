from datetime import datetime
from unittest import result
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from decimal import Decimal


class MonoAccount(BaseModel):
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

class MonoClientInfo(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, hide_input_in_errors=True)

    client_id: str
    name: str
    web_hook_url: str
    permissions: str
    accounts: list[MonoAccount]    

class MonoTransaction(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, hide_input_in_errors=True)

    id: str
    time: datetime
    description: str
    mcc: int
    amount: int
    operation_amount: int
    currency_code: int
    commission_rate: int | None = None
    cashback_amount: int | None = None
    balance: int
    hold: bool
    comment: str | None = None
    receipt_id: str | None = None

def format_amount(kopecks: int) -> str:
    value = Decimal(kopecks) / 100

    return f"{value:.2f}"