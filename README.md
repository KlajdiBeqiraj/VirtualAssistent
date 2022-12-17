# VirtualAssistent

---

This short guide shows how to create a virtual assistant in python using openai's gpt-3.
Code Structure
Speech to text: we use the speech_recognition library to capture the voice via the microphone
GTP-3: we use the gtp3 library to create the response
Text to speech: The gtts library is used to synthesise the text

In order to use the libraries mentioned in the Python code, it is necessary to install them. This can be done using pip, the Python package manager, by executing the following commands:
pip install gTTS
pip install SpeechRecognition
pip install openai

---

Speech to text
As mentioned above, we use the speech_recognition library. It allows you to transcribe spoken words into text and can be used to build speech-based applications such as voice commands, language translation, and automated transcription.
Through speech_recognition we use the microphone to acquire the text we want to pass to the gtp-3 module:
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
The speech_to_text function takes two inputs: 
duration: seconds in which the module keeps the microphone switched on for audio acquisition
language: several languages can be selected

---

GTP-3
GPT-3 (Generative Pre-training Transformer 3) is a state-of-the-art language generation model developed by OpenAI. It is capable of generating human-like text and completing a wide variety of language tasks, such as translation, summarization, and question answering.
GPT-3 is a pre-trained model that has been trained on a large dataset of text and language data, allowing it to generate high-quality, human-like text when given a prompt. It uses a transformer architecture, which is a type of neural network that is particularly well-suited for processing sequential data such as text.
GPT-3 has received a lot of attention in the media and technology industry due to its impressive performance on a wide range of language tasks and its ability to generate text that is difficult to distinguish from text written by humans. It is currently being used in a variety of applications, including chatbots, content generation, and language translation.
A quick implementation of using gtp-3 in python is shown below.
import openai

def GPT_Completion(texts):
    ## Call the API key under your account (in a secure way)
    openai.api_key = "OPENAI KEY"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=texts,
        temperature=0.6,
        top_p=1,
        max_tokens=600,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text
The openai.Completion.create method takes the following input parameters:
engine: The name of the GPT-3 model to use. Available models include davinci, curie, and babbage.
prompt: The prompt to provide to the model. This should be a string that specifies the text or task that you want the model to complete.
max_tokens: The maximum number of tokens (words and punctuation) to generate. The model will stop generating text once it has generated this many tokens.
n: The number of completions to generate.
stop: A string or list of strings that specify the conditions under which the model should stop generating text. For example, you can specify a string such as "END_OF_TEXT" to indicate that the model should stop generating text when it reaches this string.
temperature: The temperature of the output. A value of 0 will generate text that is more conservative and predictable, while a value of 1 or higher will generate text that is more creative and varied.

---

Text to speech
As mentioned, we use the gTTS library for this part. gTTS (Google Text-to-Speech) is a Python library that allows you to generate audio files of natural sounding synthesized text. It uses the Google Text-to-Speech API to convert text into audio files, which can be played back using any media player or included in a multimedia application.
def text_to_speech_gttps(mytext, lang="en", file_path=''):
    audio = gTTS(text=mytext, lang=lang, slow=False)
    audio.save(file_path)
    os.system("start " + file_path)
The text_to_speech_gttps function takes three inputs:
mytext: text to be synthesised
lan: several languages can be selected
file_path: path where the result is saved

---

Virtual assistant
Now let's use all the functions together to create a virtual assistant:
    language = "en"
    duration = 5

    in_text = speech_to_text(duration=duration, language=language)
    out_text = GPT_Completion(in_text)
    text_to_speech_gttps(out_text, lang=language, file_path=file_path)
