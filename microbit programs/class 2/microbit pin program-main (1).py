from microbit import *
yellow_led = pin0
while True:
    if button_a.is_pressed():
        yellow_led.write_digital(1)
    else:
        yellow_led.write_digital(0)



