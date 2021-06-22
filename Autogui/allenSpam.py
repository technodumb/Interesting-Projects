import keyboard
import emoji
import random
from time import sleep

a = list(emoji.EMOJI_UNICODE_ENGLISH)
# c = ' '.join(random.choices(a, k=6))
# print(emoji.emojize(c), '\n', c)

# sleep(3)
while True:
    if keyboard.is_pressed('q'):
        keyboard.send('Backspace')
        for i in range(1000):
            j = random.randint(0,len(a))
            c = emoji.emojize(a[j])
            sleep(0.1)
            keyboard.write(c)
            keyboard.send('Enter')
            if keyboard.is_pressed('r'):
                break
        break