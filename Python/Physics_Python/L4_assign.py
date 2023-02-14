"""
    建國中學 Vpython物理模擬
    作者: 物理科 賴奕帆老師
    日期: 107/07/25
    特色課程 Lecture 04 碰撞
    4_02_collision with formula_Y.py

"""
from vpython import *  #引用視覺畫套件Vpython
"""
    1. 參數設定
"""
m1 = 1
m2 = 10
g=9.8                 #重力加速度 9.8 m/s^2
size = 1              #球半徑 1 m
height_1 = 20.0       #球1初始高度
height_2 = 18.0       #球2初始高度
dt = 0.001                              #時間間隔 0.001 秒
"""
    2. 畫面設定
"""
scene = canvas(width=400, height=600, center = vec(0,height_1,0), background=vec(0.6,0.8,0.8)) #設定畫面
floor = box(length=15, height=0.01, width=10, color=color.blue)                         #畫地板
ball_1 = sphere(radius = size, color=color.yellow ) #畫球
ball_2 = sphere(radius = size, color=color.green ) #畫球


ball_1.pos = vector( 0, size+height_1, 0)        #球初始位置       
ball_1.v = vector( 0, 0, 0)                    #球初速 
ball_2.pos = vector( 0, size+height_2, 0)        #球初始位置       
ball_2.v = vector( 0, 0, 0)                    #球初速 

y1_lab = label(pos=vec(8.0,20.0,0), box = True , color = color.black)
y2_lab = label(pos=vec(8.0,12.0,0), box = True , color = color.black)
v1_lab = label(pos=vec(8.0,16.0,0), box = True , color = color.black)
v2_lab = label(pos=vec(8.0,8.0,0), box = True , color = color.black)

"""
    3. 執行迴圈
"""
while True:             
    rate(1000)                          #每一秒跑 1000 次

    ball_1.pos += ball_1.v*dt
    ball_1.v.y += - g*dt
    
    if ball_1.pos.y <= size and ball_1.v.y < 0:     
        ball_1.v.y = - 1* ball_1.v.y

    ball_2.pos += ball_2.v*dt
    ball_2.v.y += - g*dt
    
    if ball_2.pos.y <= size and ball_2.v.y < 0:     
        ball_2.v.y = - 1* ball_2.v.y

    if mag(ball_1.pos-ball_2.pos) <= 2*size  :
        v1y = ball_1.v.y-ball_2.v.y
        v2y = ball_2.v.y-ball_1.v.y
        ball_1.v = vector (0 , v1y , 0)
        ball_2.v = vector (0 , v2y , 0)

    y1_lab.text = str('y1 = %1.1f m'%ball_1.pos.y)
    y2_lab.text = str('y2 = %1.1f m'%ball_2.pos.y)
    v1_lab.text = str('v1 = %1.1f m/s'%ball_1.v.y)
    v2_lab.text = str('v2 = %1.1f m/s'%ball_2.v.y)