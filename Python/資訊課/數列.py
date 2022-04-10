a=int(input())

i = 0
while (i<a):
    b=input()
    d,e,f=b.split()
    d=int(d)
    e=int(e)
    f=int(f)
    if  e-d+1==f-e:
        k=f+(f-e+1)
    elif e//d+1==f//e:
        k=f*(f/e+1)
    k=int(k)
    print(d, e, f, k)
    i=i+1
