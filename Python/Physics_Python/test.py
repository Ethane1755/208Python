from vpython import *

size = 0.1
theta = 0.0
theta_probe = 45*pi/180
R = 1.0
omega = 2*pi

scene = canvas(width=500, height=500, center=vector(0,0,0), range=1.5*R, background=vector(148.0/255,228.0/255,204.0/255))
ball = sphere(radius=size, color=color.black, make_trail=True, interval=1, retain=1000)
ball1 = sphere(radius=2*size, color=color.blue, make_trail=True, interval=1, retain=1000)
probe =  sphere(radius=size, color=color.red, make_trail=True, interval=1, retain=1000)
ball.pos = vector(R,0,0)
ball1.pos = vector (0,0,0)
probe.pos = vector (2*R,R,0)
probe.v = vector(-R,-R,0)

dt = 0.001
t = 0.0

pre_theta = theta

while True:
    rate(1/dt)
    t = t + dt

    pre_pre_theta = pre_theta    #前前時刻角度
    pre_theta = theta            #前一時刻角度
    theta = theta + omega*dt     #現在時刻角度

    pre_pre_ball_pos = vector(R*cos(pre_pre_theta),R*sin(pre_pre_theta),0) #球前前時刻的位置
    pre_ball_pos = vector(R*cos(pre_theta),R*sin(pre_theta),0)             #球前一時刻的位置
    now_ball_pos = vector(R*cos(theta),R*sin(theta),0)                     #球現在時刻的位置
    ball.pos = pre_ball_pos    #將球物件畫在前一時刻的位置（ps.上面三個可任挑，dt很小肉眼看不出來差別）
    
    ball_v_12 = (pre_ball_pos - pre_pre_ball_pos)/dt   #前半程平均速度
    ball_v_23 = (now_ball_pos - pre_ball_pos)/dt       #後半程平均速度
    ball.v = ball_v_12         #將球的速度指定為前半程平均速度（ps.這兩個平均速度也可任挑，理由同上）
    
    ball.a = (ball_v_23 - ball_v_12)/dt
    ball_a_r = mag2(ball.v)/R