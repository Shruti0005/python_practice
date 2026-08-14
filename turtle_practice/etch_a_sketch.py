from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

user_choice = screen.textinput(title="Pen color", prompt="Which color do you want for pen to draw?")

if user_choice:
    tom.color(user_choice)

def move_forward():
    tom.forward(10)

def move_backward():
    tom.backward(10)
    
def turn_left():
    new_angle = tom.heading() + 10
    tom.setheading(new_angle)
    
def turn_right():
    new_angle = tom.heading() - 10
    tom.setheading(new_angle)    
    
def clear_screen():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()
    
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()
