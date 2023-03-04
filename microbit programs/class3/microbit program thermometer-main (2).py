from microbit import *
while True:
    t=temperature()
    if t>31:
        display.scroll("t increased")
    else:
        print(t)
    