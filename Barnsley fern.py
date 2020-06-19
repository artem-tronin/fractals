import random
import pygame

pygame.init()
SIZE = (700, 700)
DOTCOLOR = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode(SIZE)
screen.fill(WHITE)
x, y = 0, 0
dot = (x+350, y+600)
screen.set_at(dot, DOTCOLOR)

def f1(xn, yn):
    x1 = 0
    y1 = 0.16 * yn
    return x1, y1

def f2(xn, yn):
    x1 = 0.85 * xn + 0.04 * yn
    y1 = -0.04 * xn + 0.85 * yn + 1.6
    return x1, y1

def f3(xn, yn):
    x1 = 0.20 * xn - 0.26 * yn
    y1 = 0.23 * xn + 0.22 * yn + 1.6
    return x1, y1

def f4(xn, yn):
    x1 = -0.15 * xn + 0.28 * yn
    y1 = 0.26 * xn + 0.24 * yn + 0.44
    return x1, y1

def getXY(r, xn, yn):
    if r < 1:  # elif ladder based on the probability
        x, y = f1(xn, yn)
    elif r < 86:
        x, y = f2(xn, yn)
    elif r < 93:
        x, y = f3(xn, yn)
    else:
        x, y = f4(xn, yn)

    return x, y


event = pygame.event.poll()

while event.type != pygame.QUIT:
    event = pygame.event.poll()

    r = random.random()
    r *= 100
    xn = x
    yn = y

    x, y = getXY(r, xn, yn)

    dot = (85*x, 57*y-275)
    print((85*x, 57*y-275), r)
    screen.set_at((round(85*x)+300, round(57*y)), DOTCOLOR)
    pygame.display.flip()
