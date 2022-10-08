import turtle
from turtle import Turtle, Screen
sona = Turtle()
screen = Screen()


def move_forward():
    sona.forward(100)


def move_backwards():
    sona.backward(100)


def move_counterClockwise():
    sona.left(60)


def move_clockwise():
    sona.right(60)


def clear():
    sona.clear()
    sona.penup()
    sona.home()
    sona.pendown()


screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=move_counterClockwise)
screen.onkey(key="d",fun=move_clockwise)
screen.onkey(key="c",fun=clear)
screen.exitonclick()