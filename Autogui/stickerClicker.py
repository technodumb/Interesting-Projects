import keyboard
import pyautogui
from time import sleep
import win32api, win32con

# pyautogui.mouseInfo()

def click(coords):
    win32api.SetCursorPos(coords)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)


pixel = 1511,641

while True:
    if keyboard.is_pressed('q'):
        while keyboard.is_pressed('q'):
            pass
        for i in range(10):
            click(pixel)
            sleep(0.02)
        break
