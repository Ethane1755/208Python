import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
np1 = np.genfromtxt('D:/Database/練習資料/海水變化_日期.csv', delimiter=',')
np2 = np.genfromtxt('D:/Database/練習資料/海水變化_公尺.csv', delimiter=',')
a = np.linspace(1880, 2015, 1608)
plt.plot(a, np2)
plt.xlim(1880,2015)
plt.xlabel('years')
plt.ylim(-200,85)
plt.text(2008,-197,'謝氏製圖')
plt.ylabel('global mean sea level(m)')
plt.title('Global Mean Sea Levels(1880~2015)')
plt.grid()
plt.show()
