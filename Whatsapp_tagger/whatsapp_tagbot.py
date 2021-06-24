import keyboard
import time
import pyautogui
from PIL import Image
from PIL import ImageGrab
import pytesseract


# pyautogui.mouseInfo()
scrsht = ImageGrab.grab((1359,151,1897,1016))
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
txt = pytesseract.image_to_string(scrsht)
print(txt)


# Coordinates
# 1359,151 45,49,52 #2D3134
# 1898,160 45,49,52 #2D3134
# 1353,1014 45,49,52 #2D3134
# 1897,1016 45,49,52 #2D3134
