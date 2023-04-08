from microbit import *
import radio
radio.on()
while True:
    #ambient_light=display.read_light_level()
    #pin0.write_analog(ambient_light)
    radio.send("led_on")
    
    
    