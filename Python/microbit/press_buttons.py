from microbit import *

while True:
    if button_a.was_pressed():
        display.set_pixel(0,2,9)
        sleep(1000)
        display.clear()
    if button_b.was_pressed():
        display.set_pixel(4,2,9)
        sleep(1000)
        display.clear()
    sleep(100)