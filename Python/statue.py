import numpy as np
n = input('please input the name of the statue here:')
s = float(input('please input statue height here(m):'))
p = float(input('please input height of the statue base here(m):'))
d = np.sqrt(s*p+p**2)
print('the best distance for watching',n, 'is:',d,'m')