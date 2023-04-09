from microbit import *
while True: 
    light_motor_controller=display.read_light_level()
    if light_motor_controller >100:
        pin1.write_digital(1)
        pin0.write_digital(0)
    if light_motor_controller <100:
        pin1.write_digital(0)
        pin0.write_digital(0)
   