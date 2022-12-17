import speech_recognition as sr

def speech_to_text(duration=5, language="en"):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print('start recognizing')
        audio_data = r.record(source, duration=duration)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data, language=language)
        print(text)
        return text