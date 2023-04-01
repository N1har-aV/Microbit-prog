from microbit import *
import radio
radio.on()
while True:
    if button_a.was_pressed():
        radio.send("Hi DAD")
    if button_b.was_pressed():
        radio.send('STOP')