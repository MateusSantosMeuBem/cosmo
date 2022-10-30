# ---------- External packages ----------
import pandas as pd

# TYPES
from pandas.core.frame import DataFrame

# ---------- Personal packages ----------
from util.path import (
    XLSX_PATH
)
def table_data() -> DataFrame:
    return pd.read_excel(
        io=XLSX_PATH,
        sheet_name='livros'
    )