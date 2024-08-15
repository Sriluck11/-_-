import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to get the current time
def tell_time():
    now = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {now}")

# Function to get the current date
def tell_date():
    today = datetime.datetime.today().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")

# Function to listen and recognize voice commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
        except sr.RequestError:
            speak("Sorry, I am unable to process your request at the moment.")
        return ""

# Function to search the web
def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the search results for {query}")

# Function to handle commands related to opening websites
def open_website(command):
    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "gmail" in command:
        webbrowser.open("https://www.gmail.com")
        speak("Opening Gmail")
    elif "google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

# Function to handle file explorer navigation
def open_file_explorer():
    os.startfile("explorer")
    speak("Opening file explorer")

def open_folder(folder_name):
    user_profile = os.environ['USERPROFILE']
    folder_path = os.path.join(user_profile, folder_name)
    if os.path.exists(folder_path):
        os.startfile(folder_path)
        speak(f"Opening {folder_name}")
    else:
        speak(f"{folder_name} folder not found")

# Function to close applications using subprocess
def close_application(app_name):
    os.system(f"taskkill /im {app_name} /f")
    speak(f"Closing {app_name}")

# Function to handle commands
def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        tell_time()
    elif "date" in command:
        tell_date()
    elif "search" in command:
        query = command.replace("search", "").strip()
        search_web(query)
    elif "open" in command:
        if "file explorer" in command:
            open_file_explorer()
        elif any(folder in command for folder in ["desktop", "downloads", "documents"]):
            folder = command.split()[-1]
            open_folder(folder.capitalize())
        else:
            open_website(command)
    elif "close" in command:
        if "youtube" in command:
            close_application("chrome.exe")  # Assuming YouTube is opened in Chrome
        elif "gmail" in command:
            close_application("chrome.exe")  # Assuming Gmail is opened in Chrome
        elif "google" in command:
            close_application("chrome.exe")  # Assuming Google is opened in Chrome
        elif "file explorer" in command:
            close_application("explorer.exe")
    elif "exit" in command:
        speak("Goodbye! See you next time.")
        exit()
    else:
        speak("I'm not sure how to help with that.")

# Main loop to continuously listen for commands
def start_voice_assistant():
    while True:
        command = listen()
        if command:
            handle_command(command)

# Start the voice assistant
start_voice_assistant()
