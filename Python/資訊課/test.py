import turtle

t=turtle.Turtle()

k=int(input())

for i in range(1,k+1):
    t.forward(20)
    t.left(180-((180*(k-2))/k))

turtle.done()

