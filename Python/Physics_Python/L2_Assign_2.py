from vpython import *

g = 9.8                 
size = 1.0            
height = 15.0           
m = 1.0                 
Fg = vector(0, -m*g, 0) 
v = 20
theta = 3*pi/180
damp = 0

scene = canvas(width=600, height=600,x=0, y=0, center = vector(0,height/2,0)) 
floor = box(length=60, height=0.01, width=10, color=color.green)     
ball1 = sphere(radius = size, color=color.yellow, make_trail= True,trail_type='points', interval=10)     
gd = graph(width=600, height=400)
f1 = gcurve(color=color.red)  


ball1.pos = vector(0, size, 0)
ball1.v = vector(v*cos(theta), v*sin(theta), 0)

dt = 0.001    
t = 0.0        
k=0.0001
while True: 
    rate(1/dt)
    t = t+dt
    ball1.a = (-damp*ball1.v+vector(0,-m*g,0))/m
    ball1.v += ball1.a*dt    
    ball1.pos += ball1.v*dt 
    
    if ball1.pos.y < size and ball1.v.y<0:
        f1.plot(pos=(t,ball1.pos.x))
        theta = theta+5*pi/180
        ball1.pos = vector(0,size,0) 
        ball1.v = vector(v*cos(theta), v*sin(theta), 0)
    t1 = str('theta='+str(round(theta/pi*180)))
    show_angle = label(pos=vector(0,-7*size,0), box = False, height = 20, color=color.yellow)
    show_angle.text=t1
    

    

