from microbit import *
while True:
    t=temperature()
    display.scroll(t)
    sleep(1000)
    
    