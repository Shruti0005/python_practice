import turtle as t
import random

tom_the_turtle = t.Turtle()
tom_the_turtle.shape("turtle")

direction_list = (0, 90, 180, 270)

tom_the_turtle.speed(0)

t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    color = (r, g, b)
    return color


for _ in range(200):
    tom_the_turtle.color(random_color()) 
    tom_the_turtle.pensize(10)
    tom_the_turtle.forward(20)
    tom_the_turtle.setheading(random.choice(direction_list))


screen = t.Screen()
screen.exitonclick()
