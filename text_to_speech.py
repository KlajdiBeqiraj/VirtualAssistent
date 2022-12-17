import os
import pyttsx3
from gtts import gTTS

def text_to_speech_gttps(mytext, lang="en", file_path=''):
    audio = gTTS(text=mytext, lang=lang, slow=False)
    audio.save(file_path)
    os.system("start " + file_path)

def text_to_speech_pyttsx3(mytext):
    pyttsx3.init(driverName='sapi5')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(mytext)
    engine.runAndWait()