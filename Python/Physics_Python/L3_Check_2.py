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

scene = canvas(width=600, height=600, center=vector(0, -L*0.8, 0), range=1.2*L)#設定畫面
ceiling = box(length=0.4, height=0.005, width=0.4, opacity = 0.2)#畫天花板
ball = sphere(radius = size,  color=color.yellow, make_trail = True, retain = 1000, interval=1)#畫球
rod = cylinder(radius=size/10)#畫棒子

v_vector = arrow(shaftwidth = 0.02, color=color.green)
Ftot_vector = arrow(shaftwidth = 0.02, color=color.red)
mg_vector = arrow(shaftwidth = 0.02, color=color.yellow)
Fs_vector = arrow(shaftwidth = 0.02, color=color.white)

v_text = label(box = False, opacity = 0, height = 25, color=color.green, text = 'v')
Fs_text = label(box = False, opacity = 0, height = 25, color=color.white, text = 'Fs')
mg_text = label(box = False, opacity = 0, height = 25, color=color.yellow, text = 'mg')
Ftot_text = label(box = False, opacity = 0, height = 25, color=color.red, text = 'F_tot')

ball.pos = vector(L*sin(theta), -L*cos(theta), 0)   #球的初始位置
vz = (g*L*sin(theta)*tan(theta))**0.5
ball.v = vector(0, 0, vz)                            #球初速
rod.pos = vector(0, 0, 0)                           #棒子頭端的位置

dt = 0.001    #時間間隔
t = 0.0       #初始時間

pre_x = ball.pos.x         #三點記錄法，初始設定

while True:
    rate(1/dt)
    rod.axis = ball.pos - rod.pos                #桿子的軸方向：由桿子頭端指向尾端的向量
    ball.a = (Fg + SpringForce(rod.axis,L)+SpringDamp(ball.v, rod.axis))/m    #牛頓第二定律：加速度＝合力/質量

    pre_pre_x = pre_x      #三點記錄法，前前時刻x座標
    pre_x = ball.pos.x     #三點記錄法，前一時刻x座標

    ball.v += ball.a*dt    #速度
    ball.pos += ball.v*dt  #三點記錄法，現在時刻x座標
    t += dt

    Ug = m * g * (ball.pos.y + 0.5)
    Us = 0.5 * k * (mag(rod.axis) - L)**2
    K = 0.5 * m * mag(ball.v)**2
    F = Ug+Us+K
    
    v_vector.pos = ball.pos + vector(2.5*size,0,0)      #將速度箭頭設定在球的右方2.5size處
    v_vector.axis = ball.v/4
    
    Ftot_vector.pos = ball.pos + vector(-2.5*size,0,0)  #將合力箭頭設定在球的左方2.5size處
    Ftot_vector.axis = vector(0,(-m*g)+mag(SpringForce(rod.axis,L)),0)/4
    
    mg_vector.pos = ball.pos    #將重力箭頭設定在球上
    mg_vector.axis =vector(0,-m*g,0)/4
    
    Fs_vector.pos = ball.pos    #將彈力箭頭設定在球上
    Fs_vector.axis = SpringForce(rod.axis,L)/4
    
    v_text.pos = v_vector.pos + v_vector.axis*1.2
    Ftot_text.pos = Ftot_vector.pos + Ftot_vector.axis*1.2
    mg_text.pos = mg_vector.pos + mg_vector.axis*1.2
    Fs_text.pos = Fs_vector.pos + Fs_vector.axis*1.2

    if pre_x > pre_pre_x and pre_x > ball.pos.x:    #計算單擺週期
        print ('simulated period = ', t, ', theoretical period = ', 2*pi*(L*cos(theta)/g)**0.5 )    #印出單擺週期
        t = 0    #印出單擺週期
