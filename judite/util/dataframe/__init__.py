# ---------- External packages ----------


# TYPES
from pandas.core.frame import (
    DataFrame
)

# ---------- Built-in packages ----------
import json

# ---------- Personal packages ----------
from util import ROOT_PATH

def get_header(
    header_key: str
) -> str | None:
    """
    [IMPLEMENTS]
    """
    headers_path: str = f'{ROOT_PATH}/data/json/table_headers.json'
    with open(headers_path, 'r', encoding='utf-8') as headers_as_json:
        table_headers: dict[str, list[str]] = json.load(headers_as_json)

    for header, header_aliases in table_headers.items():
        if header_key in header_aliases: return header

    return None

def seach_items(
    data_frame: DataFrame,
    header_key: str,
    substring: str
) -> DataFrame | None:
    """
    Search rows with specific  substring in a column of a DataFrame.

    Parameters
    ----------
    data_frame : DataFrame
        DataFrame where to search.
    header_key : str
        Column name in the DataFrame where serch for item.
    substring : str
        Substring value to be found.

    Returns
    -------
    DataFrame
        Result of the search.
    
    """

    header_key = get_header(header_key.lower())

    if header_key:
        # Makes a copy of original dataframe, but with its columns in lower case
        lower_dataframe: DataFrame = data_frame.copy()
        lower_dataframe.columns = data_frame.columns.str.lower()

        return data_frame[
            lower_dataframe[header_key.lower()]
            .apply(str)
            .str.lower()
            .str.contains(substring)
        ]
    else:
        return None