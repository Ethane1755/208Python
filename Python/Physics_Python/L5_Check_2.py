from vpython import *  #引用視覺畫套件Vpython

G = 6.67*10**(-11) ; M = 6*10**24 ; m = 1000  
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 1 ; V0 = (G*M/H)**0.5
def Fg(x):                                 #定義公式
    return -G*M*m/(x**2)

scene = canvas(align = 'left',title ='4_01_Gravity force',  width=400, height=400, center=vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定視窗
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth) #放置物件地球
mater = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.blue, make_trail=True) #放置物件衛星
materv = vec(0,0.7*V0,0) #衛星速率=0
mater1 = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.red, make_trail=True) #放置物件衛星
mater1v = vec(0,0.8*V0,0) #衛星速率=0
mater2 = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.yellow, make_trail=True) #放置物件衛星
mater2v = vec(0,V0,0) #衛星速率=0
gd = graph(align='left',width=400,height=400,  #設定X-t繪圖視窗
              title='Fg', xtitle='R', ytitle='Fg(red)',
              foreground=color.black,background=color.white,ymax = 4e10)
f1 = gcurve(color=color.red)  #定義曲線
f2 = gcurve(color=color.black)  #定義曲線
f3 = gcurve(color=color.green)
Fe = G*M*m/Re**2 #定義地球表面重力強度
oval = curve( color = color.black )
pre_mater_pos = vector(0,0,0)

while True:  #執行迴圈
    rate(5000)

    dist = ((mater.pos.x-earth.pos.x)**2+(mater.pos.y-earth.pos.y)**2+(mater.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector = (mater.pos-earth.pos)/dist #距離單位向量
    Fg_vector = Fg(dist)*radiavector # 萬有引力向量=萬有引力量值*單位向量
    
    dist2 = ((mater2.pos.x-earth.pos.x)**2+(mater2.pos.y-earth.pos.y)**2+(mater2.pos.z-earth.pos.z)**2)**0.5
    radiavector2 = (mater2.pos-earth.pos)/dist2 
    Fg_vector2 = Fg(dist2)*radiavector2  
    mater2v += Fg_vector2/m*dt   
    mater2.pos = mater2.pos + mater2v*dt  
    
    dist1 = ((mater1.pos.x-earth.pos.x)**2+(mater1.pos.y-earth.pos.y)**2+(mater1.pos.z-earth.pos.z)**2)**0.5
    radiavector1 = (mater1.pos-earth.pos)/dist1 
    Fg_vector1 = Fg(dist1)*radiavector1
    mater1v += Fg_vector1/m*dt   
    mater1.pos = mater1.pos + mater1v*dt 
    
    materv += Fg_vector/m*dt   #Δv = F/m *dt
    mater.pos = mater.pos + materv*dt  # S = S0 + v *dt


  
    t = t+dt

   