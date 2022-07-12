import random
from turtle import Turtle, Screen, forward
import turtle

screen = Screen()
screen.setup(1000,900)
screen.bgcolor("black")



finishline= Turtle("turtle")
finishline.color("white")
finishline.penup()
finishline.goto(400,300)
finishline.pendown()
finishline.goto(400,-300)

finishline.hideturtle()





turtlelist = [ Turtle("turtle", visible = False),
        Turtle("turtle", visible =False),
    Turtle("turtle", visible =False),
    Turtle("turtle", visible =False),
    Turtle("turtle", visible =False),
    Turtle("turtle", visible =False),
    Turtle("turtle", visible =False),
    Turtle("turtle", visible =False)]

turtlecolourlist=["red","blue","lightblue","lightgreen","purple","brown","yellow","orange"]

for i in range(0 ,len(turtlelist)):
    turtlelist[i].color(turtlecolourlist[i])
    turtlelist[i].penup()
    turtlelist[i].goto(-450, i* 50 -200)
    turtlelist[i].showturtle()
    turtlelist[i].shapesize(1,1)

while True:
    for i in range(0, len(turtlelist)):
        turtlelist[i].forward(random.randint(1,5))

        if turtlelist[i].pos()[0]>400:
            screen.exitonclick()









