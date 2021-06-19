import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests

name = 'Jarvis'

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello, Good Morning")
        # print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon")
        # print("Hello,Good Afternoon")
    else:
        speak("Hello, Good Evening")
        # print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone(1) as source:
        print("Listening...")
        audio=r.listen(source, phrase_time_limit=5)

        try:
            statement=r.recognize_google(audio,language='en-US')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return takeCommand()
        return statement

# print("Loading your AI personal assistant Neo")
speak(f"Loading your AI personal assistant {name}")
wishMe()

if __name__=='__main__':
    while True:
        # speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        elif "bye" in statement or "stop" in statement:
            speak(f'Your personal assistant {name} is shutting down... Good bye')
            # print('your personal assistant G-one is shutting down,Good bye')
            break

        
        elif 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            # print(results)
            speak(results)
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'change' in statement and 'name' in statement:
            speak("Do you want me to change my name?")
            if 'yes' in takeCommand().lower():
                speak("What is my new name?")
                name = takeCommand().capitalize()
                speak(f"{name} is my new name.")

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")    
                    
        elif 'repeat after me' in statement:
            speak("What should I say?")
            rep = takeCommand().lower()
            speak(rep)
        
        elif 'you are the best' in statement:
            speak("No... You are the best.")
        
        elif 'thank you' in statement:
            speak('YEAH BITCH')

        else:
            speak("I don't know how to do that")
        
