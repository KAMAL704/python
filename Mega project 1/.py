import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

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
        parts = c.split(" ", 1)
        if len(parts) > 1:
            song = parts[1].strip()
            if song in musicLibrary.music:
                link = musicLibrary.music[song]
                webbrowser.open(link)
            else:
                speak(f"Sorry, I couldn't find the song {song}")
        else:
            speak("Please specify a song to play.")

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        try:
            r = sr.Recognizer()
            print("recognizing.....")
            with sr.Microphone() as source:
                print("Listening...!")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            print(f"Heard: {word}")
            if word.lower() == "jarvis":
                speak("Ya")
                with sr.Microphone() as source:
                    print("jarvis active...!")
                    audio = r.listen(source, timeout=2, phrase_time_limit=4)
                command = r.recognize_google(audio)
                print(f"Command: {command}")
                processCommand(command)
        except Exception as e:
            print(f"Error: {e}")