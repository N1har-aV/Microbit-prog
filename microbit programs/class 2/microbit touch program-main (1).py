from microbit import *
yellow_led = pin0
while True:
    if pin1.is_touched():
        yellow_led.write_digital(1)
    else:
        yellow_led.write_digital(0)



