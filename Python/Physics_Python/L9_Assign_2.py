from vpython import *

t = 0.0 ; t1 = 0.0  ; dt = 0.0001 #時間參數
theta = 0.0 * pi / 180 #氣體入射角度
d = 3.0  #氣體與牆壁距離
r = 0.50  #氣柱半徑
v0 = 2.0  # 氣體初速率
m = 0.01  #單一氣體質量
K = 5.0  #牆壁碰撞參數
per_N = 5.0 #每秒射出的氣體數
k = 9*10**9
Q_charge = 10**(-5)
q_charge = 10**(-8)
q_m = 10**(-3)

scene = canvas(align = 'left' , center = vec ( -0.5*d , 0 , 0 ) , height=600, width=1000, range=3.5,auto_scale=False, background=vec(0,0,0) , fov = 0.004)  #設定畫面

gas = []  #氣體的List

Q = sphere(pos = vec(0,0,0) ,  radius = 0.2 , color = color.yellow)

def Force_E(r, q):
    r1 = r - Q.pos
    return k*q*Q_charge*r1.norm()/(r1.mag*r1.mag)   

sum_F = 0  #計算程式中每顆小球撞擊牆壁時的總力

while True:
    rate(10000)
    t = t + dt       #時間
    t1 = t1 + dt  
    sum_F = 0     #每千分之一秒，程式內的總力要歸零重算

    if t1 > 1/ per_N:  # 設定per_N = 100.0時，則每1/100秒會射出一顆空氣分子
        t1 = 0  
        r_dom = random()  #空氣射出的位置隨機參數
        p_dom = random() #空氣射出的角度位置參數
        gas.append(sphere(pos = vector((-d*cos(theta)+r*r_dom*cos(p_dom*2*pi)*sin(theta)),(d*sin(theta)+r*r_dom*cos(p_dom*2*pi)*cos(theta)),(r*r_dom*sin(p_dom*2*pi))) , radius = 0.05, v = vec(v0*cos(theta),-v0*sin(theta),0) , Fx = 0 , visible = True, make_trail = True))
        # 每1/100秒會產生一個隨機位置的空氣分子，以相同的速度射出
            
    for N in gas :  
        N.pos = N.pos+N.v*dt  #讓粒子等速前進
        N.v = N.v + Force_E(N.pos, q_charge)/q_m *dt
        N.pos = N.pos+N.v*dt
        if mag(N.pos -  vec(0,0,0) ) > 4: #若粒子離原點超過4的距離就會從List消除
            N.visible = False
            N = None
