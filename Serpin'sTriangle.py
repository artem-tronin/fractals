# This code is about drawing Serpinskiy's triangle by moving a random dot towards a random top by half of the distance beween them

import pygame
import random

pygame.init() #this turns pygame 'on'

SIZE = (800, 800)
WHITE = (255, 255, 255)
DOTCOLOR = (255, 0, 0)
x, y = random.randint(0, 700), random.randint(0, 700)
edges = 3  # int(input())
cords = []
count=0

screen = pygame.display.set_mode(SIZE)
screen.fill(WHITE)
event = pygame.event.poll()

while event.type != pygame.QUIT:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        print ("mouse at (%d, %d)" % event.pos)
        cords.append(event.pos)
        count+=1
        screen.set_at(cords[-1], DOTCOLOR)
        if count==edges:
            print(cords)
            while event.type != pygame.QUIT:
                event = pygame.event.poll()

                screen.set_at((x, y), DOTCOLOR)
                randtop = cords[random.randint(0, edges-1)]
                print([x, y], randtop)
                x = round((randtop[0]+x)/2)
                y = round((randtop[1]+y)/2)
                print([x, y], randtop)
                print()
                pygame.display.flip()
            break
    pygame.display.flip()

