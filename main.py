import os

from gtp3 import GPT_Completion
from speech_to_text import speech_to_text
from text_to_speech import text_to_speech_gttps

FILES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "files")


def main():
    language = "en"
    duration = 5

    os.makedirs(FILES_DIR, exist_ok=True)
    file_path = os.path.join(FILES_DIR, "example.mp3")

    in_text = speech_to_text(duration=duration, language=language)
    out_text = GPT_Completion(in_text)
    text_to_speech_gttps(out_text, lang=language, file_path=file_path)


if __name__ == "__main__":
    main()
