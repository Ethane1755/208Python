import turtle
t=turtle.Turtle()

k=120
t.speed(5)

for c in ['#ebf2fd','#c3d8f9','#9bbef5','#5f97ef','#4b8aed','#377deb']:
  t.fillcolor(c)
  t.begin_fill()
  for j in range(1,5):
    t.forward(k)
    t.left(72)
  k=k-10
  t.end_fill()

turtle.done()
