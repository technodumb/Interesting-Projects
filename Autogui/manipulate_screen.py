import keyboard
import string
from time import sleep

sleep(2)
st1 = string.ascii_lowercase

print(st1)
for i in range(20):
    keyboard.press_and_release('ctrl+shift+N')
    keyboard.write(st1[i])
    keyboard.press_and_release('Enter')