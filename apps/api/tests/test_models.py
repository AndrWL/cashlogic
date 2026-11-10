from pathlib import Path
from api.mono.models import MonoTransaction, format_amount

import json


FIXTURES = Path(__file__).parent / "fixtures"


def make_transactions() -> list[MonoTransaction]:
    statements: list[dict] = json.loads(
        s=(FIXTURES / "statement.json").read_text(encoding="utf-8")
    )

    transactions: list[MonoTransaction] = []

    for statement in statements:
        transaction = MonoTransaction.model_validate(statement)
        transactions.append(transaction)

    return transactions    

def test_parses_all_transactions():
    transactions = make_transactions()
  
    assert len(transactions) == 3   

def test_foreign_currency_transaction():
    transactions = make_transactions()
    foreign_transaction = next(t for t in transactions if t.id == "test-tx-001")

    assert foreign_transaction.currency_code == 840 
    assert foreign_transaction.amount != foreign_transaction.operation_amount

def test_format_amount():
    assert format_amount(-15050) == "-150.50"
    assert format_amount(100) == "1.00"
    assert format_amount(-5) == "-0.05"
    assert format_amount(0) == "0.00"


