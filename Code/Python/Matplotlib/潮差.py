import matplotlib.pyplot as plt
import numpy as  np
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

x = [20, 621, 1158, 1819]
y = [190, -3, 166, -70]
z = [54, 555, 1150, 1828]
a = [96,34,117,-31]
s = [43, 656, 1339, 1951]
v = [-12, 108, -57, 72]

plt.plot(x, y,'-o', label = '新北市淡水區')
plt.plot(z, a,'-x', label = '台南市北門區')
plt.plot(s, v,'-^', label = '台東縣台東市')
plt.xlim(0000,2000,100)
plt.ylim(-100,200)
plt.legend(loc = 'upper right')
plt.title('台灣各地國曆8/10潮差')
plt.grid()
plt.show()