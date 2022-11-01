# ---------- External packages ----------
from dotenv import load_dotenv
import pandas as pd

# TYPES
from pandas.core.frame import DataFrame

# --------------- BUILT-IN PACKAGES ---------------
import os

# ---------- Personal packages ----------
from util.path import (
    XLSX_PATH
)
def table_data() -> DataFrame:
    load_dotenv()

    return pd.read_excel(
        io=XLSX_PATH,
        sheet_name=os.getenv('sheet_name')
    )