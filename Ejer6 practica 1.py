from turtle import *
pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)
tortuga = Turtle()
l=float(input('¿Cuánto mide el lado?' ))
tortuga.goto(l, 0)
tortuga.goto(l, l)
tortuga.goto(0, l)
tortuga.goto(0, 0)

pantalla.exitonclick()
