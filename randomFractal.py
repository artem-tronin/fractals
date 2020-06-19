from turtle import *

t = Turtle()
t.speed(0)


def setCords(corner, radius, cords):
    t.penup()
    angle = 360 / corner
    t.goto(0, 0)
    for i in range(corner):
        t.forward(radius)
        cords[i][0] = t.xcor()
        cords[i][1] = t.ycor()
        t.goto(0, 0)
        t.right(angle)
    return cords


def drawFigure(corner, radius, cords):
    cords = setCords(corner, radius, cords)
    t.goto(cords[0][0], cords[0][1])
    t.pendown()
    for i in range(corner - 1):
        t.goto(cords[i + 1][0], cords[i + 1][1])
    t.goto(cords[0][0], cords[0][1])


def figureInFigure(corner, cords, radius, depth):
    if depth == 0:
        return
    drawFigure(corner, radius, cords)
    t.right(45)
    figureInFigure(corner, cords, radius+20, depth - 1)


corner = 4
radius = 20
depth = 10

t.left(90)
cords = [[0] * 2 for i in range(corner)]
figureInFigure(corner, cords, radius, depth)
done()
