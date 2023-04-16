from microbit import *
import radio
radio.on()
while True:
    message=radio.receive()
    if message is not None:
        if message=='Hello':
            display.scroll(message)
