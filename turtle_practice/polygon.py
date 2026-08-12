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

def draw_shape(num_sides):
    angle = 360 / num_sides
    
    for _ in range(num_sides):
        tom_the_turtle.forward(100)
        tom_the_turtle.left(angle)
    

for shape_side_num in range(3, 11):
    tom_the_turtle.color(random_color())
    draw_shape(shape_side_num)
    


screen = t.Screen()
screen.exitonclick()
