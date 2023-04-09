from microbit import *
while True:
    if button_a.was_pressed():
        pin0.write_digital(0)
        pin1.write_digital(1)
    if button_b.was_pressed():
        pin0.write_digital(0)
        pin1.write_digital(0)