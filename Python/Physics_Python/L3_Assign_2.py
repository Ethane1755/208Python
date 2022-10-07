from vpython import *


g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.05             #球半徑 0.05 m            
L = 0.5                 #彈簧原長 0.5m
k = 100000              #彈簧力常數 100000 N/m
m = 0.1                 #球質量 0.1 kg
theta = 30 * pi/180     #初始擺角
Fg = m*vector(0,-g,0)   #球所受重力向量
damp = 1

def SpringForce(r,L):
    return -k*(mag(r)-L)*r/mag(r)
    
def SpringDamp(v, r):  #避震器
    cos_theta = dot(v,r)/(mag(v)*mag(r))                    #用向量內積找v和r夾角的餘弦函數
    r_unit_vector = norm(r)                                 #沿彈簧軸方向的單位向量
    projection_vector = mag(v) * cos_theta * r_unit_vector  #計算v在r方向的分量
    spring_damp = - damp * projection_vector                #沿彈簧軸方向的阻力
    return spring_damp

scene = canvas(width=1500, height=700, center=vector(0, -L*0.8, 0), range=1.2*L)#設定畫面
ceiling = box(length=0.4, height=0.005, width=0.4, opacity = 0.2)#畫天花板
ball = sphere(radius = size,  color=color.red, make_trail = True, retain = 5000, interval=1)#畫球
ball1 = sphere(radius = size,  color=color.green, make_trail = True, retain = 5000, interval=1)#畫球
rod = cylinder(radius=size/10)#畫棒子
rod1 = cylinder(radius=size/10)#畫棒子

gd = graph(title = "x-t plot", width=600, height=400, xtitle="t", ytitle="x")
f1 = gcurve(color=color.red)  
f2 = gcurve(color=color.green)  

ball.pos = vector(L,0, 0)   #球的初始位置
ball1.pos = vector(2*L,0, 0)   #球的初始位置
ball.v = vector(0.00000000000001, 0, 0)      
ball1.v = vector(0.00000000000001, 0, 0)                        #球初速
rod.pos = vector(0, 0, 0)          
rod1.pos = vector(L, 0, 0)                  #棒子頭端的位置

dt = 0.001    #時間間隔
t = 0.0       #初始時間

pre_x = ball.pos.x         #三點記錄法，初始設定

while t<10:
    rate(1/dt)
    rod1.pos = ball.pos                 #外棒的位子在紅球處
    rod.axis = ball.pos                #內棒的軸方向由原點指向紅球
    rod1.axis = ball1.pos - ball.pos   #外棒的軸方向由紅球指向綠球
    ball.a = (Fg + SpringForce(rod.axis,L)+SpringDamp(ball.v, rod.axis))/m    #牛頓第二定律：加速度＝合力/質量
    ball1.a = (Fg + SpringForce(rod1.axis,L)+SpringDamp(ball1.v, rod1.axis))/m    #牛頓第二定律：加速度＝合力/質量
    F1 = vector(0, -m*g, 0) + SpringForce(rod.axis,L) - SpringForce(rod1.axis,L)
    F2 = vector(0, -m*g, 0) + SpringForce(rod1.axis,L)

    pre_pre_x = pre_x      #三點記錄法，前前時刻x座標
    pre_x = ball.pos.x     #三點記錄法，前一時刻x座標

    ball.v += F1/m*dt    #速度
    ball.pos += ball.v*dt  #三點記錄法，現在時刻x座標
    ball1.v += F2/m*dt    #速度
    ball1.pos += ball1.v*dt  #三點記錄法，現在時刻x座標
    t += dt

    f1.plot(pos=(t,mag(F1)))    
    f2.plot(pos=(t,mag(F2)))  


