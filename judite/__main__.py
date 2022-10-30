# ---------- Built-in packages ----------
import json

# ---------- Personal packages ----------
from util import ROOT_PATH

headers_path: str = f'{ROOT_PATH}/data/json/table_headers.json'
with open(headers_path, 'r', encoding='utf-8') as headers_as_json:
    table_headers: dict[str, list[str]] = json.load(headers_as_json)
