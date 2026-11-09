from api.core.config import config
from pathlib import Path

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


def save_json(data: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    client_info: dict = fetch_client_info()
    save_json(client_info, Path("data/client_info.json"))