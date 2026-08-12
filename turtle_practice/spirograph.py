import turtle as t
import random

tom_the_turtle = t.Turtle()

t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    color = (r, g, b)
    return color

tom_the_turtle.speed(0)
tom_the_turtle.width(2)

def drew_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tom_the_turtle.color(random_color())
        tom_the_turtle.circle(100)
        tom_the_turtle.setheading(tom_the_turtle.heading() + size_of_gap)


drew_spirograph(10)


screen = t.Screen()
screen.exitonclick()
