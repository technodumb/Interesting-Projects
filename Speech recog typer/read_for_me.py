import pyttsx3

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voices', voice[0])
engine.setProperty('rate', 100)

user_input = input("Enter what you wanna hear: ")

engine.say(user_input)
engine.runAndWait()