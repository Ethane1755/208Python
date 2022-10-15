from vpython import *  
import pandas as pd

G = 6.67 ; m1 = 5.2 ; m2 = 0.05 ; m3 = 0.00000000610 ; R = 11.8 ; v_m2 = (G*m1/R)**0.5 ; t = 0 ; dt = 0.001 ; k = 5
def Fg(x):
    return -G*m1*m2/(x**2)

scene = canvas(width=1200, height=800, center=vec(0,0,0),
                background=vec(0.6,0.8,0.8),range=2*R)
ra = 2*R*pi/v_m2
ball_m1_v = vector(0,-v_m2*(m2/m1),0)
ball_m2_v = vector(0,v_m2,0)
ball_m3_v = vector(-6.258,0,0)
ball_m1 = sphere(pos=vector(0,0,0), radius=3.9, color = color.blue, make_trail=True)
ball_m2 = sphere(pos=vector(R,0,0), radius=1.71, color = color.red, make_trail=True)
ball_m3 = sphere(pos=vector((mag(ball_m3_v)*ra)+8,0,0), radius=2, color = color.black)

list1 = []
list2 = []

while t<=180:
    rate(2000)
    dist = ((ball_m1.pos.x-ball_m2.pos.x)**2+(ball_m1.pos.y-ball_m2.pos.y)**2+(ball_m1.pos.z-ball_m2.pos.z)**2)**0.5   
    radiavector = (ball_m2.pos-ball_m1.pos)/dist
    Fg_vector = Fg(dist)*radiavector
    
    ball_m2_v += Fg_vector/m2*dt 
    ball_m2.pos = ball_m2.pos + ball_m2_v*dt

    ball_m1_v += -Fg_vector/m1*dt
    ball_m1.pos = ball_m1.pos + ball_m1_v*dt 
    ball_m3.pos = ball_m3.pos + ball_m3_v*dt

    if mag(ball_m2.pos - ball_m3.pos) <= 1.71 :
        ballm3_a = -1 * k * (1.71 - ( ball_m2.pos.x - ball_m3.pos.x )) / m3
        ballm2_a = k * (1.71- ( ball_m2.pos.x - ball_m3.pos.x )) / m2
        print('impact')
    else :                             #如果沒有，兩球的加速度均為0
        ballm3_a = 0
        ballm2_a = 0
    
    ball_m3_v = ball_m3_v + vector(ballm3_a,0,0) *dt  #加速度是向量，所以要用vector(ball1_a,0,0)
    ball_m2_v = ball_m2_v + vector(ballm2_a,0,0) *dt
    t = t+dt
    list1.append(ball_m2.pos.x)
    list2.append(t)
data = pd.DataFrame(list(zip(list1, list2)),columns =['x', 't'])
data.to_csv('out.csv')