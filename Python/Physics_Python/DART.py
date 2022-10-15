from re import A
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
ball_m3 = sphere(pos=vector((mag(ball_m3_v)*ra)+8,0,0), radius=0.2, color = color.black)
m1_text = label(box = False, opacity = 0, height = 25, color=color.blue, text = 'Didymos\nm=5.2x10¹¹kg')
m2_text = label(box = False, opacity = 0, height = 25, color=color.red, text = 'Dimorphos\nm=5x10⁹kg')
m3_text = label(box = False, opacity = 0, height = 15, color=color.black, text = 'DART\n610kg')

list1 = []
list2 = []
list3 = []

while t<=180:
    rate(500)
    dist = ((ball_m1.pos.x-ball_m2.pos.x)**2+(ball_m1.pos.y-ball_m2.pos.y)**2+(ball_m1.pos.z-ball_m2.pos.z)**2)**0.5   
    radiavector = (ball_m2.pos-ball_m1.pos)/dist
    Fg_vector = Fg(dist)*radiavector

    ball_m2_v += Fg_vector/m2*dt 
    ball_m2.pos = ball_m2.pos + ball_m2_v*dt

    ball_m1_v += -Fg_vector/m1*dt
    ball_m1.pos = ball_m1.pos + ball_m1_v*dt 
    ball_m3.pos = ball_m3.pos + ball_m3_v*dt

    m1_text.pos = vector(ball_m1.pos.x,ball_m1.pos.y-5.6,0)
    if ball_m2.pos.x>=0:
        m2_text.pos = vector(ball_m2.pos.x+8,ball_m2.pos.y,0)
    else:
        m2_text.pos = vector(ball_m2.pos.x-8,ball_m2.pos.y,0)
    m3_text.pos = vector(ball_m3.pos.x+3,ball_m3.pos.y,0)

    if mag(ball_m2.pos - ball_m3.pos) <= 1.71 :
        ballm3_a = -1 * k * (1.71 - ( ball_m2.pos.x - ball_m3.pos.x )) / m3
        ballm2_a = k * (1.71- ( ball_m2.pos.x - ball_m3.pos.x )) / m2
        print('impact at',t*967.27250/60,'min')
        Ek = 0.5*m2*(ballm2_a*0.000001)**2*100000000000*967.27520
        ball_m2 = sphere(pos=ball_m2.pos,radius=1.71, color = color.yellow, make_trail=True)
        m2_text = m2_text = label(box = False, opacity = 0, height = 20, color=color.yellow, text = 'Dimorphos(DARTed)\nm=5x10⁹kg')
    else :                         
        ballm3_a = 0
        ballm2_a = 0

    
    ball_m3_v = ball_m3_v + vector(ballm3_a,0,0) *dt  
    ball_m2_v = ball_m2_v + vector(ballm2_a,0,0) *dt
    t = t+dt
    list1.append(ball_m2.pos.x)
    list3.append(ball_m2.pos.y)
    list2.append(t)
    
data = pd.DataFrame(list(zip(list1,list3, list2)),columns =['x','y','t'])
data.to_csv('out.csv')
df = pd.read_csv('out.csv')

l1 = df['x'].tolist()
l2 = df['t'].tolist()
l6 = df['y'].tolist()
l3 = []
l4 = []
l5 = []
#l7 = []
#l8 = []
#l9 = []
#l10 = []
#l11 = []
#l12 = []
#l13 = []

for i in l1:
    if i!=l1[-1]:
        if i>l1[l1.index(i)-1] and i>l1[l1.index(i)+1]:
            l3.append(l1.index(i)) #max x
#            l13.append(i)
#    if i!=l1[-1]:
#        if i<l1[l1.index(i)-1] and i<l1[l1.index(i)+1]:
#            l7.append(i) #min x
#for i in l6:
#    if i!=l6[-1]:
#        if i>l6[l6.index(i)-1] and i>l6[l6.index(i)+1]:
#            l8.append(i) # max y
#    if i!=l6[-1]:
#        if i<l6[l6.index(i)-1] and i<l6[l6.index(i)+1]:
#            l9.append(i) #min y
for i in l3:
    l4.append(l2[i])

#a = (l13[0]-l7[0])/2
#b = (l8[0]-l9[0])/2
#a1 = (l13[-1]-l7[-1])/2
#b1 = (l8[-1]-l9[-1])/2

a = 11.8010910
b = 11.8005456
a1 = 12.1799935
b1 = 12.2570471763804
if a>b:
    Ecc = sqrt(1-b**2/a**2)
if a<b:
    Ecc = sqrt(1-a**2/b**2)
if a==b:
    Ecc = 0

if a1>b1:
    Ecc1 = sqrt(1-b1**2/a1**2)
if a1<b1:
    Ecc1 = sqrt(1-a1**2/b1**2)
if a1==b1:
    Ecc1 = 0

for i in l4:
    if l4.index(i)!=0:
        l5.append(i-l4[l4.index(i)-1])

time = l5[1]-l5[0]
meter = 42918/l5[0]
answer = time*meter
print('Affected orbital time:',answer/60,'min')
print('Dimorphos Eccentricity:',Ecc,'Dimorphos(DARTed) Eccentricity:',Ecc1)


