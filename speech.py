# speech.py
import tempfile
from gtts import gTTS
from playsound3 import playsound
import speech_recognition as sr

def speak_text(text, lang_code='en', speed=1.2):
    tts = gTTS(text=text, lang=lang_code, slow=False)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        playsound(fp.name)

def get_input_text():
    choice = input("🎤 Speak (s) or type (t)? ").lower()
    if choice == 's':
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"🗣 You said: {text}")
            return text
        except Exception as e:
            print(f"❌ Could not recognize speech: {e}")
            return None
    else:
        return input("✍️ Type your text: ")
