import turtle as t
import random

tom_the_turtle = t.Turtle()
tom_the_turtle.color("red")

for _ in range(5):
    tom_the_turtle.forward(200)
    tom_the_turtle.right(144)


screen = t.Screen()
screen.exitonclick()
