import pyttsx3
import random


locations = 'Speech recog typer\\english-words\\'
def load_words():
    with open(locations+'words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return sorted(tuple(valid_words))


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)
randomstring = '... '.join(random.choices(load_words(), k=50))
print(randomstring)
engine.say(randomstring)

engine.runAndWait()
