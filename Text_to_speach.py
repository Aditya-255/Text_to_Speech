# text_to_speech.py
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Speak the text
engine.say("I will speak this text")
engine.runAndWait()
