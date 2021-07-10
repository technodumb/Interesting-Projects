import keyboard
import time

n_members = int(input("Enter the number of members in the group: "))
print("\n\nSelect the group input box and press x to activate.")
while True:
    if keyboard.is_pressed('x'):
        keyboard.send("Backspace")
        for i in range(n_members):
            time.sleep(0.01)
            keyboard.write("@")
            for j in range(i):
                keyboard.send("Down")
                time.sleep(0.01)
            keyboard.send("Enter")
            # keyboard.write(".")
            if i==0:
                keyboard.send("Shift+Enter")
            keyboard.send("Shift+Enter")
            keyboard.send("Shift+Enter")
        break
