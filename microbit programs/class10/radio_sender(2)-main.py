from microbit import *
import radio
radio.on()
while True:
    #radio.send("hello")
    if button_a.is_pressed():
        radio.send("start")
    if button_b.is_pressed():
        radio.send("stop")