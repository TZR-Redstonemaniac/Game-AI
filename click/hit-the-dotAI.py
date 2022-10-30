from PIL import Image, ImageGrab
import mouse
import time

width = 1536
height = 1024
searchforblack = True
foundblack = False


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
    global searchforblack
    offlimitx1, offlimitx2, offlimity1, offlimity2 = 0, 0, 0, 0
    time.sleep(2)
    mouse.move(0, 0)
    px = ImageGrab.grab(bbox=(382, 372, 636, 515))
    while searchforblack:
        for y in range(0, 515 - 372):
            for x in range(0, 636 - 382):
                r, g, b = px.getpixel((x, y))
                moveposx = x + 382
                moveposy = y + 372
                if mouse.is_pressed(button='middle'):
                    print("Ended")
                    exit()
                if 60 >= r >= 33 and 60 >= g >= 33 and 60 >= b >= 33:
                    mouseclicklabsolute(moveposx, moveposy)
                    offlimitx1 = moveposx - 20
                    offlimitx2 = moveposx + 20
                    offlimity1 = moveposy - 20
                    offlimity2 = moveposy + 20
                    r, g, b = 0, 0, 0
                    time.sleep(0.02)
                    mouse.move(0, 0)
                    px = ImageGrab.grab(bbox=(382, 372, 636, 515))


while not mouse.is_pressed('middle'):
    continue
else:
    main()
