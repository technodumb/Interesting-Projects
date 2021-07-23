import keyboard
import random
import time

locations = 'english-words\\'
def load_words():
    with open(locations+'words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return sorted(tuple(valid_words))

q_words = [x for x in load_words() if x[0]=='q']

while True:
    if keyboard.is_pressed('Space'):
        for i in range(len(q_words)):
            keyboard.write(q_words[i])
            keyboard.send('Enter')
            time.sleep(0.01)
        break   
