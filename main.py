import time
import random
import pygame
import keyboard

pygame.init()

gridwidth = 20
gridheight = 20

actualwidth = gridwidth * 40
actualheight = gridheight * 40

screen = pygame.display.set_mode([actualwidth, actualheight])

running = True

snakeBodyPositionsX = [20]
snakeBodyPositionsY = [20]

applePositionsX = []
applePositionsY = []

applecount = 0

lastx = 0
lasty = 0

rightLastPress = False
leftLastPress = False
upLastPress = False
downLastPress = False


def main():
    global rightLastPress
    global leftLastPress
    global upLastPress
    global downLastPress

    global rightLastPress
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    drawboard()

    if applecount < 5:
        createapple()

    if keyboard.is_pressed("d") or rightLastPress:
        movecharacter("right")
        rightLastPress = True
        leftLastPress = False
        upLastPress = False
        downLastPress = False
        time.sleep(0.25)

    if keyboard.is_pressed("a") or leftLastPress:
        movecharacter("left")
        rightLastPress = False
        leftLastPress = True
        upLastPress = False
        downLastPress = False
        time.sleep(0.25)

    if keyboard.is_pressed("s") or downLastPress:
        movecharacter("down")
        rightLastPress = False
        leftLastPress = False
        upLastPress = False
        downLastPress = True
        time.sleep(0.25)

    if keyboard.is_pressed("w") or upLastPress:
        movecharacter("up")
        rightLastPress = False
        leftLastPress = False
        upLastPress = True
        downLastPress = False
        time.sleep(0.25)

    pygame.display.flip()
    print(len(snakeBodyPositionsX), len(snakeBodyPositionsY))


def drawboard():
    screen.fill((0, 0, 0))
    for i in range(0, len(snakeBodyPositionsX)):
        pygame.draw.rect(screen, (0, 255, 0), (snakeBodyPositionsX[i], snakeBodyPositionsY[i], 10, 10))

    for i in range(0, len(applePositionsX)):
        pygame.draw.rect(screen, (255, 0, 0), (applePositionsX[i], applePositionsY[i], 10, 10))



def movecharacter(direction):
    global lastx
    global lasty
    if direction == "right":
        lastx = snakeBodyPositionsX[len(snakeBodyPositionsX) - 1]
        lasty = snakeBodyPositionsY[len(snakeBodyPositionsY) - 1]
        for x in range(0, len(snakeBodyPositionsX)):
            if x != 0:
                snakeBodyPositionsX[x] = snakeBodyPositionsX[x - 1]
        snakeBodyPositionsX[0] += 20

    if direction == "left":
        lastx = snakeBodyPositionsX[len(snakeBodyPositionsX) - 1]
        lasty = snakeBodyPositionsY[len(snakeBodyPositionsY) - 1]
        for x in range(0, len(snakeBodyPositionsX)):
            if x != 0:
                snakeBodyPositionsX[x] = snakeBodyPositionsX[x - 1]
        snakeBodyPositionsX[0] -= 20

    if direction == "up":
        lastx = snakeBodyPositionsX[len(snakeBodyPositionsX) - 1]
        lasty = snakeBodyPositionsY[len(snakeBodyPositionsY) - 1]
        for y in range(0, len(snakeBodyPositionsY)):
            if y != 0:
                snakeBodyPositionsY[y] = snakeBodyPositionsY[y - 1]
        snakeBodyPositionsY[0] -= 20

    if direction == "down":
        lastx = snakeBodyPositionsX[len(snakeBodyPositionsX) - 1]
        lasty = snakeBodyPositionsY[len(snakeBodyPositionsY) - 1]
        for y in range(0, len(snakeBodyPositionsY)):
            if y != 0:
                snakeBodyPositionsY[y] = snakeBodyPositionsY[y - 1]
        snakeBodyPositionsY[0] += 20

    checkforapple()


def createapple():
    global applecount
    checkforpos = True
    x = random.randint(0, actualwidth)
    y = random.randint(0, actualheight)

    x = 20 * round(x / 20)
    y = 20 * round(y / 20)

    while checkforpos:
        for xcoord in snakeBodyPositionsX:
            if xcoord == x:
                x = random.randint(0, actualwidth)
                checkforpos = True
            else:
                checkforpos = False

        for ycoord in snakeBodyPositionsY:
            if ycoord == y:
                y = random.randint(0, actualwidth)
                checkforpos = True
            else:
                checkforpos = False

        for xcoord in applePositionsX:
            if xcoord == x:
                x = random.randint(0, actualwidth)
                checkforpos = True
            else:
                checkforpos = False

        for ycoord in applePositionsY:
            if ycoord == y:
                y = random.randint(0, actualwidth)
                checkforpos = True
            else:
                checkforpos = False

    applePositionsX.append(x)
    applePositionsY.append(y)
    applecount += 1


def checkforapple():
    global snakeBodyPositionsX
    global snakeBodyPositionsY
    global applecount
    for x in snakeBodyPositionsX:
        for ax in applePositionsX:
            if x == ax:
                for y in snakeBodyPositionsY:
                    for ay in applePositionsY:
                        if y == ay:
                            applePositionsX.remove(ax)
                            applePositionsY.remove(ay)
                            snakeBodyPositionsX.insert(len(snakeBodyPositionsX), int(lastx))
                            snakeBodyPositionsY.insert(len(snakeBodyPositionsY), int(lasty))
                            applecount -= 1



while __name__ == "__main__" and running:
    main()
