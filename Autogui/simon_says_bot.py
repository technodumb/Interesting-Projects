import keyboard
import pyautogui
from time import sleep
import win32api, win32con

def click(coords):
    win32api.SetCursorPos(coords)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

# class simon_says:
#     memory = []
#     count = 0
#     def __init__(self):
#         while True:    
#             if(keyboard.is_pressed('enter')):
#                 a = pyautogui.displayMousePosition()
#                 print(a)
#             if(keyboard.is_pressed('q')):
#                 break
#          listen()

count=0
memory=[]
listen = True

locations = [(1200, 450), (1600, 450), (1600, 750), (1200, 750)]

def color_check(count, listen):
    if(pyautogui.pixel(1200, 450)!=(35,  69,  71)):
        while(pyautogui.pixel(1200, 450)!=(35,  69,  71)):
            sleep(0.05)
        count+=1
        if count > len(memory):
            memory.append(0)
            listen = False

    if(pyautogui.pixel(1600, 450)!=(69,  35,  46)):
        while(pyautogui.pixel(1600, 450)!=(69,  35,  46)):
            sleep(0.05)
        count+=1
        if count > len(memory):
            memory.append(1)
            listen = False

    if(pyautogui.pixel(1600, 750)!=(36,  64,  84)):
        while(pyautogui.pixel(1600, 750)!=(36,  64,  84)):
            sleep(0.05)
        count+=1
        if count > len(memory):
            memory.append(2)
            listen = False

    if(pyautogui.pixel(1200, 750)!=(62,  49,  43)):
        while(pyautogui.pixel(1200, 750)!=(62,  49,  43)):
            sleep(0.05)
        count+=1
        if count > len(memory):
            memory.append(3)
            listen = False
    return count, listen


while True:
    if keyboard.is_pressed('q'):
        while True:
            if listen:
                count, listen = color_check(count, listen)
            else:
                count = 0
                for color in memory:
                    sleep(0.05)
                    click(locations[color])
                win32api.SetCursorPos((1200,900))
                sleep(1)
                listen = True
        #     if keyboard.is_pressed('q'):
        #         break
        #     else:
        #         pass
        # break


    
# X: 1200 Y:  450 RGB: ( 35,  69,  71)      --> 
# X: 1500 Y:  450 RGB: ( 69,  35,  46)
# X: 1600 Y:  750 RGB: ( 36,  64,  84)
# X: 1200 Y:  750 RGB: ( 62,  49,  43)

# X = simon_says()