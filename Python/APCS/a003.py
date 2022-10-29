a = input()
a = a.split()
a=list(map(int,a))

b = (a[0]*2+a[1])%3
if b == 0:
    print('普通')
if b == 1:
    print('吉')
if b == 2:
    print('大吉')