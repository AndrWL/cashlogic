from api.core.config import config
from pathlib import Path
from datetime import datetime, timedelta

import httpx
import json

def fetch_client_info() -> dict:
    response = httpx.get(
        url="https://api.monobank.ua/personal/client-info",
        headers={"X-Token": config.MONO_TOKEN.get_secret_value()},
        timeout=10
    )

    response.raise_for_status()

    return response.json()

def fetch_statement(account_id: str, date_from: datetime, date_to: datetime) -> list[dict]:
    date_from_value = int(date_from.timestamp())
    date_to_value = int(date_to.timestamp())

    response = httpx.get(
        url=f"https://api.monobank.ua/personal/statement/{account_id}/{date_from_value}/{date_to_value}",
        headers={"X-Token": config.MONO_TOKEN.get_secret_value()},
        timeout=10
    )

    response.raise_for_status()

    return response.json()

def save_json(data: dict | list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    client_info: dict = fetch_client_info()
    save_json(client_info, Path("data/client_info.json"))

    now = datetime.now()
    month_ago = now - timedelta(days=30)
    statement = fetch_statement(client_info["accounts"][0]["id"], date_from=month_ago, date_to=now)
    save_json(statement, Path("data/statement.json"))