a=int(input())

c=[]
for i in range(a):
    b=[]
    k=input()
    m=input()
    h=k.split()
    n=m.split()
    if h[1]!=h[3] and h[1]==h[5] and n[1]!=n[3] and n[1]==n[5]:
        c.append(1)
    else:
        b.append('A')
    if h[6]=='1' and n[6]=='0':
        c.append(1)
    else:
        b.append('B')
    if h[1]!=n[1] and h[3]!=n[3] and h[5]!=n[5]:
        c.append(1)
    else:
        b.append('C')
    if b==[]:
        print('None')
    else:
        print(''.join(b))