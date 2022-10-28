from turtle import Screen, Turtle

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('green')


for i in range(10):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()
    timmy_the_turtle.rt(90)










screen = Screen()
screen.exitonclick()