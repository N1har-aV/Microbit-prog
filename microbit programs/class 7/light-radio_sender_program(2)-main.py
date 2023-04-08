from microbit import *
import radio
radio.on()
while True:
    #ambient_light=display.read_light_level()
    if button_a.was_pressed():
        radio.send('led_on')
    if button_b.was_pressed():
        radio.send('led_off')