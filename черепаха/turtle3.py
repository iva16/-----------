import turtle
t=turtle.Turtle()
t.shape('turtle')
t.color('darkgreen','yellow')
t.shapesize(2)
t.begin_fill()
for i in range(5):
    for k in range(3):
        t.forward(100)
        t.left(360/3)
    t.forward(100)
    t.right(360/5)
t.end_fill()
t.hideturtle()

