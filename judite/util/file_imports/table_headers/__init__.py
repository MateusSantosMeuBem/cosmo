# ---------- Built-in packages ----------
import json

# ---------- Personal packages ----------
from util.path import (
    HEADERS_PATH,
)
def table_headers() -> dict[str, list[str]]:
    with open(
        HEADERS_PATH, 'r',
        encoding='utf-8'
    ) as headers_as_json:
        return json.load(headers_as_json)