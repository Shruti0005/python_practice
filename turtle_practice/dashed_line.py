import turtle as t

tom_the_turtle = t.Turtle()

for _ in range(15):
    tom_the_turtle.forward(10)
    tom_the_turtle.penup()
    tom_the_turtle.forward(10)
    tom_the_turtle.pendown()
    

screen = t.Screen()
screen.exitonclick()
