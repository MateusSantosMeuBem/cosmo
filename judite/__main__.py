# ---------- External packages ----------
import pandas as pd

# ---------- Built-in packages ----------
import json

# ---------- Personal packages ----------
from util import ROOT_PATH
from util.dataframe import (
    seach_items
)

# ---------- IMPORT TABLE HEADERS ----------
headers_path: str = f'{ROOT_PATH}/data/json/table_headers.json'
with open(headers_path, 'r', encoding='utf-8') as headers_as_json:
    table_headers: dict[str, list[str]] = json.load(headers_as_json)

# ---------- IMPORT TABLE DATA FILE ----------
xlsx_path: str = f'{ROOT_PATH}/data/xlsx/data.xlsx'
df_table = pd.read_excel(
    io=xlsx_path,
    sheet_name='livros'
)
