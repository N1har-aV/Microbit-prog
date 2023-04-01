from microbit import *
import music
import radio
radio.on()
while True:
    message=radio.receive()
    if message is not None:
        if message=='HI DAD':
            music.play(music.ODE)
            display.scroll(message)
        if message=='STOP':
            display.clear()
            music.stop(pin0)
            