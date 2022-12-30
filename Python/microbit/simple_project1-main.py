# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        display.show("A")
        sleep(1000)
    if button_b.is_pressed():
        display.show("B")
    else:
        display.clear()
