## Random neopixel color based on light
from microbit import *
import neopixel
from random import randint

np = neopixel.NeoPixel(pin12, 4)

while True:
    light = display.read_light_level()
    # display.scroll(light)
    print(light)
    sleep(1000)

    if light <= 20 or button_b.was_pressed():
        np.clear()
    else:
        for pixel_id in range(0, len(np)):
            color1 = randint(0, 255)
            color2 = randint(0, 255)
            color3 = randint(0, 255)

            np[pixel_id] = (color1, color2, color3)
            np.show()
            sleep(100)