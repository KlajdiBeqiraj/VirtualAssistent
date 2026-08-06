# Virtual Assistant with GPT-3

A voice-driven assistant built in **December 2022**, a few weeks after the ChatGPT launch, using
OpenAI's GPT-3 completions API. Speech in, completion, speech out.

Kept here as a dated artifact rather than a maintained project. Companion write-up:
[Virtual assistant with GPT-3 from OpenAI](https://medium.com/@BeckzKla).

## How it works

```
microphone -> speech-to-text -> GPT-3 completion -> text-to-speech -> speaker
```

| File | Role |
|---|---|
| `main.py` | Entry point: capture, completion, playback loop |
| `speech_to_text.py` | Microphone capture, transcription via Google Speech Recognition |
| `gtp3.py` | GPT-3 completion call |
| `text_to_speech.py` | Speech synthesis via gTTS, with a pyttsx3/SAPI5 alternative |

## Status

**Not runnable as-is.** The code targets the legacy Completions endpoint with `text-davinci-002`,
which OpenAI retired in January 2024, and the audio playback path is Windows-only. It is left
public unchanged because it is the earliest dated example of my work with large language models:
porting it to the current Chat Completions API is the exercise, not the artifact.

## Running it, if you port it

Windows, Python 3, and an OpenAI API key in the environment:

```
git clone https://github.com/KlajdiBeqiraj/VirtualAssistent.git
cd VirtualAssistent
pip install -r requirements.txt
setx OPENAI_API_KEY sk-...
python main.py
```

Speak when prompted; the assistant transcribes, completes and reads the answer back.
