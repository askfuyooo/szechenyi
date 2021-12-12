#TOGGLE SYSTEM WITH FUNCTION
import keyboard as kb
import time
t = 0
tString = "unknown"

def infos(tErtek):
    print()
    print("%%%%%%%%%%%%%%%%")
    if tErtek == 0:
        tString = "% [TOGGLE] OFF %"
        print(tString)
    else:
        tString = "% [TOGGLE] ON  %"
        print(tString)
    print("%%%%%%%%%%%%%%%%")

while True:
    if (kb.is_pressed("T")):
        if t == 0:
            infos(t + 1) #TOGGLED ON LINES
            t += 2
            t /= 2    
            time.sleep(0.25)
        else:
            if t == 1:
                infos(t -1) #TOGGLED OFF LINES
                t = 0
                time.sleep(0.25)
