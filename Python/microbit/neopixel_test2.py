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
        for i in range(3):
            np[i] = color[i]
            np.show()
            sleep(1000)
    if button_b.was_pressed():
        np.clear()
        display.clear()
    sleep(100)