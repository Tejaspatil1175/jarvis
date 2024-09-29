import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Default voice
engine.setProperty("rate", 200)  # Set speech rate

def speak(audio):
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    """Greet the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning, sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon, sir")
    else:
        speak("Good Evening, sir")
    
    speak("Please tell me, how can I help you?")

if __name__ == "__main__":
    greetMe()
