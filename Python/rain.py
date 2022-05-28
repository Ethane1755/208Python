import numpy as np

D = float(input('please import the density of raindrops(kg/m3):'))
K = float(input('please import the angle of randrops:'))
V = float(input('please import the falling velocity of raindrops:'))
At = float(input('please import the area of your top:'))
Af = float(input('please import the area of your front:'))
H = float(input('please import the distance between you and your destination:'))
Vp = float(input('please import the speed you are running:'))

a = D*Af*H
b = (D*H*At*V*np.cos(K))
c = b/Vp
e = Af/At
d = c*(1-e* np.tan(K))
print(a*c*d)
#此公式有致命問題:原公式未給出單位
#僅做練習使用
