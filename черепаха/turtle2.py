import turtle
t=turtle.Turtle()
t.shape('turtle')
t.color('darkgreen')
t.shapesize(2)
t.begin_fill()
for i in range(10):
    t.forward(100)
    t.right(360/5)
t.end_fill()    
