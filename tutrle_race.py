from turtle import Turtle
from random import randint


red = Turtle()
red.color('red')
red.shape('turtle')
red.penup()
red.goto(0, 0)
red.pendown()



blue = Turtle()
blue.color('blue')
blue.shape('turtle')
blue.penup()
blue.goto(0, 20)
blue.pendown()


green = Turtle()
green.color('green')
green.shape('turtle')
green.penup()
green.goto(0, 40)
green.pendown()



yellow = Turtle()
yellow.color('yellow')
yellow.shape('turtle')
yellow.penup()
yellow.goto(0, 60)
yellow.pendown()



for movement in range(100):
    blue.forward(randint(1,5))
    red.forward(randint(1,5))
    green.forward(randint(1,5))
    yellow.forward(randint(1,5))


    





input("End of the program")