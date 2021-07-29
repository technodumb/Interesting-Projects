import keyboard
import random
import time

locations = 'english-words\\'
def load_words():
    with open(locations+'words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return sorted(tuple(valid_words))

a_words = [x for x in load_words() if x[0]=='a']

while True:
    if keyboard.is_pressed('Space'):
        for i in range(50):
            keyboard.write(random.choice(a_words))
            keyboard.send('Enter')
            time.sleep(1)
        break   
