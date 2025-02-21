# TASK 2: VOICE ASSISTANT
# Create a custom voice assistant using Python to personalize and automate tasks.
# The assistant should listen to the user's voice, recognize the speech, and respond.
# Python's versatility makes it an excellent choice for scripting and development.

import speech_recognition as sr # type: ignore
import pyttsx3

def speak(text):
    """Convert text to speech"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """Recognize speech from the microphone"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None
    except sr.RequestError:
        print("Could not request results. Check your internet connection.")
        return None

speak("Hello! How can I assist you?")
command = listen()

if command:
    speak(f"You said: {command}")
