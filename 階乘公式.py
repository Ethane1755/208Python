# -*- coding: utf-8 -*-
import numpy as np
from math import factorial
N = int(input("please input your number here: "))
b = np.sqrt(2*np.pi)
d = N+0.5
c = pow(N,d)
A = b*c*np.exp(-N)
X = factorial(N)
P = ((X-A)/X)*100
print("斯特靈公式計算出的階乘概略:",A)
print("實際階乘為:",X)
print("相差百分比:",P,'%')