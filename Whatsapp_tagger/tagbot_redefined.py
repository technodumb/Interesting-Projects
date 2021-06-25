import keyboard
import time

n_members = int(input("Enter the number of members in the group: "))
print("\n\nSelect the group input box and press x to activate.")
while True:
    if keyboard.is_pressed('x'):
        keyboard.send("Backspace")
        for i in range(n_members):
            keyboard.write("@")
            for j in range(i):
                keyboard.send("Down")
            keyboard.send("Enter")
            time.sleep(0.05)
        break
