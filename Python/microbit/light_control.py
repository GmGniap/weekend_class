from microbit import *
light1 = Image("99999:99999:99999:99999:99999")
light2 = Image("55555:55555:55555:55555:55555")
light3 = Image("00000:00000:00000:00000:00000")

while True:
    level = display.read_light_level()
    if level < 10:
        display.show(light1)
    elif level >= 10 and level < 100:
        display.show(light2)
    else:
        display.show(light3)