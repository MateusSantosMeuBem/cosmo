ROOT_PATH: str = f'{__path__[0]}/../..'

HEADERS_PATH: str = f'{ROOT_PATH}/data/json/table_headers.json'

XLSX_PATH: str = f'{ROOT_PATH}/data/xlsx/data.xlsx'

voice_models: dict[str, str] = {
    'pt-br': f'{ROOT_PATH}/data/voice_model/pt-br/vosk-model-small-pt-0.3'
}