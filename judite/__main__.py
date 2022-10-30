# ---------- External packages ----------

# ---------- Built-in packages ----------

# ---------- Personal packages ----------
from model.voice_recognizer import (
    VoiceRecognizer
)
from util.path import (
    voice_models
)

voice_recognizer = VoiceRecognizer(
    model=voice_models,
    language='pt-br'
)
voice_recognizer.listening()