with open('1000pi.txt', 'r') as pifile:
    pi = pifile.read()

import keyboard
from time import sleep
import numpy as np
from PIL.ImageGrab import grab

ndigit = 4

while True:
    if keyboard.is_pressed('q'):
        while keyboard.is_pressed('q'):
            pass
        while True:
            if np.mean(grab([1500,400,1750,445]))==45:
                keyboard.write(pi[:ndigit])
                print(pi[:ndigit])
                sleep(1)
                ndigit+=1;
                
            if keyboard.is_pressed('q'):
                break
        break


# 1534,403 44,45,46 #2C2D2E
# 1751,443 44,45,46 #2C2D2E
