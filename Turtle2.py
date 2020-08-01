import turtle
a=turtle.Turtle()
a.color("red")
a.shape("turtle")
a.circle(180,steps=3)
a.pu()
a.left(72)
a.forward(150)
a.pd()
a.circle(45)
a.pu()
for i in range(1000):
    a.left(20)
    a.forward(10)