# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 20:25:30 2021

@author: USER
"""

import matplotlib.pyplot as plt

labels = 'p','y','t','h','o','n' # 標籤
sizes = [10,20,30,10,20,10] # 百分比
explode = (0,0,0.1,0,0,0) # 突出

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)

plt.axis = ('equal') # 控制為平面
plt.savefig('D:/Database/Python/Spyder/pie_chart')
plt.show()


