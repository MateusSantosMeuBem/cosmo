# --------- External packages ---------
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
)

# ---------- Built-in packages ----------
import json

# --------- Personal packages ---------
from util.path import (
    voice_models
)
from model.voice_recognizer.commands import commands

class VoiceRecognizer:
    def __init__(
        self,
        model: Model,
        language: str
    ):
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
        # [CLEANING TERMINAL FALLOWING THE OS]
        while True:
            data: bytes = self.stream.read(4096)
            if self.recognizer.AcceptWaveform(data):
                text_data: str = json.loads(self.recognizer.Result())['text'].lower()
                if text_data in commands['bot_name']:
                    print('Olá! Eu sou a Judite, sua bibliotecaria pessoal!')
                print(text_data)