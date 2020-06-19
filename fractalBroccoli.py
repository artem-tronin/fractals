from turtle import *
t=Turtle()
t.speed(0)
n=90

def Recursive_Koch(length, depth):
    t.begin_fill()
    if depth == 0:
        t.forward(length)
    else:
        Recursive_Koch(length, depth - 1)
        t.right(n)
        Recursive_Koch(length, depth - 1)
        t.left(2*n)
        Recursive_Koch(length, depth - 1)
        t.right(n)
        Recursive_Koch(length, depth - 1)
        t.left(2*n)
    t.end_fill()


t.penup()
t.goto(-400, 100)
t.pendown()
Recursive_Koch(10, 10)
done()