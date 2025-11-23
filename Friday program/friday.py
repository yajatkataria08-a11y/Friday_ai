import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import musiclibrary

engine = pyttsx3.init()
#defining speak function 
def speak(text):
    engine.say(text)
    engine.runAndWait()

# we are trying to process all the command that one may give to friday
def processcomand(command):
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "what time is it" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}.")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook.")
    elif "open twitter" in command:
        webbrowser.open("https://www.twitter.com")
        speak("Opening Twitter.")
    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
    elif "open github" in command:
        webbrowser.open("https://www.github.com")
        speak("Opening GitHub.")
    elif "what is your name" in command:
        speak("I am Friday, your personal assistant.")
    elif "who created you" in command:
        speak("I was created by a talented developer, Yajat kataria :).")
    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn.")
    elif "search for" in command or "google" in command:
        # we will need to use this command to extract the search query
        if "search for" in command:
            query = command.split("search for", 1)[1].strip()
        elif "google" in command:
            query = command.split("google", 1)[1].strip()
        
        if query:
            # if the user used common phrase such as google do something, we need to identify it
            #by splitting the command and taking the second part(do this) as the query
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(search_url)
            speak(f"Searching Google for {query}")
        else:
            speak("Please tell me what you would like me to search for.")
   
     
    elif "play" in command:
        speak("Playing music from my creator's fav's song.")
        # we will just play the songs in the music library 
        song = command.replace("play", "").strip()
        if song:
            speak(f"Playing {song}")
            musiclibrary.play_song_by_name(song)
        elif "play a random song" in command or "play music" in command:
            speak("Playing a random song")
            musiclibrary.play_random_song()
        # in case the song is not found in the library
        else:
            speak("sorry,the song you specified is not in my library.")
        
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    # just in case the command given was not defined by me :)
    else:
        speak("Sorry, I did not understand that command.")

if __name__ == "__main__":
    speak("Initializing Friday...")
    speak("Welcome back sir")
    speak("Good morning, what can I do for you?")
    
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    # this is inspired from marvel friday ai, in order to activate friday 
    # we need to say the wake word aka friday first
    while True:
        try:
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening...")
                audio = recognizer.listen(source)
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(command)
            command = command.lower()
            if command == "friday":
                speak("Yes sir, I am listening")
                with microphone as source:
                #after wake word is detected, we listen for the actual command
                    recognizer.adjust_for_ambient_noise(source)
                    print("friday active...")
                    audio = recognizer.listen(source)
                    new_command = recognizer.recognize_google(audio)
                    new_command = new_command.lower()
                    #and call process command function
                    print("Recognizing...")
                    print(f"Command: {new_command}")
                    processcomand(new_command)
        #in case of error we print it
        except Exception as e:
            print("error; {0}".format(e))
