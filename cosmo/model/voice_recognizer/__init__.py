# --------- External packages ---------
from pandas import DataFrame
import pyaudio
from vosk import Model, KaldiRecognizer

# TYPES
from pyaudio import (
    PyAudio,
    Stream
)
from vosk import (
    KaldiRecognizer,
    Model,
    SetLogLevel
)

# ---------- Built-in packages ----------
import json
import time

# --------- Personal packages ---------
from util.dataframe import (
    search_items
)
from util.file_imports.table_data import (
    table_data
)

from model.voice_recognizer.commands import commands

class VoiceRecognizer:
    BOT_NAME: str = 'Cosmo'
    def __init__(
        self,
        model: Model,
        language: str
    ):
        SetLogLevel(-1)
        self.recognizer: KaldiRecognizer = KaldiRecognizer(
            Model(model[language]),
            16000
        )

        self.capture: PyAudio = pyaudio.PyAudio()
        self.stream: Stream = self.capture.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=8192
        )
        self.stream.start_stream()

    def listening(self):
        print(f'\n[{self.BOT_NAME}] Olá, eu sou o {self.BOT_NAME}, seu bibliotecario pessoal!\nSe precisar de algo, é só chamar meu nome.')
        while True:
            data: bytes = self.stream.read(4096)
            if self.recognizer.AcceptWaveform(data):
                text_data: str = json.loads(self.recognizer.Result())['text'].lower()
                # CALL BOT
                if text_data in commands['bot_name']:
                    print(f'[{self.BOT_NAME}] Escutando...')
                    # [STORE START DATE1]
                    start_time_01: float = time.time()
                    found_command: bool = False
                    while not found_command:
                        
                        data: bytes = self.stream.read(4096)
                        # WAITS 7s AFTER BOT BE CALLED
                        if time.time() - start_time_01 >= 7:
                            print(f'[{self.BOT_NAME}] Vou ficar aqui esperando você me chamar.')
                            break

                        if self.recognizer.AcceptWaveform(data):
                            text_data: str = json.loads(self.recognizer.Result())['text'].lower()
                            print(f'->[VOCÊ] {text_data}')

                            for command, aliases in commands.items():
                                found_command = False

                                if text_data in aliases and command != 'bot_name':
                                    print(f'[{self.BOT_NAME}] Qual {command}?')
                                    found_command = True

                                    # ASK FOT THE SUBSTRING TO SEARCH
                                    while True:
                                        data: bytes = self.stream.read(4096)
                                        if self.recognizer.AcceptWaveform(data):
                                            print(f'->[VOCÊ] {text_data}')
                                            text_data: str = json.loads(self.recognizer.Result())['text'].lower()

                                            # SHOW RESULTS
                                            print(f'[{self.BOT_NAME}] Buscando por "{text_data}" na categoria "{command}"...')
                                            text_data = '-1' if text_data == '' else text_data
                                            search: DataFrame | None = search_items(
                                                data_frame=table_data(),
                                                header_key=command,
                                                substring=text_data
                                            )
                                            if type(search) == DataFrame:
                                                if not search.empty:
                                                    print()
                                                    print(search)
                                                    print()
                                                else:
                                                    print(f'[{self.BOT_NAME}] Putz! Não achei nada pra essa pesquisa.')
                                            else:
                                                print(f'[{self.BOT_NAME}] Putz! Não achei nada pra essa pesquisa.')
                                            print(f'[{self.BOT_NAME}] Vou ficar aqui esperando você me chamar.')
                                                

                                            break


                                    break