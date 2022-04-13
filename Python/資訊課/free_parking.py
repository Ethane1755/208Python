a=int(input())

for i in range(1,a+1):
    b=input()
    c,d,e=b.split()
    c=int(c)
    d=int(d)
    e=int(e)
    f=[]
    for i in range(c+1,d):
        if i%e!=0:
            f.append(i)
    if f!=[]:
        print(*f)
    elif f==[]:
        print('No free parking spaces.')
