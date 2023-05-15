import keyboard
import time

i=0
for i in range(5):
    i+=1
    time.sleep(5)
    
    keyboard.press("d")
    time.sleep(0.5)
    keyboard.release("d")
    time.sleep(0.5)


    keyboard.press("s")
    time.sleep(0.5)
    keyboard.release("d")
    time.sleep(0.5)

    keyboard.press("q")
    time.sleep(0.5)
    keyboard.release("d")
    time.sleep(0.5)

    keyboard.press("z")
    time.sleep(0.5)
    keyboard.release("d")
    time.sleep(0.5)


