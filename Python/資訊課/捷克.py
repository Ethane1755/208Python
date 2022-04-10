from math import sqrt
a=int(input())

i = 0
while (i<a):
    b=input()
    d,e=b.split()
    d=int(d)
    e=int(e)
    k=sqrt(d+e)
    if 0<100-k*k<=30:
        print('sad!')
    elif 30<100-k*k<=60:
        print('hmm~~')
    elif 60<100-k*k<100:
        print("Happyyummy")
    else:
        print("evil!!")
    i=i+1
