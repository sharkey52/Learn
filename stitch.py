import turtle
import random
turtle.speed(10)
turtle.penup()
turtle.goto(10,10)
tp = turtle.pos()

def go(crit,axis):
    if crit ==1:
        turtle.forward(10)
    else:
        pass
    
    while crit < 10:
        crit = crit + 1
        turtle.forward(10)
        turtle.pendown()
        turtle.forward(10)
        turtle.penup()

    goback(axis)

def goback(axis):
    tp = turtle.pos()
    if axis == 'across':
        turtle.goto(10,((tp[1])-10))
    else:
        turtle.goto(((tp[0])+10),10)
  
            
n = 0
while n < 20:
    n = n + 1
    crit = random.randint(0,1)
    go(crit,'across')
    
turtle.goto(20,10)
turtle.right(90)
    
n = 0
while n < 20:
    n = n + 1
    crit = random.randint(0,1)
    go(crit,'down')
    
    
