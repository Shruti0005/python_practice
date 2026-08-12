import turtle as t


tom_the_turtle = t.Turtle()
tom_the_turtle.color("MediumVioletRed")


for _ in range(2):
    tom_the_turtle.forward(200)
    tom_the_turtle.left(90)
    tom_the_turtle.forward(100)
    tom_the_turtle.left(90)
    

screen = t.Screen()
screen.exitonclick()
