from turtle import *

t = Turtle()
h = Turtle()
t.speed(0)
n = 90
sqrt = 1.414213562373095
mainstep = 11
colorstep = 1 / mainstep


def square(length, x, y, deg, step):
    if deg == 360:
        deg = 0
    elif deg < 0:
        deg += 360
    t.penup()
    t.goto(x, y)
    h.penup()
    # h.goto(x, y)
    # t.dot(5, 'red')
    if step == 0:
        return
    if deg == 0:
        x1 = length / 2 + x
        y1 = length / 2 + y
        x2 = x1
        y2 = y1 - length
        x3 = x2 - length
        y3 = y2
        x4 = x3
        y4 = y3 + length

        xnew1 = x4
        ynew1 = y4 + length / 2
        xnew2 = x1
        ynew2 = y1 + length / 2
    elif deg == 90:
        x4 = x - length / 2
        y4 = y - length / 2
        x2 = x + length / 2
        y2 = y + length / 2
        x1 = x2 - length
        y1 = y4 + length
        x3 = x4 + length
        y3 = y2 - length
        xnew1 = x4 - length / 2
        ynew1 = y4
        xnew2 = x1 - length / 2
        ynew2 = y1
    elif deg == 180:
        x3 = length / 2 + x
        y3 = length / 2 + y
        x4 = x3
        y4 = y3 - length
        x1 = x4 - length
        y1 = y4
        x2 = x1
        y2 = y1 + length
        xnew1 = x4
        ynew1 = y4 - length / 2
        xnew2 = x1
        ynew2 = y1 - length / 2

    elif deg == 270:
        x2 = x - length / 2
        y2 = y - length / 2
        x3 = x2
        y3 = y2 + length
        x4 = x3 + length
        y4 = y3
        x1 = x4
        y1 = y4 - length
        xnew1 = x4 + length / 2
        ynew1 = y4
        xnew2 = x1 + length / 2
        ynew2 = y1

    elif deg == 45:
        x1 = x
        y1 = y + length / sqrt
        x2 = x + length / sqrt
        y2 = y
        x3 = x
        y3 = y - length / sqrt
        x4 = x - length / sqrt
        y4 = y

        xnew1 = x4 - (length / sqrt) / 2
        ynew1 = y4 + (length / sqrt) / 2
        xnew2 = x1 - (length / sqrt) / 2
        ynew2 = y1 + (length / sqrt) / 2

    elif deg == 135:
        x3 = x + length / sqrt
        y3 = y
        x4 = x
        y4 = y - length / sqrt
        x1 = x - length / sqrt
        y1 = y
        x2 = x
        y2 = y + length / sqrt

        xnew1 = x4 - (length / sqrt) / 2
        ynew1 = y4 - (length / sqrt) / 2
        xnew2 = x1 - (length / sqrt) / 2
        ynew2 = y1 - (length / sqrt) / 2

    elif deg == 225:
        x3 = x
        y3 = y + length / sqrt
        x4 = x + length / sqrt
        y4 = y
        x1 = x
        y1 = y - length / sqrt
        x2 = x - length / sqrt
        y2 = y

        xnew1 = x4 + (length / sqrt) / 2
        ynew1 = y4 - (length / sqrt) / 2
        xnew2 = x1 + (length / sqrt) / 2
        ynew2 = y1 - (length / sqrt) / 2

    elif deg == 315:
        x2 = x
        y2 = y - length / sqrt
        x3 = x - length / sqrt
        y3 = y
        x4 = x
        y4 = y + length / sqrt
        x1 = x + length / sqrt
        y1 = y

        xnew1 = x4 + (length / sqrt) / 2
        ynew1 = y4 + (length / sqrt) / 2
        xnew2 = x1 + (length / sqrt) / 2
        ynew2 = y1 + (length / sqrt) / 2

    # r = colorstep*(mainstep-step)
    r = colorstep*step
    # b = colorstep*(mainstep-step)
    # b = colorstep*step
    b=0
    g = colorstep*(mainstep-step)
    # g = colorstep*step
    color = (r, g, b)

    t.color(color)
    h.color(color)

    t.begin_fill()
    h.begin_fill()
    t.goto(x1, y1)
    h.goto(-x1, y1)
    t.pendown()
    h.pendown()
    t.goto(x2, y2)
    h.goto(-x2, y2)
    t.goto(x3, y3)
    h.goto(-x3, y3)
    t.goto(x4, y4)
    h.goto(-x4, y4)
    t.goto(x1, y1)
    h.goto(-x1, y1)
    t.end_fill()
    h.end_fill()

    square(length / sqrt, xnew2, ynew2, deg - 45, step - 1)
    square(length / sqrt, xnew1, ynew1, deg + 45, step - 1)


t.penup()
# t.goto(0, 200)
t.pendown()
square(100, 0, -250, 0, mainstep)
done()
