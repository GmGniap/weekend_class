## main ref - http://www.yahboom.net/study/Super:bit
from microbit import *
import neopixel

Red = (255,0,0)
Orange = (255,165,0)
Yellow = (255,255,0)
Green = (0,255,0)
White = (255,255,255)

color = (Red, Orange, Yellow, Green, White)

display.show(Image.HAPPY)
np = neopixel.NeoPixel(pin12, 4)
i = 0
while True:
    if button_a.was_pressed():
        np.clear()
        np[2] = color[i]
        np.show()
        sleep(1000)
        i += 1
        if i > 4:
            i = 0
    sleep(100)