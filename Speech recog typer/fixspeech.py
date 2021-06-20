import pyttsx3
import random

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
randomstring = random.choices('abcdefghijklmnopqrstuvwxyz', k=50000) 
engine.say("".join(randomstring))
engine.runAndWait()
