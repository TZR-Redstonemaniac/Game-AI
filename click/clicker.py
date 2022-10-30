import mouse
import time

width = 1536
height = 1024


def xpos(x):
    return width * x


def ypos(y):
    return height * y


def mclickl(x, y):
    mouse.move(xpos(x), ypos(y))
    mouse.click("left")


def mclickr(x, y):
    mouse.move(xpos(x), ypos(y))
    mouse.click("right")


def ismousehere(x1, x2, y1, y2):
    mouseposx = mouse.get_position()[0]
    mouseposy = mouse.get_position()[1]
    mouseposx = float(mouseposy)
    mouseposy = float(mouseposy)

    if width * x1 <= mouseposx <= width * x2 or height * y1 >= mouseposy >= height * y2:
        return True
    else:
        return False


def main():
    timestart = time.time()
    mclickl(0.3475, 0.635)
    while True:
        if time.time() < timestart + 10 and ismousehere(0.25, 0.445, 0.62, 0.65):
            mclickl(0.3475, 0.635)
            time.sleep(0.01)
        else:
            break


time.sleep(2)

if True:
    main()
