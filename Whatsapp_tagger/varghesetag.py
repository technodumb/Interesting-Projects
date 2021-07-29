import keyboard
import time
while True:
    if keyboard.is_pressed('space'):
        for i in range(1):
            keyboard.write('/tagtillreply')
            keyboard.send("Shift+Enter")
            keyboard.send("Shift+Enter")
            keyboard.send("Shift+Enter")
            keyboard.write("@vargh")
            keyboard.send("Enter")
            keyboard.send("Enter")
            time.sleep(3)
        break