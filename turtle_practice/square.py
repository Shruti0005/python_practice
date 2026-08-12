import turtle as t

tom_the_turtle = t.Turtle()
tom_the_turtle.color("DarkOliveGreen")

for _ in range(4):
    tom_the_turtle.forward(100)
    tom_the_turtle.left(90)


screen = t.Screen()
screen.exitonclick()
