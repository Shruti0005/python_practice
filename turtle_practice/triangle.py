import turtle as t

tom_the_turtle = t.Turtle()
tom_the_turtle.color("Indigo")

for _ in range(3):
    tom_the_turtle.forward(200)
    tom_the_turtle.left(120)


screen = t.Screen()
screen.exitonclick()
