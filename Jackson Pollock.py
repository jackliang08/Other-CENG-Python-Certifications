import turtle
import random

t = turtle.Turtle()

def square():
    for i in range(4):
        t.forward(10)
        t.right(90)


while True:
    randD = random.randrange(-30,30)
    t.right(randD)
    t.forward(5)
    if(random.random() <= 0.1):
        square()


