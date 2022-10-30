import time

import mouse

width = 1536
height = 1024
hits = 0

def xpos(x):
    return width * x


def ypos(y):
    return height * y


def mouseclicklabsolute(x, y):
    mouse.move(x, y)
    mouse.click("left")


def mclickl(x, y):
    mouse.move(xpos(x), ypos(y))
    mouse.click("left")


def mclickrabsolute(x, y):
    mouse.move(x, y)
    mouse.click("left")


def mclickr(x, y):
    mouse.move(xpos(x), ypos(y))
    mouse.click("right")


def ismousehereprecent(x1, x2, y1, y2):
    mouseposx = mouse.get_position()[0]
    mouseposy = mouse.get_position()[1]
    mouseposx = float(mouseposy)
    mouseposy = float(mouseposy)

    if width * x1 <= mouseposx <= width * x2 or height * y1 >= mouseposy >= height * y2:
        return True
    else:
        return False


def ismousehereabsolute(x1, x2, y1, y2):
    mouseposx = mouse.get_position()[0]
    mouseposy = mouse.get_position()[1]
    mouseposx = float(mouseposy)
    mouseposy = float(mouseposy)

    if x1 <= mouseposx <= x2 or y1 >= mouseposy >= y2:
        return True
    else:
        return False


def main():
    global hits
    for x in range(0, 613 - 415, 20):
        for y in range(0, 438 - 249, 19):
            mouseclicklabsolute(x + 426, y + 262)
            hits += 1
            if hits == 100:
                print("Ended")
                exit()


while not mouse.is_pressed('middle'):
    continue
else:
    time.sleep(1)
    main()
