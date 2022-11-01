# --------------- EXTERNAL PACKAGES ---------------
from dotenv import load_dotenv, find_dotenv, set_key

# --------------- BUILT-IN PACKAGES ---------------
import os

load_dotenv()

ROOT_PATH: str = f'{__path__[0]}/../..'

HEADERS_PATH: str = f'{ROOT_PATH}/data/json/table_headers.json'

XLSX_PATH: str = os.getenv('database_file_path')

voice_models: dict[str, str] = {
    'pt-br': f'{ROOT_PATH}/data/voice_model/pt-br/vosk-model-small-pt-0.3'
}