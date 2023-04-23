from microbit import *
import radio
radio.on()
while True:
    message=radio.receive()
    if message is not None:
        if message=="start":
             pin1.write_digital(1)
             pin0.write_digital(0)
        if message=="stop":
            pin1.write_digital(0)
            pin0.write_digital(0)
