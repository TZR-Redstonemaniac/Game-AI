import time

import keyboard
import pygame

import random

pygame.init()

gridwidth = 20
gridheight = 20

actualwidth = gridwidth * 40
actualheight = gridheight * 40

drawwidth = actualwidth + 10
drawheight = actualheight + 10

screen = pygame.display.set_mode((drawwidth + 1, drawheight + 1))

pygame.display.set_caption("Snek")

my_font = pygame.font.SysFont("comicsans", 30)

running = True
dead = False

snakeBodyPositionsX = [20]
snakeBodyPositionsY = [20]

snakecount = 1

applePositionsX = []
applePositionsY = []

applecount = 0

lastx = 0
lasty = 0

rightLastPress = False
leftLastPress = False
upLastPress = False
downLastPress = False

cooldown = 0.05
start = time.time()

temp = 0


def main():
    global dead
    if not dead:
        print("Running")
        global rightLastPress
        global leftLastPress
        global upLastPress
        global downLastPress

        global running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if applecount < 50:
            createapple()

        if keyboard.is_pressed("right arrow") and not leftLastPress:
            movecharacter("right")
            if dead:
                return
            rightLastPress = True
            leftLastPress = False
            upLastPress = False
            downLastPress = False
        elif rightLastPress:
            movecharacter("right")
            if dead:
                return

        if keyboard.is_pressed("left arrow") and not rightLastPress:
            movecharacter("left")
            if dead:
                return
            rightLastPress = False
            leftLastPress = True
            upLastPress = False
            downLastPress = False
        elif leftLastPress:
            movecharacter("left")
            if dead:
                return

        if keyboard.is_pressed("down arrow") and not upLastPress:
            movecharacter("down")
            if dead:
                return
            rightLastPress = False
            leftLastPress = False
            upLastPress = False
            downLastPress = True
        elif downLastPress:
            movecharacter("down")
            if dead:
                return

        if keyboard.is_pressed("up arrow") and not downLastPress:
            movecharacter("up")
            if dead:
                return
            rightLastPress = False
            leftLastPress = False
            upLastPress = True
            downLastPress = False
        elif upLastPress:
            movecharacter("up")
            if dead:
                return

        drawboard(False, False)
        pygame.display.flip()
    elif dead:
        gameover()


def movecharacter(key):
    global lastx
    global lasty
    global start
    global dead
    if start + cooldown <= time.time():
        match key:
            case "up":
                snakeBodyPositionsY[0] -= 20
                checkforcollision("up")
                if dead:
                    return
                snakeBodyPositionsY[0] += 20

                if snakecount >= 2:
                    snakeBodyPositionsX.insert(1, snakeBodyPositionsX[0])
                    snakeBodyPositionsX.pop()

                    snakeBodyPositionsY.insert(1, snakeBodyPositionsY[0])
                    snakeBodyPositionsY.pop()

                snakeBodyPositionsY[0] -= 20
                start = time.time()

            case "down":
                snakeBodyPositionsY[0] += 20
                checkforcollision("down")
                if dead:
                    return
                snakeBodyPositionsY[0] -= 20

                if snakecount >= 2:
                    snakeBodyPositionsX.insert(1, snakeBodyPositionsX[0])
                    snakeBodyPositionsX.pop()

                    snakeBodyPositionsY.insert(1, snakeBodyPositionsY[0])
                    snakeBodyPositionsY.pop()

                snakeBodyPositionsY[0] += 20
                start = time.time()

            case "right":
                snakeBodyPositionsX[0] += 20
                checkforcollision("right")
                if dead:
                    return
                snakeBodyPositionsX[0] -= 20

                if snakecount >= 2:
                    snakeBodyPositionsX.insert(1, snakeBodyPositionsX[0])
                    snakeBodyPositionsX.pop()

                    snakeBodyPositionsY.insert(1, snakeBodyPositionsY[0])
                    snakeBodyPositionsY.pop()

                snakeBodyPositionsX[0] += 20
                start = time.time()

            case "left":
                snakeBodyPositionsX[0] -= 20
                checkforcollision("left")
                if dead:
                    return
                snakeBodyPositionsX[0] += 20

                if snakecount >= 2:
                    snakeBodyPositionsX.insert(1, snakeBodyPositionsX[0])
                    snakeBodyPositionsX.pop()

                    snakeBodyPositionsY.insert(1, snakeBodyPositionsY[0])
                    snakeBodyPositionsY.pop()

                snakeBodyPositionsX[0] -= 20
                start = time.time()

    checkforapple()


def drawboard(kill, deady):
    global my_font
    global actualwidth
    global actualheight
    global temp
    screen.fill((0, 0, 0))

    pygame.draw.line(screen, (0, 0, 255), (0, 0), (drawwidth, 0))
    pygame.draw.line(screen, (0, 0, 255), (0, 0), (0, drawheight))
    pygame.draw.line(screen, (0, 0, 255), (drawwidth, 0), (drawwidth, drawheight))
    pygame.draw.line(screen, (0, 0, 255), (0, drawheight), (drawwidth, drawheight))

    if not deady:
        for i in range(0, snakecount):
            if i == 0 and not kill:
                pygame.draw.rect(screen, (30, 100, 15), (snakeBodyPositionsX[i], snakeBodyPositionsY[i], 10, 10))
            else:
                pygame.draw.rect(screen, (0, 255, 0), (snakeBodyPositionsX[i], snakeBodyPositionsY[i], 10, 10))

        for i in range(0, applecount):
            pygame.draw.rect(screen, (255, 0, 0), (applePositionsX[i], applePositionsY[i], 10, 10))

        if snakecount >= temp:
            temp = snakecount
        score_text = my_font.render(f"{temp}", 1, (255, 255, 255))
        screen.blit(score_text, (0, 0))
        pygame.display.update()
        pygame.display.flip()
    elif deady:
        text_surface = my_font.render("Game Over", True, (255, 0, 0))
        screen.blit(text_surface, (int(actualwidth / 0.5), int(actualheight / 0.5)))


def createapple():
    global applecount
    checkforpos = True
    x = random.randint(0, actualwidth)
    y = random.randint(0, actualheight)

    x = 20 * round(x / 20)
    y = 20 * round(y / 20)

    while checkforpos:
        for xcoord in snakeBodyPositionsX:
            while xcoord == x:
                x = random.randint(0, actualwidth)
                x = 20 * round(x / 20)
                checkforpos = True
            else:
                checkforpos = False

        for ycoord in snakeBodyPositionsY:
            while ycoord == y:
                y = random.randint(0, actualwidth)
                y = 20 * round(y / 20)
                checkforpos = True
            else:
                checkforpos = False

        for xcoord in applePositionsX:
            while xcoord == x:
                x = random.randint(0, actualwidth)
                x = 20 * round(x / 20)
                checkforpos = True
            else:
                checkforpos = False

        for ycoord in applePositionsY:
            while ycoord == y:
                y = random.randint(0, actualwidth)
                y = 20 * round(y / 20)
                checkforpos = True
            else:
                checkforpos = False

    applecount += 1
    applePositionsX.append(x)
    applePositionsY.append(y)


def checkforapple():
    global snakeBodyPositionsX
    global snakeBodyPositionsY
    global applecount
    global snakecount
    for i in range(0, applecount):
        if i != 0:
            i -= 1
        if applePositionsX[i] == snakeBodyPositionsX[0] and applePositionsY[i] == snakeBodyPositionsY[0]:
            applePositionsX.pop(i)
            applePositionsY.pop(i)
            snakeBodyPositionsX.insert(len(snakeBodyPositionsX), int(lastx))
            snakeBodyPositionsY.insert(len(snakeBodyPositionsY), int(lasty))
            applecount -= 1
            snakecount += 1


def checkforcollision(dir):
    global snakecount
    global screen
    global dead
    coords = {

    }

    for i in range(0, snakecount):
        coords.update({
            "coords" + str(i + 1): {
                "x": snakeBodyPositionsX[i],
                "y": snakeBodyPositionsY[i]
            }
        })

    for i in range(0, snakecount):
        for j in range(0, snakecount):
            if i != j and snakeBodyPositionsX[i] == coords["coords" + str(j + 1)]["x"] and \
                    snakeBodyPositionsY[i] == coords["coords" + str(j + 1)]["y"] or snakeBodyPositionsX[0] < 0 or \
                    snakeBodyPositionsX[0] > actualwidth or snakeBodyPositionsY[0] < 0 or \
                    snakeBodyPositionsY[0] > actualheight:
                time.sleep(1)

                while len(snakeBodyPositionsX) > 0:
                    if dir == "up":
                        snakeBodyPositionsY[0] += 20
                    elif dir == "down":
                        snakeBodyPositionsY[0] -= 20
                    elif dir == "left":
                        snakeBodyPositionsX[0] += 20
                    elif dir == "right":
                        snakeBodyPositionsX[0] -= 20

                    snakeBodyPositionsX.pop(0)
                    snakeBodyPositionsY.pop(0)
                    snakecount -= 1
                    drawboard(True, False)
                    pygame.display.flip()
                    time.sleep(0.05)

                print("Game Over")
                dead = True
                gameover()
                return


def gameover():
    drawboard(False, True)


while __name__ == "__main__" and running:
    main()
