import pyttsx3
import speech_recognition as sr
import datetime
import requests
from bs4 import BeautifulSoup
import pyautogui  # Add the pyautogui library
# Ensure these functions are defined or replaced with pyautogui equivalent
from keyboard import volumeup, volumedown  

# Your GROQ API Key
GROQ_API_KEY = "your api"

# Initialize pyttsx3 engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set to male voice
engine.setProperty("rate", 170)  # Set speech rate

def speak(audio):
    """Converts text to speech."""
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """Takes microphone input from the user and returns it as text."""
    r = sr.Recognizer()  # Initialize recognizer
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Pause before listening
        r.energy_threshold = 300  # Adjust this threshold based on the environment
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)  # Listen with timeout and phrase limit
        except sr.WaitTimeoutError:
            print("Timeout. Please try again.")
            return "None"

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')  # Use Google's speech recognition
        print(f"You Said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"

    return query.lower()  # Return the query in lowercase

def greetMe():
    """Greets the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning, sir")
    elif hour < 18:
        speak("Good Afternoon, sir")
    else:
        speak("Good Evening, sir")
    speak("How can I assist you today?")

def fetch_temperature(city):
    """Fetches and returns the temperature of the given city."""
    search = f"temperature in {city}"
    url = f"https://www.google.com/search?q={search}"
    try:
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        return f"The current {search} is {temp}"
    except Exception as e:
        return f"Sorry, I couldn't fetch the temperature details. {e}"

def call_groq_api(query):
    """Calls the GROQ API with the given query."""
    url = "https://api.groq.cloud/v1/chat/completions"  # Confirm this endpoint is correct
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",  # Make sure this model is correct
        "messages": [
            {
                "role": "user",
                "content": query  # The user's input
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx or 5xx
        response_data = response.json()  # Process JSON response
        answer = response_data['choices'][0]['message']['content']  # Adjust based on GROQ's response structure
        return answer
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")  # Print the error for debugging
        return "API request failed."
    except Exception as e:
        print(f"Unexpected error: {e}")  # Catch any unexpected errors
        return "An unexpected error occurred."

def main():
    """Main function to run the assistant."""
    while True:
        query = takeCommand()

        if "wake up" in query:
            greetMe()

            # Sub-loop for when assistant is awake
            while True:
                query = takeCommand()

                if "go to sleep" in query:
                    speak("Okay sir, You can call me anytime.")
                    break

                elif "what time is it" in query or "the time" in query:
                    strTime = datetime.datetime.now().strftime("%I:%M %p")  # 12-hour format with AM/PM
                    speak(f"Sir, the time is {strTime}")

                elif "what is your name" in query:
                    speak("I am your assistant. You can call me Jarvis.")

                elif "hello" in query:
                    speak("Hello sir, how are you?")
                
                elif "i am fine" in query:
                    speak("That's great, sir")

                elif "how are you" in query:
                    speak("I'm doing well, thank you for asking!")

                elif "thank you" in query:
                    speak("You're welcome, sir!")

                # Media controls using pyautogui
                elif "stop" in query:
                    pyautogui.press("k")
                    speak("Video paused.")
                
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played.")
                
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video muted.")
                
                elif "volume increase" in query:
                    speak("Turning volume up, sir.")
                    volumeup()  # Ensure this function is defined
                
                elif "volume down" in query:
                    speak("Turning volume down, sir.")
                    volumedown()  # Ensure this function is defined
                
                # Scroll up command for YouTube
                elif "scroll up" in query:
                    pyautogui.scroll(500)  # Scroll up by 500 units
                    speak("Scrolling up on YouTube.")

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)

                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query)

                # Temperature and weather commands
                elif "temperature" in query or "weather" in query:
                    speak(fetch_temperature("Shirpur"))

                # Example: Call the GROQ API
                elif "jarvis" in query:
                    groq_response = call_groq_api(query)
                    speak(f"GROQ says: {groq_response}")

                elif "exit" in query or "quit" in query:
                    speak("Goodbye, sir!")
                    return  # Use return instead of break to exit both loops

if __name__ == "__main__":
    main()
