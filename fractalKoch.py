from turtle import *

depth = int(input())
length = 5
t=Turtle()
t.speed(0)
n=60


def Recursive_Koch(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        Recursive_Koch(length, depth-1)
        t.right(n)
        Recursive_Koch(length, depth-1)
        t.left(2*n)
        Recursive_Koch(length, depth-1)
        t.right(n)
        Recursive_Koch(length, depth-1)

# t.penup()
# t.setposition(-700, 300)
# t.pendown()

Recursive_Koch(length, depth)
t.left(120)
Recursive_Koch(length, depth)
t.left(120)
Recursive_Koch(length, depth)

done()