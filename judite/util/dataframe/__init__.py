# ---------- External packages ----------


# TYPES
from re import sub
from pandas.core.frame import (
    DataFrame
)

# ---------- Personal packages ----------
from util.file_imports.table_headers import (
    table_headers
)

def get_header(
    header_key: str
) -> str | None:
    """
    [IMPLEMENTS]
    """
    headers: dict[str, list[str]] = table_headers()

    for header, header_aliases in headers.items():
        if header_key in header_aliases: return header

    return None

def search_items(
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

    header_key: str = get_header(header_key.lower())

    if header_key:
        # Make a copy of original dataframe, but with its columns in lower case
        lower_dataframe: DataFrame = data_frame.copy()
        lower_dataframe.columns = data_frame.columns.str.lower()
        
        return data_frame[
            lower_dataframe[header_key.lower()]
            .apply(str)
            .str.lower()
            .str.contains(substring.lower())
        ]
    else:
        return None