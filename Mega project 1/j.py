import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary  # Ensure this has a dictionary called music

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        song = c.split(" ", 1)[1]  # Get song name after 'play'
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            word = recognizer.recognize_google(audio)
            print(f"Detected word: {word}")

            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = recognizer.recognize_google(audio)
                print(f"Command: {command}")
                processCommand(command)

        except Exception as e:
            print("Error:", e)
