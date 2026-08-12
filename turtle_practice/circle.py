import turtle as t

tom_the_turtle = t.Turtle()
tom_the_turtle.color("navy", "CadetBlue")

tom_the_turtle.begin_fill()
tom_the_turtle.circle(80)
tom_the_turtle.end_fill()

screen = t.Screen()
screen.exitonclick()
