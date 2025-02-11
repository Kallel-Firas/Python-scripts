from turtle import*
def function(x):
    return 0.05*x**3
   
speed(0)
goto(-450,0)
goto(450,0)
penup()
goto(0,450)
pendown()
goto(0,-450)
penup()
x=-30
for i in range(0,1000):
    x+=0.1
    goto(x*10,function(x))
    pendown()
