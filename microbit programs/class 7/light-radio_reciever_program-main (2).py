from microbit import *
import radio 
radio.on()
while True:
    message=radio.receive()
    #print(message)
    if message is not None:   
        if message == 'led_on':
            pin1.write_digital(1)
        if message == 'led_off':
            pin1.write_digital(0)