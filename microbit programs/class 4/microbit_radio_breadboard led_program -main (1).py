from microbit import *
import music
import radio
radio.on()
while True:
    message=radio.receive()
    if message is not None:
        if message:
            pin1.write_digital(1)
            music.play(music.ODE)
            display.scroll(message)
            