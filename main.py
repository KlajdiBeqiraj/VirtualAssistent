import os

from VirtualAssistantGTP.gtp3 import GPT_Completion
from VirtualAssistantGTP.speech_to_text import speech_to_text
from VirtualAssistantGTP.text_to_speech import text_to_speech_gttps


def main():
    # text_to_speech()
    language = "en"
    duration = 5
    file_path = r"C:\Users\klajd\PycharmProjects\BekzProjects\VirtualAssistantGTP\files\example.mp3"

    in_text = speech_to_text(duration=duration, language=language)
    out_text = GPT_Completion(in_text)
    text_to_speech_gttps(out_text, lang=language, file_path=file_path)

if __name__ == "__main__":
    main()