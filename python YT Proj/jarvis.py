import audioop
import pyttsx3
import datetime
import speechRecognition as sr

engine  = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')  #get voices property
#print(voices[1].id)
engine.setProperty('voice',voices[0].id) #set men Voice Property

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning")
    elif hour >= 12 and hour<18:
        speak("Good Afternoon")
    elif hour>=18 and hour<21:
        speak("Good Evening")    
    elif hour>=21 and hour<24:
        speak("Good Night..")
    speak("I AM Jarvice how can i help u....")


def takecommand():
    '''
    it takes microphone input from the user and return string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogninzing....")    
        query = r.recognize_google(audio,language="en-in")
        print(f"User said:{query}\n")

    except Exception as e:
        #print(e)
        print("say that again please..!")    
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    takecommand()        

    
    