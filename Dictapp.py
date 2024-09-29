import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

# Initialize the pyttsx3 engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Dictionary of applications and their executable names
dictapp = {
    "commandprompt": "cmd",
    "paint": "mspaint",
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "vscode": "code",
    "powerpoint": "powerpnt",
    "whatsapp": "WhatsApp"  # Added WhatsApp
}

def openappweb(query):
    """Open applications or websites based on the query."""
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    elif "whatsapp" in query:
        # Open WhatsApp Desktop by full path
        speak("Opening WhatsApp")
        try:
            os.startfile(r"C:\Users\<YourUserName>\AppData\Local\WhatsApp\WhatsApp.exe")  # Replace <YourUserName> with your actual username
        except FileNotFoundError:
            speak("WhatsApp is not installed in the default location.")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    """Close applications or browser tabs based on the query."""
    speak("Closing, sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("Closed one tab.")
    elif "2 tab" in query:
        for _ in range(2):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("Closed two tabs.")
    elif "3 tab" in query:
        for _ in range(3):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("Closed three tabs.")
    elif "4 tab" in query:
        for _ in range(4):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("Closed four tabs.")
    elif "5 tab" in query:
        for _ in range(5):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("Closed five tabs.")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                try:
                    os.system(f"taskkill /f /im {dictapp[app]}.exe")
                    speak(f"{dictapp[app]} closed successfully.")
                except Exception as e:
                    speak(f"Unable to close {app}. Error: {e}")
