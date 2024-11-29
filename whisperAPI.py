import pywhisper as whisper
import logging, sys
import time

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def load_audio(audio_bytes):
    audio = whisper.load_audio(audio_bytes)

    return audio


def load_model(modelName):
    models = ["tiny", "base", "small", "medium", "large"]

    if modelName in models:
        model = whisper.load_model(modelName)

        logging.info(modelName + " model loaded")
    else:
        logging.warning("model entered is not valid. Model must be one of " + " ".join(models) + ". Auto loading base model now")
        
        model = whisper.load_model("base")

    return model


def transcribe_audio(model, audio_file_path):
    transcribed_text = model.transcribe(audio_file_path)

    return transcribed_text

  


#Testing
if __name__ == "__main__":
    load_model("tiny")