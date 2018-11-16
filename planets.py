import turtle
import math
wn = turtle.Screen()
turtle.screensize(900,900,"black")
turtle.speed(0)
colors = ["sea green","yellow","blue","orange","green","gray"]
sun = turtle.Turtle()
Mercury = turtle.Turtle()
Venus = turtle.Turtle()
earth = turtle.Turtle()
Mars = turtle.Turtle()
Jupiter = turtle.Turtle()
Saturn = turtle.Turtle()

turtle.hideturtle()
turtle.penup()
turtle.goto(30,-15)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("red")
turtle.circle(20)
turtle.end_fill()

def place(planet,a,n):
    planet.shape("circle")
    planet.up()
    planet.fd(a)
    planet.down()
    planet.color(colors[n])

place(Mercury,100,0)
place(Venus,130,1)
place(earth,160,2)
place(Mars,200,3)
place(Jupiter,250,4)
place(Saturn,300,5)

def planet(planet,a,θ):
    b = (a**2-30**2)**0.5
    x = a * math.cos(θ*0.006)
    y = b * math.sin(θ*0.006)
    planet.goto(x,y)

for θ in range(1000):
    planet(Mercury,100,16*θ)
    planet(Venus,130,14*θ)
    planet(earth,160,12*θ)
    planet(Mars,200,10*θ)
    planet(Jupiter,250,8*θ)
    planet(Saturn,300,6*θ)

turtle.done()



