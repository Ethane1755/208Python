from vpython import *
#Web VPython 3.2

size = 0.1

scene = canvas(width=600, height=400, center=vector(2.5,0,0), background=vector(0,0,0))
#設定物件視窗的顯示畫面與背景，寬為600畫素、高為400畫素
#center為畫面中心，background為背景顏色

x = arrow(pos=vector(0,0,0), axis=vector(1,0,0), shaftwidth=0.02, color=color.green)
y = arrow(pos=vector(0,0,0), axis=vector(0,1,0), shaftwidth=0.02, color=color.red)
z = arrow(pos=vector(0,0,0), axis=vector(0,0,1), shaftwidth=0.02, color=color.blue)
ball = sphere(radius=size, color=color.yellow, pos=vector(0,0,0), v=vector(0,0,0))

gd = graph(title = "x-t plot", width=600, height=400, xtitle="t", ytitle="x")
f1 = gcurve(color=color.blue)  
gd1 = graph(title = "v-t plot", width=600, height=400, xtitle="t", ytitle="x")
f2 = gcurve(color=color.green)
gd3 = graph(title = "a-t plot", width=600, height=400, xtitle="t", ytitle="x")
f3 = gcurve(color=color.red)
#設定函數圖的畫面

dt = 0.001
t = 0.0
v=vector(0,0,0)


while t<3:
    rate(1/dt)
    t = t+dt
    while t<2:
        a=vector(5.0,0,0)
    else:
        a=vector(-5.0,0,0)
    ball.pos = ball.pos + (v+a*t)*dt
    ball.v = ball.v + a*dt
    ball.a = a
    f1.plot(pos=(t,ball.pos.x))	#每一個迴圈畫一個點描出線條，x軸為時間，y軸為位置
    f2.plot(pos=(t,ball.v.x))
    f3.plot(pos=(t,ball.a.x))
    if ball.v.x < 0 and ball.v.x + ball.a.x*dt > 0:
        print('time:',t)
        print('position:',ball.pos.x)
        print('velocity:',ball.v.x)