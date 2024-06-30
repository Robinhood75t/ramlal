import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer = sr.Recognizer() #for recognizer 
engine = pyttsx3.init()
newsapi = "97f5bff1282f42f5a4c7bd96e79325d3"

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com/")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://www.chatgpt.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apikey={newsapi}")
        if r.status_code == 200:
            #parse the json response
            data = r.json()

            #extract the articles
            articles = data.get('articles',[])

            #print the headlines
            for article in articles:
                speak(article['title'])
        else: 
            speak("error occupied")


def speak(text):
    engine.say(text)
    engine.runAndWait()  # so that it cannot be exit

if __name__ == "__main__":
    speak("initializing ramlal......")
    while True:
        # listen for the wake word "Ramlal"
        #obtain audio from  the microphone
        r = sr.Recognizer()
        
        #recognize speech using sphinx
        print("recognizing...")
        try: 
            with sr.Microphone() as source:
                print("listening....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "ramlal"):
                speak("hello sir")
                # listen for command
                with sr.Microphone() as source:
                    print("ramlal active....")
                    audio = r.listen(source,timeout=2,phrase_time_limit=1)
                    command = r.recognize_google(audio)

                processcommand(command)


        except Exception as e:
            print("Error: {0}".format(e))
        
