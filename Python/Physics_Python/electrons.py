"""
    建國中學 Vpython物理模擬
    作者: 物理科 賴奕帆老師
    日期: 107/08/31
    特色課程 Lecture 10 
    10_2_4_mouse_control Example_Electric field simulation.py
"""
from vpython import *  #引用視覺畫套件Vpython
k = 9*10**9      
size = 0.4  # charge size
t = 0 ; dt = 0.001
b_N = 20

Q1_charge = 1*10**(-5) #Q1電量 
Q1_position = vector(-2, 0, 0) #Q1位置
Q2_charge = -1*10**(-5) #Q2電量 
Q2_position = vector(2, 0, 0) #Q2位置

q_charge = 1 * 10 **(-7)
q_position = vector (1 , 1 , 0)
q_m = 10**(-3)
q_v = vector (0 , 0 , 0)

scene = canvas(title='dipole', height=600, width=1000, range=5.0,
                auto_scale=False, background=vec(1.0,1.0,1.0))

Q1 = sphere(pos = Q1_position , radius = size , color = color.blue)
Q2 = sphere(pos = Q2_position , radius = size , color = color.red)

field_ball_1=[]
for N in range(0,b_N,1):#build field ball from wall
    field_ball_1.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Q1_position,
                             radius=0.01, color=vec(1,1,0), make_trail=True, v=vector(0,0,0)))

field_ball_2=[]
for N in range(0,b_N,1):#build field ball from wall
    field_ball_2.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Q2_position,
                             radius=0.01, color=vec(0.8,0.8,0.3), make_trail=True, v=vector(0,0,0)))

def Force_E(r, q):#force of field 
    r1 = r - Q1_position
    r2 = r - Q2_position
    return k*q*Q1_charge*r1.norm()/(r1.mag*r1.mag)+k*q*Q2_charge*r2.norm()/(r2.mag*r2.mag)

q = []
def make_q_charge(evt):
    loc = evt.pos
    print ("click at ", loc)
    q.append(sphere(pos=loc, radius=0.2*size, color=color.green, make_trail=True,
                       v=vector(0,0,0)))
   
scene.bind('mousedown', make_q_charge)

while True:
    rate(1000)
        
    for N in field_ball_1:
        N.v = Force_E(N.pos, 1.0).norm()
        N.pos += N.v*dt

    for N in field_ball_2:
        N.v = Force_E(N.pos, -1.0).norm()
        N.pos += N.v*dt

    for N in q:
        
        if mag(N.pos-Q1_position)>=size and mag(N.pos-Q2_position)>=size :
            N.v = N.v + Force_E(N.pos, q_charge)/q_m *dt
            N.pos = N.pos+N.v*dt
        else : 
            N.pos = N.pos
